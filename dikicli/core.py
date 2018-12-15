import configparser
import html
import logging
import os
import re
import shutil
import sys
import textwrap
import urllib.parse
import urllib.request
import webbrowser
from collections import namedtuple
from itertools import zip_longest
from pathlib import Path

from bs4 import BeautifulSoup

from .templates import CONFIG_TEMPLATE
from .templates import HTML_TEMPLATE

__version__ = "0.3"

Meaning = namedtuple("Meaning", ["meaning", "examples"])
PartOfSpeech = namedtuple("PartOfSpeech", ["part", "meanings"])
Translation = namedtuple("Translation", ["word", "parts_of_speech"])

XDG_DATA_HOME = os.environ.get("XDG_DATA_HOME", "~/.local/share")
XDG_CACHE_HOME = os.environ.get("XDG_CACHE_HOME", "~/.cache")
XDG_CONFIG_HOME = os.environ.get("XDG_CONFIG_HOME", "~/.config")

DATA_DIR = Path(
    os.environ.get("DIKI_DATA_DIR", os.path.join(XDG_DATA_HOME, "dikicli"))
).expanduser()
CACHE_DIR = Path(
    os.environ.get("DIKI_CACHE_DIR", os.path.join(XDG_CACHE_HOME, "dikicli"))
).expanduser()
CONFIG_FILE = Path(
    os.environ.get(
        "DIKI_CONFIG_FILE", os.path.join(XDG_CONFIG_HOME, "dikicli", "diki.conf")
    )
).expanduser()

DEBUG = os.environ.get("DIKI_DEBUG")

logger = logging.getLogger(__name__)


class WordNotFound(Exception):
    pass


class Config:
    def __init__(self):
        self.config_file = CONFIG_FILE
        self.default_config = {
            "data dir": DATA_DIR.as_posix(),
            "linewrap": "78",
            "colors": "yes",
            "web browser": "default",
        }
        self.config = configparser.ConfigParser(
            defaults=self.default_config, default_section="dikicli"
        )

    def __getitem__(self, key):
        return self.config["dikicli"][key]

    def __setitem__(self, key, value):
        self.config["dikicli"][key] = value

    def read_config(self):
        """
        Read config from a file.

        Invalid config values will be discarded and defaults used
        in their place.
        """
        _config = self.config["dikicli"]
        # TODO: what if file doesn't exist?
        if self.config_file.is_file():
            logger.debug("Reading config file: %s", self.config_file.as_posix())
            with open(self.config_file, mode="r") as f:
                self.config.read_file(f)

            # DIKI_DATA_DIR should always take precedence if it's set
            if "DIKI_DATA_DIR" in os.environ:
                _config["data dir"] = DATA_DIR.as_posix()

            w = _config.get("linewrap")
            try:
                w = int(w)
                if w < 0:
                    raise ValueError()
            except ValueError:
                logger.warning("Config: Invalid linewrap value. Using default.")
                _config["linewrap"] = self.default_config["linewrap"]

            c = _config.get("colors")
            if c.lower() not in ["yes", "no", "true", "false"]:
                logger.warning("Config: Invalid colors value. Using default.")
                _config["colors"] = self.default_config["colors"]

    def create_default_config(self):
        """Write default config file to disk.

        Backs up existing configuration file.

        Returns
        -------
        filename : string
            Path to config file.
        """
        filename = self.config_file.as_posix()
        logger.info("Creating default config file: %s", filename)
        config_dir = self.config_file.parent
        if not config_dir.exists():
            config_dir.mkdir(parents=True)
        if self.config_file.is_file():
            backup = filename + ".old"
            logger.info("Saving config file backup at: %s", backup)
            shutil.copy(filename, backup)
        with open(self.config_file, mode="w") as f:
            config_string = CONFIG_TEMPLATE.format(
                data_dir=self.default_config["data dir"],
                linewrap=self.default_config["linewrap"],
                colors=self.default_config["colors"],
                browser=self.default_config["web browser"],
            )
            f.write(config_string)
        return filename


