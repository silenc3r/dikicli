# -*- coding: utf-8 -*-

import configparser
import json
import logging
import os
import pathlib
import re
import shutil
import sys
import urllib
import webbrowser
from collections import namedtuple
from itertools import zip_longest
from pathlib import Path
from urllib.request import Request, urlopen
import urllib.parse

from bs4 import BeautifulSoup

import dikicli.parsers
from dikicli.helpers import flatten, flatten_compat
from dikicli.templates import CONFIG_TEMPLATE
from dikicli.templates import HTML_TEMPLATE

# HTML output types
ContentSuccess = namedtuple("ContentSuccess", "html")
ContentNotFound = namedtuple("ContentNotFound", "html")

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


class ParseError(Exception):
    pass

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


def lookup_online(word: str) -> str:
    word = urllib.parse.quote(word)
    URL = "https://www.diki.pl/" + word
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; "
            "Trident/7.0;  rv:11.0) like Gecko"
        )
    }

    request = Request(URL, headers=HEADERS)
    try:
        response = urlopen(request)
        content = response.read().decode("utf-8")
        return content
    except urllib.error.HTTPError as e:
        if e.code == 404:
            content = e.read().decode("utf-8")
            return content
        raise e


def _parse_html(html_dump, pl_to_en=False):
    """Parse html string.

    Parameters
    ----------
    html_dump : str
        HTML content.
    pl_to_en : bool, optional
        Whether to translate from native to foreign language.

    Returns
    -------
    translations : list
        Translations list.

    Raises
    -----   -
    WordNotFound
        If word can't be found.
    """
    # pylint: disable=too-many-locals

    soup = BeautifulSoup(html_dump, "html.parser")
    translations = []
    dikiContainer = soup.find("div", class_="dikiContainer")
    for entity in dikiContainer.select(
        "div.diki-results-left-column > div > div.dictionaryEntity"
    ):
        if not pl_to_en:
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
                if not pl_to_en:
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
    not_found = dikiContainer.p.img.find(string=True, recursive=False).strip()
    suggestions = dikiContainer.div.b
    if suggestions:
        raise WordNotFound(f"{not_found}\n{suggestions.get_text().strip()}")
    raise WordNotFound(not_found)


def parse_en_pl(html_dump):
    """Parse html string."""

    soup = BeautifulSoup(html_dump, "html.parser")
    result = []
    dikiContainer = soup.find("div", class_="dikiContainer")

    # word not found
    if not dikiContainer.find("div", class_="diki-results-container", recursive=False):
        err_msg = dikiContainer.p.img.find(string=True, recursive=False).strip()
        suggestions = dikiContainer.div.b
        if suggestions:
            err_msg += "\n" + suggestions.get_text().strip()
        raise WordNotFound(err_msg)

    id_en_pl = dikiContainer.find_all("div", id="en-pl")
    if len(id_en_pl) > 1:
        raise ParseError("Didn't expect multiple divs with 'en-pl' tag")

    # word found, moving to 'diki-results-container'
    en_pl_parent = id_en_pl[0].parent
    _newline = en_pl_parent.next_sibling
    # first sibling should be newline
    if _newline.get_text() != "\n":
        raise ParseError("Expected newline")

    # second sibling should contain our results
    resultsContainer = _newline.next_sibling
    if not (resultsContainer.has_attr('class')
            and resultsContainer.get('class') == ['diki-results-container']):
        raise ParseError("Expected 'diki-results-container'")

    left_column = resultsContainer.find("div", class_="diki-results-left-column").find("div")
    entities = left_column.find_all("div", class_="dictionaryEntity")

    for ent in entities:
        entry = {}
        variants = ent.find("div", class_="hws").find_all("span", class_="hw")
        entry["Entry"] = [v.get_text().strip() for v in variants]
        entry["PartsOfSpeech"] = []
        pos_nodes = ent.find_all("div", class_="partOfSpeechSectionHeader")
        parts = (p.get_text().strip().replace("\xa0", " ") for p in pos_nodes)
        meaning_nodes = ent.find_all("ol", class_="foreignToNativeMeanings", recursive=False)

        if len(pos_nodes) == 0 and len(meaning_nodes) > 1:
            raise ParseError("Found 0 partOfSpeech and many foreignToNativeMeanings")

        for pos, mean in zip_longest(parts, meaning_nodes, fillvalue=""):
            mean_list = []
            for elem in mean.find_all("li", recursive=False):
                # this needs to be recursive because profanity words are contained in additional span
                meaning = [m.get_text().strip() for m in elem.find_all("span", class_="hw", recursive=True)]
                if not meaning:
                    raise ParseError("Meaning is empty")
                sentences = []
                # recursive because of profanity words
                for ex_node in elem.find_all("div", class_="exampleSentence", recursive=True):
                    sentence = {}
                    stc = ""
                    for s in ex_node.find_all(string=True, recursive=False):
                        stc = s.strip()
                        if stc:
                            break
                    if not stc:
                        raise ParseError("Example sentence is empty")
                    sentence["Sentence"] = stc
                    sentence["Translation"] = ex_node.find("span", class_="exampleSentenceTranslation").get_text().strip()
                    if not sentence["Translation"]:
                        raise ParseError("Sentence translation is empty")
                    sentences.append(sentence)
                mean_list.append({"Meaning": meaning, "ExampleSentences": sentences})
            entry["PartsOfSpeech"].append({"Part": pos, "Meanings": mean_list})

        result.append(entry)

    return result


