import configparser
import logging
import re
import shutil

from bs4 import BeautifulSoup
from collections import OrderedDict
from itertools import zip_longest
from pathlib import Path

from .templates import CONFIG_TEMPLATE, HTML_TEMPLATE

logger = logging.getLogger(__name__)


class WordNotFound(Exception):
    pass


class Config:
    def __init__(self, config_file, data_dir):
        self.config_file = Path(config_file)
        self.default_config = {
            'data dir': data_dir,
            'prefix': 'none',
            'linewrap': '78',
            'colors': 'yes',
            'web browser': 'default'
        }
        self.config = configparser.ConfigParser(defaults=self.default_config,
                                                default_section='dikicli')

    def __getitem__(self, key):
        return self.config['dikicli'][key]

    def __setitem__(self, key, value):
        self.config['dikicli'][key] = value

    def read_config(self):
        """
        Read config from a file.

        Invalid config values will be discarded and defaults used
        in their place.
        """
        _config = self.config['dikicli']
        if self.config_file.is_file():
            logger.debug("Reading config file: %s", self.config_file.as_posix())
            with open(self.config_file, mode='r') as f:
                self.config.read_file(f)

            p = _config.get('prefix')
            if p.lower() not in ['-', '+', '*', 'none']:
                logger.warning("Config: Invalid prefix value. Using default.")
                _config['prefix'] = self.default_config['prefix']
            if p == 'none':
                _config['prefix'] = ''

            w = _config.get('linewrap')
            try:
                w = int(w)
                if w < 0:
                    raise ValueError()
            except ValueError:
                logger.warning("Config: Invalid linewrap value. Using default.")
                _config['linewrap'] = self.default_config['linewrap']

            c = _config.get('colors')
            if c.lower() not in ['yes', 'no', 'true', 'false']:
                logger.warning("Config: Invalid colors value. Using default.")
                _config['colors'] = self.default_config['colors']

    def create_default_config(self):
        """
        Write default config file to disk.

        Backs up existing configuration file.

        :returns: string path to config file
        """
        filename = self.config_file.as_posix()
        logger.info("Creating default config file: %s", filename)
        config_dir = self.config_file.parent
        if not config_dir.exists():
            config_dir.mkdir(parents=True)
        if self.config_file.is_file():
            backup = filename + '.old'
            logger.info("Saving config file backup at: %s", backup)
            shutil.copy(filename, backup)
        with open(self.config_file, mode='w') as f:
            config_string = CONFIG_TEMPLATE.format(
                data_dir=self.default_config['data dir'],
                prefix=self.default_config['prefix'],
                linewrap=self.default_config['linewrap'],
                colors=self.default_config['colors'],
                browser=self.default_config['web browser'],
            )
            f.write(config_string)
        return filename


def parse(html_dump, native=False):
    """
    Parse html string

    :html_dump: string containg html
    :native: whether to translate from native to foreign language

    :returns: translations dictionary
    :raises: WordNotFound
    """
    soup = BeautifulSoup(html_dump, 'html.parser')
    trans_dict = OrderedDict()
    for entity in soup.select('div.diki-results-left-column > div > div.dictionaryEntity'):
        if not native:
            meanings = entity.select('ol.foreignToNativeMeanings')
        else:
            meanings = entity.select('ol.nativeToForeignEntrySlices')
        if not meanings:
            continue
        word = tuple(e.get_text().strip() for e in entity.select('h1 > span.hw'))
        parts = [p.get_text().strip() for p in entity.select('span.partOfSpeech')]
        trans_list = []
        for p, m in zip_longest(parts, meanings):
            t = dict()
            t['part'] = p
            t['meanings_list'] = []
            for i in m.find_all('li', recursive=False):
                v = dict()
                v['examples'] = []
                if not native:
                    v['meaning'] = [m.get_text().strip() for m in i.select('span.hw')]
                    pattern = re.compile('\s{3,}')
                    for e in i.find_all('div', class_='exampleSentence'):
                        example = re.split(pattern, e.get_text().strip())
                        v['examples'].append(example)
                else:
                    v['meaning'] = [i.find('span', recursive=False).get_text().strip()]
                    # When translating to polish 'examples' are just synonyms of translation
                    synonyms = ', '.join(sorted(set(x.get_text().strip()
                                                    for x in i.select('ul > li > span.hw'))))
                    if synonyms:
                        v['examples'].append([synonyms, ''])
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
                m['meaning'] = [mn.get_text() for mn in meaning.select('li > span')]
                m['examples'] = []
                for e in meaning.find_all('p'):
                    m['examples'].append([ex.get_text() for ex in e.find_all('span')])
                t['meanings_list'].append(m)
            trans_list.append(t)
        trans_dict[word] = trans_list
    return trans_dict


def cache_lookup(word, data_dir, native=False):
    """
    Checks if word is in cache.

    :word: word to check in cache
    :data_dir: pathlib.Path cache directory location

    :returns: translation of word or None
    """
    trans_dir = 'translations'
    if native:
        trans_dir += '_native'
    logger.debug("Cache lookup: %s", word)
    filename = data_dir.joinpath(trans_dir, '{}.html'.format(word))
    if filename.is_file():
        with open(filename, mode='r') as f:
            logger.debug("Cache found: %s", word)
            translation = parse_cached(f.read())
            return translation
    logger.debug("Cache miss: %s", word)


def get_words(words_file, prefix):
    """
    Get list of words matching prefix from history file.

    If prefix is empty string returns all words.

    :words_file: pathlib.Path location of history file
    :prefix: prefix sign to use when matching words

    :returns: list of words
    """
    word_list = []
    if not words_file.is_file():
        return word_list
    with open(words_file, mode='r') as f:
        for l in f:
            line = l.rstrip()
            if line[0] in ['-', '+', '*']:
                word_list.append([line[0], line[1:]])
            else:
                word_list.append(['', line])
    return [w[1] for w in word_list if prefix in ['', w[0]]]


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


def write_html_file(word, translations, data_dir, native=False):
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
                content.append("<p class=\"part-name\">[{part}]</p>".format(part=part))
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
                    content.append("<p><span>{ex}</span><br><span>{tr}</span></p>"
                                   "".format(ex=e[0], tr=e[1]))
                content.append("</div>")  # end `examples`
                content.append("</div>")  # end `meaning`
            content.append("</ol>")
            content.append("</div>")  # end `part-of-speech`
        content.append("</div>")  # end `translation`
    content_str = '\n'.join(content)

    # create translations dir if needed
    trans_dir = 'translations'
    if native:
        trans_dir += '_native'
    translations_dir = data_dir.joinpath(trans_dir)
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
        prefix = ''
    filename = data_dir.joinpath('{name}.html'.format(name=name))

    content = ['<h1>{}</h1>'.format(name.capitalize()), '<ul>']
    word_list = get_words(data_dir.joinpath('words.txt'), prefix)
    for word in word_list:
        if data_dir.joinpath('translations/{}.html'.format(word)).is_file():
            link = '<li><a href="translations/{word}.html">{word}</a></li>'.format(word=word)
            content.append(link)
    content.append('</ul>')
    if not word_list:
        content.append('<i>Nothing to see here ...yet!</i>')
    content_str = '\n'.join(content)

    with open(filename, mode='w') as f:
        result = HTML_TEMPLATE.replace('{% word %}', name.capitalize())
        result = result.replace('{% content %}', content_str)
        logger.info("Updating %s.html", name)
        f.write(result)
    return filename
