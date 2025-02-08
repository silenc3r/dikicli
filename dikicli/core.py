# -*- coding: utf-8 -*-

import configparser
import json
import logging
import os
import pathlib
import shutil
import sys
import urllib
import urllib.parse
from itertools import zip_longest
from pathlib import Path
from urllib.request import Request
from urllib.request import urlopen

from bs4 import BeautifulSoup

from dikicli.templates import CONFIG_TEMPLATE
from dikicli.templates import HTML_TEMPLATE

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


def parse_en_pl(html_dump):
    """Parse html string."""

    lang = "en"
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
    if not id_en_pl:
        raise WordNotFound("Nie znaleziono dokładnego tłumaczenia wpisanej frazy.")

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
    if not (
        resultsContainer.has_attr("class")
        and resultsContainer.get("class") == ["diki-results-container"]
    ):
        raise ParseError("Expected 'diki-results-container'")

    left_column = resultsContainer.find("div", class_="diki-results-left-column").find(
        "div"
    )
    entities = left_column.find_all("div", class_="dictionaryEntity")

    for ent in entities:
        entry = {}
        variants = ent.find("div", class_="hws").find_all("span", class_="hw")
        entry["Entry"] = [v.get_text().strip() for v in variants]
        entry["Language"] = lang
        entry["PartsOfSpeech"] = []
        pos_nodes = ent.find_all("div", class_="partOfSpeechSectionHeader")
        parts = (p.get_text().strip().replace("\xa0", " ") for p in pos_nodes)
        meaning_nodes = ent.find_all(
            "ol", class_="foreignToNativeMeanings", recursive=False
        )

        if len(pos_nodes) == 0 and len(meaning_nodes) > 1:
            raise ParseError("Found 0 partOfSpeech and many foreignToNativeMeanings")

        for pos, mean in zip_longest(parts, meaning_nodes, fillvalue=""):
            mean_list = []
            for elem in mean.find_all("li", recursive=False):
                # this needs to be recursive because profanity words are contained in additional span
                meaning = [
                    m.get_text().strip()
                    for m in elem.find_all("span", class_="hw", recursive=True)
                ]
                if not meaning:
                    raise ParseError("Meaning is empty")
                sentences = []
                # recursive because of profanity words
                for ex_node in elem.find_all(
                    "div", class_="exampleSentence", recursive=True
                ):
                    sentence = {}
                    stc = ""
                    for s in ex_node.find_all(string=True, recursive=False):
                        stc = s.strip()
                        if stc:
                            break
                    if not stc:
                        raise ParseError("Example sentence is empty")
                    sentence["Sentence"] = stc
                    sentence["Translation"] = (
                        ex_node.find("span", class_="exampleSentenceTranslation")
                        .get_text()
                        .strip()
                    )
                    if not sentence["Translation"]:
                        raise ParseError("Sentence translation is empty")
                    sentences.append(sentence)
                mean_list.append({"Meaning": meaning, "ExampleSentences": sentences})
            entry["PartsOfSpeech"].append({"Part": pos, "Meanings": mean_list})

        result.append(entry)

    return result


