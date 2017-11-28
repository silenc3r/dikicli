import configparser
import os
import re
from bs4 import BeautifulSoup
from pathlib import Path

APP_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
HOME = Path.home()
XDG_CONFIG_HOME = Path(os.environ.get(
    'XDG_CONFIG_HOME', HOME.joinpath('.config')))
XDG_DATA_HOME = Path(os.environ.get(
    'XDG_DATA_HOME', HOME.joinpath('.local', 'share')))
XDG_CACHE_HOME = Path(os.environ.get(
    'XDG_CACHE_HOME', HOME.joinpath('.cache')))

CONFIG_FILE = XDG_CONFIG_HOME.joinpath('dikicli', 'diki.conf')
HISTORY_FILE = XDG_DATA_HOME.joinpath('dikicli', 'words.txt')
CACHE_DIR = XDG_CACHE_HOME.joinpath('dikicli')
TEMPLATE_FILE = APP_DIR.joinpath('template.html')

URL = 'https://www.diki.pl/{word}'
HEADERS = {'User-Agent': ('Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; '
                          'Trident/7.0;  rv:11.0) like Gecko')}


class WordNotFound(Exception):
    pass


def get_config(config_file=CONFIG_FILE):
    default_config = {
        'cache dir': CACHE_DIR.as_posix(),
        'history file': HISTORY_FILE.as_posix(),
        'prefix': '-',
        'linewrap': '78',
    }
    config = configparser.ConfigParser(defaults=default_config,
                                       default_section='dikicli')
    if config_file.is_file():
        with open(config_file, mode='rt') as f:
            config.read_file(f)
        return config

    # if config file doesn't exist and it's path is different from default
    # raise exception
    if config_file != CONFIG_FILE:
        raise FileNotFoundError(
            "Provided config file doesn't exist: {}".format(config_file))

    # write default config to file if it doesn't exist
    config_dir = config_file.parent
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    with open(config_file, mode='wt') as f:
        config.write(f)
    # TODO: logging
    return config


def parse(html_dump):
    soup = BeautifulSoup(html_dump, 'html.parser')
    for r in soup.find_all('div', class_='diki-results-left-column'):
        meanings_div = r.find_all('ol', class_='foreignToNativeMeanings')
        if meanings_div:
            parts = [p.get_text().strip()
                     for p in r.select('div.partOfSpeechSectionHeader')]
            assert len(parts) == len(meanings_div)
            break
    else:
        # if translation wasn't found check if there are any suggestions
        suggestions = soup.find('div', class_='dictionarySuggestions')
        if suggestions:
            raise WordNotFound(suggestions.get_text().strip())
        raise WordNotFound("Nie znaleziono tłumaczenia wpisanej frazy")

    translations = []
    for p, m in zip(parts, meanings_div):
        t = dict()
        t['part'] = p
        t['meanings_list'] = []
        for variant in m.find_all('li'):
            v = dict()
            v['meaning'] = [m.get_text() for m in variant.select('span.hw')]
            v['examples'] = []
            for e in variant.find_all('div', class_='exampleSentence'):
                pattern = re.compile('\s{3,}')
                example = pattern.sub(' ', e.get_text().strip())
                v['examples'].append(example)
            t['meanings_list'].append(v)
        translations.append(t)

    return translations


def parse_cached(word, cache_dir):
    pass


def cache_lookup(word, cache_dir):
    filename = cache_dir.joinpath('translations/{}.html'.format(word))
    if filename.is_file():
        try:
            translation = parse_cached(filename, cache_dir)
            return translation
        # TODO
        except Exception:
            pass


def get_words(words_file, prefix):
    with open(words_file, mode='rt') as f:
        return [l.rstrip()[len(prefix):] for l in f]


def write_to_file(words_file, word, prefix):
    if word not in get_words(words_file, prefix):
        with open(words_file, mode='at') as f:
            f.write(prefix + word + '\n')


def write_html_file(word, translations, cache_dir):
    content = []
    for t in translations:
        content.append("<br>")
        content.append("<p>[{part}]</p>".format(part=t['part']))
        for i, m in enumerate(t['meanings_list'], 1):
            content.append("<p><strong>{i}. {meaning}</p></strong>".format(
                i=i, meaning=', '.join(m['meaning'])))
            for e in m['examples']:
                content.append("<p>{example}</p>".format(example=e))
    content_str = '\n'.join(content)
    with open(TEMPLATE_FILE, mode='rt') as f:
        result = f.read()
        result = result.replace('{% word %}', word)
        result = result.replace('{% content %}', content_str)
    translations_dir = cache_dir.joinpath('translations')
    if not translations_dir.exists():
        translations_dir.mkdir()
    fname = translations_dir.joinpath('{}.html'.format(word))
    with open(fname, mode='wt') as f:
        f.write(result)


def write_index_file(words_file, prefix, cache_dir):
    content = ['<br>', '<ul>']
    for word in get_words(words_file, prefix):
        if cache_dir.joinpath('translations/{}.html'.format(word)).is_file():
            content.append(('<li><a href="translations/{word}.html">'
                            '{word}</a></li>').format(word=word))
    content.append('</ul>')
    content_str = '\n'.join(content)
    with open(TEMPLATE_FILE, mode='rt') as f:
        result = f.read()
        result = result.replace('{% word %}', "Index")
        result = result.replace('{% content %}', content_str)
    with open(cache_dir.joinpath('index.html'), mode='wt') as f:
        f.write(result)