def _cache_lookup(word, data_dir, pl_to_en=False):
    """Checks if word is in cache.

    Parameters
    ----------
    word : str
        Word to check in cache.
    data_dir : pathlib.Path
        Cache directory location.

    Returns
    -------
    translation : List[str] or None
        Translation of given word.
    """
    trans_dir = "translations"
    if pl_to_en:
        trans_dir += "_native"
    logger.debug("Cache lookup: %s", word)
    filename = data_dir.joinpath(trans_dir, "{}.html".format(word))
    if filename.is_file():
        with open(filename, mode="r") as f:
            logger.debug("Cache found: %s", word)
            translation = dikicli.parsers.parse_cached(f.read())
            return translation
    logger.debug("Cache miss: %s", word)
    return None


def _get_words(data_dir):
    """Return list of translated words."""
    trans_dir = data_dir / "translations"
    return [p.stem for p in sorted(pathlib.Path(trans_dir).iterdir(), key=os.path.getmtime)]


def get_word_list(cache_dir):
    """Return list of translated words."""
    return [p.stem for p in sorted(pathlib.Path(cache_dir).iterdir(), key=os.path.getmtime)]


def cache_lookup(word, cache_dir):
    """Check cache for given word.

    Args:
        word (str): Word to look up.
        cache_dir (pathlib.Path): Path to cache directory.

    Returns:
        dict or None: Translation structure or None.

    """
    logger.debug("Cache lookup: %s in cache_dir: %s", word, cache_dir.as_posix())
    filename = cache_dir / f"{word}.json"
    if filename.is_file():
        with open(filename) as f:
            logger.debug("Cache hit: %s", word)
            return json.load(f)

    logger.debug("Cache miss: %s", word)

def cache_store(word, translations, cache_dir):
    """Create json file with translations of the word.

    If `cache_dir` doesn't exist it will be created.

    Args:
        word (str)               : Word that was translated
        translations (dict)      : Translations structure
        cache_dir (pathlib.Path) : Path to cache directory
    """
    if not cache_dir.exists():
        logger.debug("Creating cache directory %s", cache_dir.as_posix())
        cache_dir.mkdir(parents=True)

    logger.debug("Saving %s to cache dir %s", word, cache_dir.as_posix())
    with open(cache_dir / f"{word}.json", mode="w") as f:
        json.dump(translations, f, indent=4, ensure_ascii=False)


def create_index_content(words):
    """Create HTML string of index file.

    Args:
        words (list): List of cached words.

    Returns:
        str: HTML string.
    """
    content = ["<h1>Index</h1>", "<ul>"]
    button = '<a href="random_word"><button type="button">Random word</button></a>'
    content.append(button)
    content.append('<hr>')
    for word in words:
        content.append(
            '<li><a href="words/{word}">{word}</a></li>'.format(word=word)
        )

    content.append("</ul>")
    if not words:
        content.append("<i>Nothing to see here ...yet!</i>")

    return "\n".join(content)


def generate_index_html(cache_dir):
    """Generates an HTML index page listing cached translations.

    This function retrieves a list of cached words from the specified cache
    directory and generates an HTML page displaying the available translations.

    Args:
        cache_dir (pathlib.Path): The path to the directory containing cached
        translation files.

    Returns:
        str: An HTML string representing the index page of cached translations.
    """
    cached_words = get_word_list(cache_dir)
    content_str = create_index_content(cached_words)
    html_string = HTML_TEMPLATE.replace("{% word %}", "Index")
    html_string = html_string.replace("{% content %}", content_str)
    return html_string


def generate_word_page(word, cache_dir):
    """Generates an HTML page for a given word using cached translations.

    This function retrieves the translation data for the specified word from
    the cache directory. If the word is found, it processes the translations
    and generates an HTML page. If the word is not in the cache, the function
    returns `None`.

    Args:
        word (str): The word to generate the page for.
        cache_dir (pathlib.Path): The directory where cached translation data
        is stored.

    Returns:
        str | None: The generated HTML page as a string if the word is found in the
        cache, otherwise `None`.
    """
    trans_dict = cache_lookup(word, cache_dir)
    if trans_dict is None:
        return None

    translations = flatten_compat(trans_dict)
    content_str = dikicli.parsers.generate_word_page(translations)
    html_string = HTML_TEMPLATE.replace("{% word %}", word)
    html_string = html_string.replace("{% content %}", content_str)
    return html_string