def parse_pl_en(html_dump):
    """Parse html string."""

    lang = "pl"
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

    id_pl_en = dikiContainer.find_all("div", id="pl-en")
    if not id_pl_en:
        raise WordNotFound("Nie znaleziono dokładnego tłumaczenia wpisanej frazy.")

    if len(id_pl_en) > 1:
        raise ParseError("Didn't expect multiple divs with 'pl-en' tag")

    # word found, moving to 'diki-results-container'
    pl_en_parent = id_pl_en[0].parent
    _newline = pl_en_parent.next_sibling
    # first sibling should be newline
    if _newline.get_text() != "\n":
        raise ParseError("Expected newline")

    # second sibling should contain our results
    resultsContainer = _newline.next_sibling
    if not (
        resultsContainer.has_attr("class")
        and resultsContainer.get("class") == ["diki-results-container"]
    ):
        raise ParseError("Expected 'diki-results-container'")

    left_column = resultsContainer.find("div", class_="diki-results-left-column").find(
        "div"
    )
    entities = left_column.find_all("div", class_="dictionaryEntity")

    for ent in entities:
        entry = {}
        variants = ent.find("div", class_="hws").find_all("span", class_="hw")
        entry["Entry"] = [v.get_text().strip() for v in variants]
        entry["Language"] = lang
        entry["PartsOfSpeech"] = []
        pos_nodes = ent.find_all("div", class_="partOfSpeechSectionHeader")
        parts = (p.get_text().strip().replace("\xa0", " ") for p in pos_nodes)
        meaning_nodes = ent.find_all(
            "ol", class_="nativeToForeignEntrySlices", recursive=False
        )

        if not meaning_nodes:
            raise ParseError("Found 0 nativeToForeignEntrySlices")

        if len(pos_nodes) == 0 and len(meaning_nodes) > 1:
            raise ParseError("Found 0 partOfSpeech and many nativeToForeignEntrySlices")

        for pos, mean in zip_longest(parts, meaning_nodes, fillvalue=""):
            mean_list = []
            for elem in mean.find_all("li", recursive=False):
                # this needs to be recursive because profanity words are contained in additional span
                meaning = [
                    m.get_text().strip()
                    for m in elem.find_all("span", class_="hw", recursive=False)
                ]
                if not meaning:
                    raise ParseError("Meaning is empty")

                var_div = elem.find("ul", class_="nativeToForeignMeanings")
                variants = []
                if var_div:
                    for var in var_div.find_all("li", recursive=False):
                        vlist = var.find_all("span", class_="hw")
                        vnames = [v.get_text().strip() for v in vlist]

                        if not vnames:
                            raise ParseError("Found variant, but no meanings")

                        sentences = []
                        for ex_node in var.find_all("div", class_="exampleSentence"):
                            sentence = {}
                            stc = ""
                            for s in ex_node.find_all(string=True, recursive=False):
                                stc = s.strip()
                                if stc:
                                    break
                            if not stc:
                                raise ParseError("Example sentence is empty")
                            sentence["Sentence"] = stc
                            sentence["Translation"] = (
                                ex_node.find(
                                    "span", class_="exampleSentenceTranslation"
                                )
                                .get_text()
                                .strip()
                            )
                            if not sentence["Translation"]:
                                raise ParseError("Sentence translation is empty")
                            sentences.append(sentence)
                        variants.append(
                            {"Variant": vnames, "ExampleSentences": sentences}
                        )

                mean_list.append({"Meaning": meaning, "Variants": variants})

            entry["PartsOfSpeech"].append({"Part": pos, "Meanings": mean_list})

        result.append(entry)

    return result


def get_word_list(cache_dir):
    """Return list of translated words."""
    return [
        p.stem for p in sorted(pathlib.Path(cache_dir).iterdir(), key=os.path.getmtime)
    ]


def cache_lookup(cache_dir, word):
    """Check cache for given word.

    Args:
        word (str): Word to look up.
        cache_dir (pathlib.Path): Path to cache directory.

    Returns:
        dict | None: Translation structure or None.

    """
    logger.debug("Cache lookup: %s in cache_dir: %s", word, cache_dir.as_posix())
    filename = cache_dir / f"{word}.json"
    if filename.is_file():
        with open(filename) as f:
            logger.debug("Cache hit: %s", word)
            return json.load(f)

    logger.debug("Cache miss: %s", word)


