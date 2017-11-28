import configparser
import os
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
from itertools import zip_longest
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
        'use colors': 'yes',
        'web browser': 'default'
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
    trans_dict = OrderedDict()
    for entity in soup.find_all('div', class_='dictionaryEntity'):
        meanings = entity.find_all('ol', class_='foreignToNativeMeanings')
        if not meanings:
            continue
        word = tuple(e.get_text().strip()
                     for e in entity.select('h1 > span.hw'))
        parts = [p.get_text().strip()
                 for p in entity.select('span.partOfSpeech')]
        trans_list = []
        for p, m in zip_longest(parts, meanings):
            t = dict()
            t['part'] = p
            t['meanings_list'] = []
            for i in m.find_all('li'):
                v = dict()
                v['meaning'] = [m.get_text() for m in i.select('span.hw')]
                v['examples'] = []
                for e in i.find_all('div', class_='exampleSentence'):
                    pattern = re.compile('\s{3,}')
                    example = pattern.sub(' ', e.get_text().strip())
                    v['examples'].append(example)
                t['meanings_list'].append(v)
            trans_list.append(t)
        trans_dict[word] = trans_list
    if trans_dict:
        return trans_dict
    else:
        # if translation wasn't found check if there are any suggestions
        suggestions = soup.find('div', class_='dictionarySuggestions')
        if suggestions:
            raise WordNotFound(suggestions.get_text().strip())
        raise WordNotFound("Nie znaleziono tłumaczenia wpisanej frazy")


def parse_cached(html_dump):
    soup = BeautifulSoup(html_dump, 'html.parser')
    trans_dict = OrderedDict()
    for trans in soup.find_all('div', class_='translation'):
        word = tuple(t.get_text() for t in trans.select('div.word > h2'))
        trans_list = []
        for part in trans.find_all('div', class_='part-of-speech'):
            t = dict()
            pn = part.find('p', class_='part-name')
            if pn:
                pn = pn.get_text().strip('[]')
            t['part'] = pn
            t['meanings_list'] = []
            for meaning in part.find_all('div', class_='meaning'):
                m = dict()
                m['meaning'] = [meaning.find('li').get_text()]
                m['examples'] = [e.get_text() for e in meaning.find_all('p')]
                t['meanings_list'].append(m)
            trans_list.append(t)
        trans_dict[word] = trans_list
    return trans_dict


def cache_lookup(word, cache_dir):
    filename = cache_dir.joinpath('translations/{}.html'.format(word))
    if filename.is_file():
        with open(filename, mode='rt') as f:
            translation = parse_cached(f.read())
            return translation
    return None


def get_words(words_file, prefix):
    with open(words_file, mode='rt') as f:
        return [l.rstrip()[len(prefix):] for l in f]


def write_to_file(words_file, word, prefix):
    if word not in get_words(words_file, prefix):
        with open(words_file, mode='at') as f:
            f.write(prefix + word + '\n')


def write_html_file(word, translations, cache_dir):
    content = []
    for i1, entity in enumerate(translations):
        if i1 > 0:
            content.append("<br>")
        content.append("<div class=\"translation\">")
        content.append("<div class=\"word\">")
        for e in entity:
            content.append("<h2>{word}</h2>".format(word=e))
        content.append("</div>")  # end `word`
        for i2, t in enumerate(translations[entity]):
            if i2 > 0:
                content.append("<br>")
            content.append("<div class=\"part-of-speech\">")
            part = t['part']
            if part is not None:
                content.append(
                    "<p class=\"part-name\">[{part}]</p>".format(part=part))
            content.append("<ol>")
            for m in t['meanings_list']:
                content.append("<div class=\"meaning\">")
                content.append("<strong><li>{meaning}</li></strong>".format(
                    meaning=', '.join(m['meaning'])))
                content.append("<div class=\"examples\">")
                for e in m['examples']:
                    content.append("<p>{example}</p>".format(example=e))
                content.append("</div>")  # end `examples`
                content.append("</div>")  # end `meaning`
            content.append("</ol>")
            content.append("</div>")  # end `part-of-speech`
        content.append("</div>")  # end `translation`
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
    content = ['<h1>Index</h1>', '<ul>']
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
