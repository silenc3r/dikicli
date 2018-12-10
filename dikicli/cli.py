import argparse
import sys

from .core import Config
from .core import WordNotFound
from .core import display_index
from .core import translate
from .core import wrap_text


def get_parser():
    parser = argparse.ArgumentParser(
        prog="diki", description="Commandline interface for diki.pl"
    )
    parser.add_argument(
        "--create-config", action="store_true", help="create default configuration file"
    )
    parser.add_argument("-r", "--refresh", action="store_true", help="ignore cache")
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


def main():
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
        except WordNotFound:
            sys.exit(1)

    # open index file in browser
    if args.display_index:
        try:
            display_index(config)
            sys.exit(0)
        except FileNotFoundError:
            sys.exit(1)