def cache_store(cache_dir, word, translations):
    """Create json file with translations of the word.

    If `cache_dir` doesn't exist it will be created.

    Args:
        cache_dir (pathlib.Path) : Path to cache directory
        word (str)               : Word that was translated
        translations (dict)      : Translations structure
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
    content.append("<hr>")
    for word in words:
        content.append('<li><a href="words/{word}">{word}</a></li>'.format(word=word))

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


def generate_page_lines(trans_dict):
    def append(list_, tag, indent):
        indent_str = " " * indent * 4
        list_.append(f"{indent_str}{tag}")

    content = []

    for entity in trans_dict:
        append(content, '<div class="translation">', 0)
        append(content, '<div class="word">', 1)
        for word in entity["Entry"]:
            append(content, f"<h2>{word}</h2>", 2)
        append(content, "</div><!--close-word-->", 1)

        append(content, '<div class="parts-of-speech">', 1)
        for i, pos in enumerate(entity["PartsOfSpeech"]):
            if i > 0:
                append(content, "<br>", 2)
            append(content, '<div class="part">', 2)
            append(content, f'<p class="part-name">{pos["Part"]}</p>', 3)
            append(content, '<div class="meanings">', 3)
            append(content, "<ol>", 4)
            for meaning in pos["Meanings"]:
                append(content, "<li>", 5)
                append(content, '<div class="meaning">', 6)
                append(
                    content,
                    f'<p><strong><span>{", ".join(meaning["Meaning"])}</span></strong></p>',
                    7,
                )
                append(content, '<div class="examples">', 7)
                for es in meaning["ExampleSentences"]:
                    append(
                        content,
                        f'<p><span>{es["Sentence"]}</span><br><span>{es["Translation"]}</span></p>',
                        8,
                    )
                append(content, "</div><!--close-examples-->", 7)
                append(content, "</div><!--close-meaning-->", 6)
                append(content, "</li>", 5)
            append(content, "</ol>", 4)
            append(content, "</div><!--close-meanings-->", 3)
            append(content, "</div><!--close-part-->", 2)
        append(content, "</div><!--close-parts-of-speech-->", 1)
        append(content, "</div><!--close-translation-->", 0)
        append(content, "<br>", 0)

    return content


def generate_word_html(cache_dir, word):
    """Generates an HTML page for a given word using cached translations.

    This function retrieves the translation data for the specified word from
    the cache directory. If the word is found, it processes the translations
    and generates an HTML page. If the word is not in the cache, the function
    returns `None`.

    Args:
        cache_dir (pathlib.Path): The directory where cached translation data
        is stored.
        word (str): The word to generate the page for.

    Returns:
        str | None: The generated HTML page as a string if the word is found in the
        cache, otherwise `None`.
    """
    trans_dict = cache_lookup(cache_dir, word)
    if trans_dict is None:
        return None

    content_str = "\n".join(generate_page_lines(trans_dict))
    html_string = HTML_TEMPLATE.replace("{% word %}", word)
    html_string = html_string.replace("{% content %}", content_str)
    return html_string


def get_stats(cache_dir: pathlib.Path):
    """Get usage statistics.
    Returns (num_of_en_words, num_of_pl_words) tuple.
    """
    en_dir = cache_dir / "words_en"
    pl_dir = cache_dir / "words_pl"

    def count_words(dir):
        return len(list(dir.glob("*.json"))) if dir.is_dir() else 0

    num_of_en_words = count_words(en_dir)
    num_of_pl_words = count_words(pl_dir)
    return num_of_en_words, num_of_pl_words


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

                if "Variants" in meaning:
                    for var in meaning["Variants"]:
                        result.append(wrap(", ".join(var["Variant"]), 5, 5))
                        result.append("")
                    for ex in var["ExampleSentences"]:
                        result.append(wrap(ex["Sentence"], 6, 6))
                        result.append(wrap(ex["Translation"], 6, 6))
                        result.append("")

                if "ExampleSentences" in meaning:
                    for ex in meaning["ExampleSentences"]:
                        result.append(wrap(ex["Sentence"], 6, 6))
                        result.append(wrap(ex["Translation"], 6, 6))
                        result.append("")

    return result