def _parse_html(html_dump, native=False):
    """Parse html string.

    Parameters
    ----------
    html_dump : str
        HTML content.
    native : bool, optional
        Whether to translate from native to foreign language.

    Returns
    -------
    translations : list
        Translations list.

    Raises
    ------
    WordNotFound
        If word can't be found.
    """
    # pylint: disable=too-many-locals

    soup = BeautifulSoup(html_dump, "html.parser")
    translations = []
    for entity in soup.select(
        "div.diki-results-left-column > div > div.dictionaryEntity"
    ):
        if not native:
            meanings = entity.select("ol.foreignToNativeMeanings")
        else:
            meanings = entity.select("ol.nativeToForeignEntrySlices")
        if not meanings:
            # this can happen when word exists in both polish and english, e.g. 'pet'
            continue
        word = tuple(e.get_text().strip() for e in entity.select("div.hws h1 span.hw"))
        parts = [p.get_text().strip() for p in entity.select("span.partOfSpeech")]
        parts_list = []
        for part, m in zip_longest(parts, meanings):
            meanings = []
            for elem in m.find_all("li", recursive=False):
                examples = []
                if not native:
                    meaning = [m.get_text().strip() for m in elem.select("span.hw")]
                    pattern = re.compile(r"\s{3,}")
                    for e in elem.find_all("div", class_="exampleSentence"):
                        example = re.split(pattern, e.get_text().strip())
                        examples.append(example)
                else:
                    meaning = [elem.find("span", recursive=False).get_text().strip()]
                    # When translating to polish 'examples' are just synonyms of translation
                    synonyms = ", ".join(
                        sorted(
                            set(
                                x.get_text().strip()
                                for x in elem.select("ul > li > span.hw")
                            )
                        )
                    )
                    if synonyms:
                        examples.append([synonyms, None])
                meanings.append(Meaning(meaning, examples))
            parts_list.append(PartOfSpeech(part, meanings))
        translations.append(Translation(word, parts_list))
    if translations:
        return translations
    # if translation wasn't found check if there are any suggestions
    suggestions = soup.find("div", class_="dictionarySuggestions")
    if suggestions:
        raise WordNotFound(suggestions.get_text().strip())
    raise WordNotFound("Nie znaleziono tłumaczenia wpisanej frazy")


def _parse_cached(html_dump):
    """Parse html string from cached html files.

    Parameters
    ----------
    html_dump : string
        HTML content

    Returns
    -------
    translations : list
        Translations list.
    """
    soup = BeautifulSoup(html_dump, "html.parser")
    translations = []
    for trans in soup.find_all("div", class_="translation"):
        word = tuple(t.get_text() for t in trans.select("div.word > h2"))
        trans_list = []
        for part in trans.find_all("div", class_="part-of-speech"):
            pn = part.find("p", class_="part-name")
            if pn:
                pn = pn.get_text().strip("[]")
            meanings = []
            for meaning in part.find_all("div", class_="meaning"):
                m = [mn.get_text() for mn in meaning.select("li > span")]
                examples = []
                for e in meaning.find_all("p"):
                    examples.append([ex.get_text() for ex in e.find_all("span")])
                meanings.append(Meaning(m, examples))
            trans_list.append(PartOfSpeech(pn, meanings))
        translations.append(Translation(word, trans_list))
    return translations


def _cache_lookup(word, data_dir, native=False):
    """Checks if word is in cache.

    Parameters
    ----------
    word : str
        Word to check in cache.
    data_dir : pathlib.Path
        Cache directory location.

    Returns
    -------
    translation : str or None
        Translation of given word.
    """
    trans_dir = "translations"
    if native:
        trans_dir += "_native"
    logger.debug("Cache lookup: %s", word)
    filename = data_dir.joinpath(trans_dir, "{}.html".format(word))
    if filename.is_file():
        with open(filename, mode="r") as f:
            logger.debug("Cache found: %s", word)
            # TODO: not sure if we should parse data here
            translation = _parse_cached(f.read())
            return translation
    logger.debug("Cache miss: %s", word)
    return None


def _get_words(data_dir):
    """Get list of words from history file.

    Parameters
    ----------
    data_dir : pathlib.Path
        Directory where data is saved.

    Returns
    -------
    word_list : list of str
        List of words.
    """
    words_file = data_dir.joinpath("words.txt")
    word_list = []
    if not words_file.is_file():
        return word_list
    with open(words_file, mode="r") as f:
        for l in f:
            line = l.rstrip()
            word_list.append(line)
    return word_list