def translate(word, data_dir, use_cache=True, pl_to_en=False):
    """Translate a word.

    Parameters
    ----------
    word : str
        Word to translate.
    data_dir : Path
        Data directory path.
    use_cache : bool, optional
        Wheter to use cache.
    pl_to_en : bool, optional
        Translate from Polish to English.

    Returns
    -------
    translation
        Translation of a word.
    """
    translation = None

    if use_cache:
        logger.debug("Checking cache: %s", word)
        translation = _cache_lookup(word, data_dir, pl_to_en=pl_to_en)

    if translation:
        return translation

    content = lookup_online(word)
    if pl_to_en:
        # FIXME: it is totally broken
        translation = flatten(_parse_html(content, pl_to_en))
        # TODO: write file
    else:
        # translation = dikicli.parsers.parse_en_pl(content)
        translation = flatten_compat(parse_en_pl(content))
        # _write_html_file(word, translation, data_dir, pl_to_en=pl_to_en)
        # _write_index_file(data_dir)

    return translation


def get_stats(data_dir: Path):
    """Get usage statistics.
    Returns (num_of_en_words, num_of_pl_words) tuple.
    """
    en_dir = data_dir.joinpath("translations")
    pl_dir = data_dir.joinpath("translations_native")

    def count_words(dir):
        return len(list(dir.glob("*.html"))) if dir.is_dir() else 0

    num_of_en_words = count_words(en_dir)
    num_of_pl_words = count_words(pl_dir)
    return num_of_en_words, num_of_pl_words


def wrap_text(translations, linewrap=0):
    """Pretty print translations.

    If lienwrap is set to 0 disable line wrapping.

    Returns list of wrapped lines.
    """
    # TODO: move this to top after cleaning up old parser
    from dikicli.parsers import Entity, Meaning, PartOfSpeech, Sentence, Info

    def wrap(text, width=linewrap, findent=0, sindent=0, bold=False):
        if width == 0:
            text = " " * findent + text
        else:
            import textwrap

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

    result = []
    meaning_idx = 0
    for i, x in enumerate(translations):
        if isinstance(x, Entity):
            meaning_idx = 1
            if i > 0 and not isinstance(translations[i - 1], Entity):
                result.append("")
            result.append(wrap(x.val, bold=True))
        elif isinstance(x, PartOfSpeech):
            meaning_idx = 1
            if i > 0 and not isinstance(translations[i - 1], Entity):
                result.append("")
            result.append(f"[{x.val}]")
        elif isinstance(x, Meaning):
            if i > 0 and isinstance(translations[i - 1], Sentence):
                result.append("")
            result.append(wrap(f"{meaning_idx:>3}. {x.val}", sindent=5, bold=True))
            meaning_idx += 1
        elif isinstance(x, Sentence):
            result.append("")
            s1 = wrap(x.val[0], findent=6, sindent=6)
            s2 = wrap(x.val[1], findent=6, sindent=7)
            result.append(s1)
            result.append(s2)
        elif isinstance(x, Info):
            result.append(x.val)
        else:
            raise TypeError("wrap_text: unexpected translation type: %s" % type(x))

    return result


def wrap_text_new(trans_dict, width=0):
    """Pretty print translations with line wrapping.

    When width is 0 thre's no linewrapping performed.

    Args:
        trans_dict (dict): Translation data structure.
        width (int): Line width.

    Returns:
        result (list): List of formatted lines.

    """
    is_tty = sys.stdout.isatty()

    import textwrap

    def wrap(text, initial_indent=0, subsequent_indent=0, bold=False):
        ii = " " * initial_indent
        si = " " * subsequent_indent
        if width == 0:
            text = ii + text
        else:
            text = textwrap.fill(text, width, initial_indent=ii, subsequent_indent=si)

        # don't use bold when stdout is pipe or redirect
        if bold and is_tty:
            text = "\033[0;1m" + text + "\033[0m"

        return text

    result = []

    for entry in trans_dict:
        for e in entry["Entry"]:
            result.append(wrap(e, bold=True))
        for pos in entry["PartsOfSpeech"]:
            if pos["Part"]:
                part = f"[{pos['Part']}]"
                result.append(wrap(part))
            for i, meaning in enumerate(pos["Meanings"], start=1):
                mean = f"{i:>3}. {', '.join(meaning['Meaning'])}"
                result.append(wrap(mean, 0, 5, True))
                result.append("")

                if meaning["ExampleSentences"]:
                    for ex in meaning["ExampleSentences"]:
                        result.append(wrap(ex["Sentence"], 6, 6))
                        result.append(wrap(ex["Translation"], 6, 6))
                        result.append("")

    return result
