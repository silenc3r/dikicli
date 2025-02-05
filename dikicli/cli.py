# -*- coding: utf-8 -*-

import argparse
import logging
import logging.config
import pathlib
import sys

from dikicli.core import CACHE_DIR
from dikicli.core import DEBUG
from dikicli.core import Config
from dikicli.core import display_index
from dikicli.core import get_stats
from dikicli.core import translate
from dikicli.core import wrap_text
from dikicli.core import WordNotFound
from dikicli.core import lookup_online
from dikicli.core import cache_store, cache_lookup
from dikicli.core import parse_en_pl
from dikicli.helpers import flatten_compat

LOG_FILE = CACHE_DIR.joinpath("diki.log")
if not CACHE_DIR.exists():
    CACHE_DIR.mkdir(parents=True)

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
            },
            "simple": {"format": "%(message)s"},
        },
        "handlers": {
            "console": {
                "level": logging.WARNING,
                "class": "logging.StreamHandler",
                "formatter": "simple",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": LOG_FILE,
                "maxBytes": 1048576,
                "backupCount": 5,
                "formatter": "verbose",
            },
        },
        "loggers": {
            "dikicli": {
                "handlers": ["file", "console"],
                "level": logging.DEBUG if DEBUG else logging.INFO,
            }
        },
    }
)
logger = logging.getLogger(__name__)


def get_version():
    # pylint: disable=import-outside-toplevel
    import pkg_resources

    return pkg_resources.get_distribution("dikicli").version


def get_parser():
    parser = argparse.ArgumentParser(
        prog="diki", description="Commandline interface for diki.pl"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="dikicli {version}".format(version=get_version()),
    )
    parser.add_argument(
        "--create-config", action="store_true", help="create default configuration file"
    )
    parser.add_argument("-r", "--refresh", action="store_true", help="ignore cache")
    parser.add_argument("-s", "--stats", action="store_true", help="show statistics")
    translation = parser.add_argument_group("translation")
    translation.add_argument("word", nargs="?", help="word to translate")
    translation.add_argument(
        "-p", "--pol-eng", action="store_true", help="translate polish word to english"
    )
    translation.add_argument(
        "-w",
        "--linewrap",
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


def translate_f(word, cache_dir, use_cache, parse_fn):
    """Translate a word.

    If cache_dir doesn't exist it will be created.

    Args:
        word (str): Word to translate.
        cache_dir (pathlib.Path): Path to cache directory.
        use_cache (bool): Whether to use cached data.
        parse_fn (fn): Parse function.

    Returns:
        dict: Translation data structure.

    Raises:
        WordNotFound: When word was not found.

    """
    translation = None

    if use_cache and cache_dir.is_dir():
        translation = cache_lookup(word, cache_dir)
        if translation:
            return translation

    # This can throw WordNotFound
    html_dump = lookup_online(word)
    translation = parse_fn(html_dump)

    if use_cache:
        # cache_dir will be created if it doesn't exist.
        cache_store(word, translation, cache_dir)

    return translation


def translate_en_pl(word, cache_dir, use_cache):
    return translate_f(word, cache_dir / "words_en", use_cache, parse_en_pl)


def translate_pl_en(word, cache_dir, use_cache):
    return translate_f(word, cache_dir / "words_pl", use_cache, parse_pl_en)


def _main():
    parser = get_parser()
    args = parser.parse_args()

    # if ran with no arguments print usage and exit
    if len(sys.argv) == 1:
        # TODO: make usage more informative
        parser.print_usage()
        sys.exit(1)

    config = Config()
    config.read_config()

    if args.linewrap:
        config["linewrap"] = args.linewrap
    linewrap = int(config["linewrap"])

    # create configuration file
    if args.create_config:
        config_file = config.create_default_config()
        print("New config file created: {}".format(config_file))
        sys.exit(0)


    data_dir = pathlib.Path(config["data dir"])

    # handle word translation
    if args.word:
        use_cache = not args.refresh

        pl_to_en = args.pol_eng
        if not pl_to_en:
            # en -> pl
            try:
                translation = translate_en_pl(args.word, data_dir, use_cache)
                translation = flatten_compat(translation)
                wrapped_text = "\n".join(wrap_text(translation, linewrap))
                print(wrapped_text)
                sys.exit(0)
            except WordNotFound as e:
                print(e, file=sys.stderr)
                sys.exit(1)
        else:
            # pl -> en
            try:
                translation = translate(args.word, data_dir, use_cache, pl_to_en)
                wrapped_text = "\n".join(wrap_text(translation, linewrap))
                print(wrapped_text)
                sys.exit(0)
            except WordNotFound as e:
                print(e, file=sys.stderr)
                sys.exit(1)

    # open index file in browser
    if args.display_index:
        try:
            browser = config["web browser"]
            display_index(data_dir, browser)
            sys.exit(0)
        except FileNotFoundError as e:
            logger.error(e)
            sys.exit(1)

    if args.stats:
        en, pl = get_stats(data_dir)
        print("english words:  {}".format(en))
        print(" polish words:  {}".format(pl))
        sys.exit(0)


def main():
    try:
        _main()
    except KeyboardInterrupt:
        logger.warning("aborting...")
        sys.exit(1)