def _save_to_history(word, data_dir):
    """Write word to history file.

    Parameters
    ----------
    word : str
        Word to save to history.
    data_dir : pathlib.Path
        Directory where history file should be saved.

    data_dir and it's parent directories will be created if needed.
    """
    if not data_dir.exists():
        logger.debug("Creating DATA DIR: %s", data_dir.as_posix())
        data_dir.mkdir(parents=True)
    if word not in _get_words(data_dir):
        with open(data_dir.joinpath("words.txt"), mode="a+") as f:
            logger.debug("Adding to history: %s", word)
            f.write(word + "\n")


def _create_html_file_content(translations):
    """Create html string out of translation dict.

    Parameters
    ----------
    tralnslations : dict
        Dictionary of word translations.

    Returns
    -------
    str:
        html string of translation
    """
    content = []
    for i1, t in enumerate(translations):
        if i1 > 0:
            content.append("<br>")
        content.append('<div class="translation">')
        content.append('<div class="word">')
        for w in t.word:
            content.append("<h2>{word}</h2>".format(word=w))
        content.append("</div>")  # end `word`
        for i2, t2 in enumerate(t.parts_of_speech):
            if i2 > 0:
                content.append("<br>")
            content.append('<div class="part-of-speech">')
            if t2.part is not None:
                content.append('<p class="part-name">[{part}]</p>'.format(part=t2.part))
            content.append("<ol>")
            for m in t2.meanings:
                content.append('<div class="meaning">')
                mng = ["<strong><li>"]
                for i3, mn in enumerate(m.meaning):
                    if i3 > 0:
                        mng.append(", ")
                    mng.append("<span>{meaning}</span>".format(meaning=mn))
                mng.append("</li></strong>")
                content.append("".join(mng))
                content.append('<div class="examples">')
                for e in m.examples:
                    content.append(
                        "<p><span>{ex}</span><br><span>{tr}</span></p>"
                        "".format(ex=e[0], tr=e[1])
                    )
                content.append("</div>")  # end `examples`
                content.append("</div>")  # end `meaning`
            content.append("</ol>")
            content.append("</div>")  # end `part-of-speech`
        content.append("</div>")  # end `translation`
    return "\n".join(content)


def _write_html_file(word, translations, data_dir, native=False):
    """Create html file of word translations.

    Parameters
    ----------
    word : str
        Word that was translated.
    tralnslations : dict
        Dictionary of word translations.
    data_dir : pathlib.Path
        Location where html files are saved.
    """
    content_str = _create_html_file_content(translations)
    html_string = HTML_TEMPLATE.replace("{% word %}", word)
    html_string = html_string.replace("{% content %}", content_str)

    trans_dir = "translations"
    if native:
        trans_dir += "_native"
    translations_dir = data_dir.joinpath(trans_dir)
    fname = translations_dir.joinpath("{word}.html".format(word=word))
    save_file(fname, html_string, mk_parents=True)


def _create_index_content(words):
    """Create html string of index file.

    Parameters
    ----------
    words : list of str
        List of cached words.

    Returns
    -------
    str
        html string.
    """
    content = ["<h1>Index</h1>", "<ul>"]
    for word in words:
        content.append(
            '<li><a href="translations/{word}.html">{word}</a></li>'.format(word=word)
        )

    content.append("</ul>")
    if not words:
        content.append("<i>Nothing to see here ...yet!</i>")

    return "\n".join(content)


def _write_index_file(data_dir):
    """Create index file of cached translations.

    Parameters
    ----------
    data_dir : pathlib.Path
        Cache directory location.
    """
    cached_words = [
        w
        for w in _get_words(data_dir)
        if data_dir.joinpath("translations/{}.html".format(w)).is_file()
    ]

    content_str = _create_index_content(cached_words)
    html_string = HTML_TEMPLATE.replace("{% word %}", "Index")
    html_string = html_string.replace("{% content %}", content_str)

    filename = data_dir.joinpath("index.html")
    save_file(filename, html_string, mk_parents=True)


def save_file(filename, data, mk_parents=True):
    """Save file to disk.

    Paramaters
    ----------
    filename : pathlib.Path
        Path to the file.
    data : str
        File contents.
    mk_parents : bool, optional
        If to create parent directories.
    """
    parent = filename.parent
    if not parent.exists() and mk_parents:
        logger.debug("Creating directory: %s", parent.as_posix())
        parent.mkdir(parents=True)
    with open(filename, mode="w") as f:
        logger.debug("Saving file: %s", filename.as_posix())
        f.write(data)


