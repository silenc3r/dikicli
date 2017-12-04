import configparser
import logging
import re

from bs4 import BeautifulSoup
from collections import OrderedDict
from itertools import zip_longest

from . import DATA_DIR
from .templates import CONFIG_TEMPLATE, HTML_TEMPLATE


logger = logging.getLogger(__name__)


class WordNotFound(Exception):
    pass


def get_config(config_file):
    """
    Read config from a file.

    If configuration file doesn't exist create one with default values.
    Invalid config values will be discarded and defaults used in their place.

    :config_file: pathlib.Path to configuration file
    :returns: config
    """
    default_config = {
        'data dir': DATA_DIR,
        'prefix': '-',
        'linewrap': '78',
        'colors': 'yes',
        'web browser': 'default'
    }
    config = configparser.ConfigParser(defaults=default_config,
                                       default_section='dikicli')
    if config_file.is_file():
        logger.debug("Reading config file: %s", config_file.as_posix())
        with open(config_file, mode='rt') as f:
            config.read_file(f)

        p = config['dikicli'].get('prefix')
        if p not in ['-', '+', '*', 'none']:
            logger.warning("Config: Invalid prefix value. Using default.")
            config['dikicli']['prefix'] = default_config['prefix']
        if p == 'none':
            config['dikicli']['prefix'] = ''

        w = config['dikicli'].get('linewrap')
        try:
            w = int(w)
            if w < 0:
                raise ValueError()
        except ValueError:
            logger.warning("Config: Invalid linewrap value. Using default.")
            config['dikicli']['linewrap'] = default_config['linewrap']

        c = config['dikicli'].get('colors')
        if c not in ['yes', 'no', 'true', 'false']:
            logger.warning("Config: Invalid colors value. Using default.")
            config['dikicli']['colors'] = default_config['colors']

        return config

    # create default config file if it doesn't exist
    logger.info("Creating default config file: %s", config_file.as_posix())
    config_dir = config_file.parent
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    with open(config_file, mode='w') as f:
        config_string = CONFIG_TEMPLATE.format(
            data_dir=config['dikicli'].get('data dir'),
            prefix=config['dikicli'].get('prefix'),
            linewrap=config['dikicli'].get('linewrap'),
            colors=config['dikicli'].get('colors'),
            browser=config['dikicli'].get('web browser'),
        )
        f.write(config_string)
    return config


def parse(html_dump):
    """
    Parse html string

    :html_dump: string containg html

    :returns: translations dictionary
    :raises: WordNotFound
    """
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
                v['meaning'] = [m.get_text().strip()
                                for m in i.select('span.hw')]
                v['examples'] = []
                for e in i.find_all('div', class_='exampleSentence'):
                    pattern = re.compile('\s{3,}')
                    example = tuple(re.split(pattern, e.get_text().strip()))
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
    """
    Parse html string from cached html files.

    :html_dump: string containg html

    :returns: translations dictionary
    """
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
                m['meaning'] = [mn.get_text()
                                for mn in meaning.select('li > span')]
                m['examples'] = []
                for e in meaning.find_all('p'):
                    m['examples'].append(
                        tuple(ex.get_text() for ex in e.find_all('span')))
                t['meanings_list'].append(m)
            trans_list.append(t)
        trans_dict[word] = trans_list
    return trans_dict


def cache_lookup(word, data_dir):
    """
    Checks if word is in cache.

    :word: word to check in cache
    :data_dir: pathlib.Path cache directory location

    :returns: translation of word or None
    """
    logger.debug("Cache lookup: %s", word)
    filename = data_dir.joinpath('translations/{}.html'.format(word))
    if filename.is_file():
        with open(filename, mode='r') as f:
            logger.debug("Cache found: %s", word)
            translation = parse_cached(f.read())
            return translation
    logger.debug("Cache miss: %s", word)
    return None


def get_words(words_file, prefix):
    """
    Get list of words from history file stripped of prefix.

    :words_file: pathlib.Path location of history file
    :prefix: word prefix

    :returns: list of words
    """
    if not words_file.is_file():
        return []
    with open(words_file, mode='r') as f:
        if len(prefix) == 0:
            return [l.rstrip() for l in f]
        if prefix == 'any':
            return [l.rstrip()[1:] for l in f]
        return [l.rstrip()[1:] for l in f if l[0] == prefix]


def save_to_history(word, prefix, data_dir):
    """
    Write word to history file with chosen prefix.

    :word: word to save to history
    :prefix: word prefix
    :data_dir: pathlib.Path location of history file parent directory
    """
    words_file = data_dir.joinpath('words.txt')
    if word not in get_words(words_file, prefix):
        with open(words_file, mode='a+') as f:
            logger.debug("Adding to history: %s", word)
            f.write(prefix + word + '\n')


def write_html_file(word, translations, data_dir):
    """
    Create html file of word translations.

    :word: word that was translated
    :tralnslations: dictionary of word translations
    :data_dir: pathlib.Path location where html files are saved
    """
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
                    "<p class=\"part-name\">[{part}]</p>".format(part=part)
                )
            content.append("<ol>")
            for m in t['meanings_list']:
                content.append("<div class=\"meaning\">")
                mng = ["<strong><li>"]
                for i3, mn in enumerate(m['meaning']):
                    if i3 > 0:
                        mng.append(", ")
                    mng.append("<span>{meaning}</span>".format(meaning=mn))
                mng.append("</li></strong>")
                content.append(''.join(mng))
                content.append("<div class=\"examples\">")
                for e in m['examples']:
                    content.append(
                        "<p><span>{ex}</span><br><span>{tr}</span></p>"
                        "".format(ex=e[0], tr=e[1])
                    )
                content.append("</div>")  # end `examples`
                content.append("</div>")  # end `meaning`
            content.append("</ol>")
            content.append("</div>")  # end `part-of-speech`
        content.append("</div>")  # end `translation`
    content_str = '\n'.join(content)

    # create translations dir if needed
    translations_dir = data_dir.joinpath('translations')
    if not translations_dir.exists():
        logger.info("Creating directory: %s", translations_dir)
        translations_dir.mkdir()

    # create html file
    fname = translations_dir.joinpath('{word}.html'.format(word=word))
    with open(fname, mode='w') as f:
        logger.info("Creating html file: %s", fname)
        result = HTML_TEMPLATE.replace('{% word %}', word)
        result = result.replace('{% content %}', content_str)
        f.write(result)


def write_index_file(prefix, data_dir, full=False):
    """
    Create index file of cached translations.

    If full is set to false include all files, even when prefix doesn't match.

    :prefix: word prefix
    :data_dir: pathlib.Path cache directory location
    :full: whether to ignore prefix or not
    """
    name = 'index'
    if full:
        name = 'index-full'
        prefix = 'any' if len(prefix) > 0 else prefix

    content = ['<h1>{}</h1>'.format(name.capitalize()), '<ul>']
    word_list = get_words(data_dir.joinpath('words.txt'), prefix)
    for word in word_list:
        if data_dir.joinpath('translations/{}.html'.format(word)).is_file():
            content.append(('<li><a href="translations/{word}.html">'
                            '{word}</a></li>').format(word=word))
    content.append('</ul>')
    if not word_list:
        content.append('<i>Nothing to see here ...yet!</i>')
    content_str = '\n'.join(content)

    with open(data_dir.joinpath('{}.html'.format(name)), mode='w') as f:
        result = HTML_TEMPLATE.replace('{% word %}', name.capitalize())
        result = result.replace('{% content %}', content_str)
        logger.info("Updating %s.html", name)
        f.write(result)
