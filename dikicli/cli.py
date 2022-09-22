# -*- coding: utf-8 -*-

import argparse
import logging
import logging.config
import pathlib
import sys

import requests

from .core import CACHE_DIR
from .core import DEBUG
from .core import Config
from .core import WordNotFound
from .core import display_index
from .core import get_stats
from .core import translate
from .core import wrap_text

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

    # handle word translation
    if args.word:
        use_cache = not args.refresh
        to_eng = args.pol_eng
        try:
            translation = translate(args.word, config, use_cache, to_eng)
            wrapped_text = wrap_text(translation, linewrap)
            print(wrapped_text)
            sys.exit(0)
        except (WordNotFound, requests.exceptions.ConnectionError) as e:
            logger.error(e)
            sys.exit(1)

    # open index file in browser
    if args.display_index:
        try:
            browser = config["web browser"]
            data_dir = pathlib.Path(config["data dir"])
            display_index(data_dir, browser)
            sys.exit(0)
        except FileNotFoundError as e:
            logger.error(e)
            sys.exit(1)

    if args.stats:
        en, pl = get_stats(pathlib.Path(config["data dir"]))
        print("english words:  {}".format(en))
        print(" polish words:  {}".format(pl))
        sys.exit(0)


def main():
    try:
        _main()
    except KeyboardInterrupt:
        logger.warning("aborting...")
        sys.exit(1)