def _lookup_online(word):
    """Look up word on diki.pl.

    Parameters
    ----------
    word : str
        Word too look up.

    Returns
    -------
    str
        website HTML content.
    """
    URL = "https://www.diki.pl/{word}"
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; "
            "Trident/7.0;  rv:11.0) like Gecko"
        )
    }

    logger.debug("Looking up online: %s", word)
    quoted_word = urllib.parse.quote(word)
    req = urllib.request.Request(URL.format(word=quoted_word), headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        html_string = response.read().decode()

    return html.unescape(html_string)


def translate(word, config, use_cache=True, to_eng=False):
    """Translate a word.

    Parameters
    ----------
    word : str
        Word to translate.
    config : Config
        Configuration settings.
    use_cache : bool, optional
        Wheter to use cache.
    to_eng : bool, optional
        Translate from Polish to English.

    Returns
    -------
    translation
        Translation of a word.

    Raises
    ------
    WordNotFound
        If word can't be found.
    """
    translation = None
    data_dir = Path(config["data dir"])

    if use_cache:
        logger.debug("Checking cache: %s", word)
        translation = _cache_lookup(word, data_dir, native=to_eng)

    if translation:
        return translation

    html_dump = _lookup_online(word)

    try:
        translation = _parse_html(html_dump, native=to_eng)
    except WordNotFound as exn:
        logger.error(str(exn))
        raise exn

    _write_html_file(word, translation, data_dir, native=to_eng)
    if not to_eng:
        _save_to_history(word, data_dir)
        _write_index_file(data_dir)

    return translation


def display_index(config):
    """Open index in web browser.

    Parameters
    ----------
    config : Config
        Configuration settings.

    Raises
    ------
    FileNotFoundError
        If index file doesn't exist.
    """
    browser = config["web browser"].lower()
    data_dir = Path(config["data dir"])
    if browser in webbrowser._browsers:
        b = webbrowser.get(browser)
    else:
        if browser != "default":
            logger.warning(
                "Couldn't find '%s' browser. Falling back to default.", browser
            )
        b = webbrowser.get()
    index_file = data_dir.joinpath("index.html")
    if not index_file.exists():
        logger.error("File doesn't exist: %s", index_file.as_posix())
        raise FileNotFoundError("Index file doesn't exist")
    else:
        logger.info("Opening %s in '%s'", index_file.as_posix(), b.name)
        b.open(index_file.as_uri())


def wrap_text(translations, linewrap=0):
    """Pretty print translations.

    If linewrap is set to 0 disble line wrapping.

    Parameters
    ----------
    translations : list
        List of word translations.
    linewrap : int
        Maximum line length before wrapping.
    """
    # pylint: disable=too-many-locals

    def wrap(text, width=linewrap, findent=0, sindent=0, bold=False):
        if width == 0:
            text = " " * findent + text
        else:
            text = textwrap.fill(
                text,
                width=width,
                initial_indent=" " * findent,
                subsequent_indent=" " * sindent,
            )
        # don't use bold when stdout is pipe or redirect
        if bold and sys.stdout.isatty():
            text = "\033[0;1m" + text + "\033[0m"
        return text

    indent = 5
    result = []
    for i1, trans in enumerate(translations):
        if i1 > 0:
            result.append("\n")
        for w in trans.word:
            result.append(wrap(w, bold=True))
        for i2, t in enumerate(trans.parts_of_speech):
            if i2 > 0:
                result.append("")
            if t.part:
                result.append("[{part}]".format(part=t.part))
            for i3, m in enumerate(t.meanings, 1):
                if i3 > 1:
                    result.append("")
                meaning = "{index:>3}. {meanings}".format(
                    index=i3, meanings=", ".join(m.meaning)
                )
                result.append(wrap(meaning, sindent=indent, bold=True))
                eindent = indent + 1
                for e in m.examples:
                    result.append("")
                    result.append(wrap(e[0], findent=eindent, sindent=eindent))
                    if e[1]:
                        result.append(wrap(e[1], findent=eindent, sindent=eindent + 1))
    return "\n".join(result)
