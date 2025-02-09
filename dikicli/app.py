# -*- coding: utf-8 -*-

import argparse
import json
import logging
import logging.handlers
import os
import pathlib
import random
import sys

from dikicli.__version__ import __version__
from dikicli.config import Config
from dikicli.core import WordNotFound
from dikicli.core import cache_lookup
from dikicli.core import cache_store
from dikicli.core import generate_index_html
from dikicli.core import generate_word_html
from dikicli.core import get_stats
from dikicli.core import get_word_list
from dikicli.core import lookup_online
from dikicli.core import parse_en_pl
from dikicli.core import parse_pl_en
from dikicli.core import wrap_text

XDG_CACHE_HOME = pathlib.Path(os.environ.get("XDG_CACHE_HOME", "~/.cache")).expanduser()
XDG_CONFIG_HOME = pathlib.Path(
    os.environ.get("XDG_CONFIG_HOME", "~/.config")
).expanduser()
XDG_STATE_HOME = pathlib.Path(
    os.environ.get("XDG_STATE_HOME", "~/.local/state")
).expanduser()

Log = logging.getLogger(__name__)


def configure_logging(log_file, debug=False):
    logger = logging.getLogger("dikicli")

    format_verbose = "[%(levelname)-s] %(asctime)s <%(name)s:%(funcName)s> %(message)s"
    format_simple = "[%(levelname)-s] %(message)s"
    date_fmt = "%Y-%m-%d %H:%M:%S"

    formatter_v = logging.Formatter(format_verbose, date_fmt)
    formatter_s = logging.Formatter(format_simple, date_fmt)

    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setLevel(logging.WARNING if not debug else logging.DEBUG)
    stream_handler.setFormatter(formatter_s if not debug else formatter_v)

    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=1048576, backupCount=5
    )
    file_handler.setLevel(logging.INFO if not debug else logging.DEBUG)
    file_handler.setFormatter(formatter_v)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    # prevent duplicate logs
    logger.propagate = False

    # configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(stream_handler)


def get_version():
    import pkg_resources

    return pkg_resources.get_distribution("dikicli").version


def get_parser():
    parser = argparse.ArgumentParser(
        prog="diki", description="Commandline interface for diki.pl"
    )
    parser.add_argument("--version", action="version", version=f"dikicli {__version__}")
    parser.add_argument(
        "--create-config", action="store_true", help="create default configuration file"
    )
    parser.add_argument(
        "-r", "--refresh", action="store_true", dest="ignore_cache", help="ignore cache"
    )
    parser.add_argument("-s", "--stats", action="store_true", help="show statistics")
    parser.add_argument("--json", action="store_true", help="output json")
    translation = parser.add_argument_group("translation")
    translation.add_argument("word", nargs="?", help="word to translate")
    translation.add_argument(
        "-p", "--pol-eng", action="store_true", help="translate polish word to english"
    )
    translation.add_argument(
        "-w",
        "--linewrap",
        "--linewidth",
        dest="linewidth",
        type=int,
        metavar="WIDTH",
        help=("wrap lines longer than WIDTH; set to 0 to disable wrapping"),
    )
    html = parser.add_argument_group("html")
    html.add_argument(
        "-i",
        "--display-index",
        action="store_true",
        help="open index file in web browser",
    )
    return parser


def translate(word, parse_fn, cache_dir, ignore_cache):
    """Translate a word.

    If cache_dir doesn't exist it will be created.

    Args:
        word (str): Word to translate.
        cache_dir (pathlib.Path): Path to cache directory.
        ignore_cache (bool): Whether to use cached data.
        parse_fn (fn): Parse function.

    Returns:
        dict: Translation data structure.

    Raises:
        WordNotFound: When word was not found.

    """
    translation = None

    if ignore_cache:
        Log.debug("ignoring cache")

    if not ignore_cache and cache_dir.is_dir():
        translation = cache_lookup(cache_dir, word)
        if translation:
            return translation

    # This can throw WordNotFound
    html_dump = lookup_online(word)

    Log.debug("parsing html")
    translation = parse_fn(html_dump)

    # cache_dir will be created if it doesn't exist.
    cache_store(cache_dir, word, translation)

    return translation


def _main():
    parser = get_parser()
    args = parser.parse_args()

    # if ran with no arguments print usage and exit
    if len(sys.argv) == 1:
        # TODO: make usage more informative
        parser.print_usage()
        sys.exit(1)

    if "DIKI_CONFIG_FILE" in os.environ:
        config_file = pathlib.Path(os.environ["DIKI_CONFIG_FILE"]).expanduser()
        Log.debug("DIKI_CONFIG_FILE defined: %s", config_file)
    else:
        config_file = XDG_CONFIG_HOME / "dikicli/diki.conf"
    if "DIKI_DATA_DIR" in os.environ:
        data_dir = pathlib.Path(os.environ["DIKI_DATA_DIR"]).expanduser()
        Log.debug("DIKI_DATA_DIR defined: %s", data_dir)
    else:
        data_dir = XDG_STATE_HOME / "dikicli"

    config = Config(config_file, data_dir)
    config.read_config()

    if args.linewidth:
        config["linewidth"] = str(args.linewidth)
    linewidth = int(config["linewidth"])
    Log.debug("linewidth set to: %s", linewidth)

    # create configuration file
    if args.create_config:
        config_file = config.create_default_config()
        msg = "New config file created: %s"
        Log.info(msg, config_file)
        print(msg % config_file)
        sys.exit(0)

    # handle word translation
    if args.word:
        pl_to_en = args.pol_eng
        if not pl_to_en:
            # en -> pl
            Log.debug("translating en->pl: %s", args.word)
            parse_fn = parse_en_pl
            cache_dir = data_dir / "words_en"
        else:
            # pl -> en
            Log.debug("translating pl->en: %s", args.word)
            parse_fn = parse_pl_en
            cache_dir = data_dir / "words_pl"

        try:
            translation = translate(args.word, parse_fn, cache_dir, args.ignore_cache)
            if args.json:
                output = json.dumps(translation, indent=4, ensure_ascii=False)
            else:
                output = "\n".join(wrap_text(translation, linewidth))
            print(output)
            sys.exit(0)
        except WordNotFound as e:
            Log.error("WordNotFound: %s", args.word)
            print(e, file=sys.stderr)
            sys.exit(1)

    # open index file in browser
    if args.display_index:
        from dikicli.server import Server

        server = Server()
        cache_dir = data_dir / "words_en"

        @server.route("/")
        def index(path):
            return generate_index_html(cache_dir)

        @server.route("/random_word")
        def random_word(path):
            wlist = get_word_list(cache_dir)
            word = random.choice(wlist)
            return {"redirect": f"/words/{word}"}

        @server.route("default")
        def get_word(path):
            path = path[1:]
            plist = path.split("/")
            if plist[0] != "words":
                return None
            word = plist[1]
            return generate_word_html(cache_dir, word)

        server.open_index()
        sys.exit(0)

    if args.stats:
        en, pl = get_stats(data_dir)
        print("english words:  {}".format(en))
        print(" polish words:  {}".format(pl))
        sys.exit(0)


def main():
    try:
        if "DIKI_LOG_FILE" in os.environ:
            log_file = pathlib.Path(os.environ["DIKI_LOG_FILE"]).expanduser()
        else:
            cache_dir = XDG_CACHE_HOME / "dikicli"
            if not cache_dir.is_dir():
                cache_dir.mkdir(parents=True)
            log_file = cache_dir / "diki.log"

        debug = "DIKI_DEBUG" in os.environ
        configure_logging(log_file, debug)

        _main()
    except KeyboardInterrupt:
        print("Aborting...", file=sys.stderr)
        sys.exit(1)
