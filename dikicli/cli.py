# pylint: disable=too-many-locals

import argparse
import sys
import textwrap

from .core import Config
from .core import WordNotFound
from .core import display_index
from .core import translate


def pretty_print(translations, linewrap=0):
    """Pretty print translations.

    If linewrap is set to 0 disble line wrapping.

    Parameters
    ----------
    translations : dict
        Dictionary of word translations.
    linewrap : int
        Maximum line length before wrapping.
    """
    # TODO: wrapping and printing should be separate actions
    #       i.e. we should create wrapped multiline string
    #       and print it once

    def print_wrapped(text, width=linewrap, findent=0, sindent=0, bold=False):
        # don't use bold when stdout is pipe or redirect
        if bold and sys.stdout.isatty():
            text = "\033[0;1m" + text + "\033[0m"
        if width == 0:
            print(" " * findent, text)
        else:
            print(
                textwrap.fill(
                    text,
                    width=width,
                    initial_indent=" " * findent,
                    subsequent_indent=" " * sindent,
                )
            )

    indent = 5
    for i1, trans in enumerate(translations):
        words = trans[0]
        meanings = trans[1]
        if i1 > 0:
            print("\n")
        for w in words:
            print_wrapped(w, bold=True)
        for i2, t in enumerate(meanings):
            if i2 > 0:
                print()
            part = t["part"]
            if part:
                print("[{part}]".format(part=part))
            for i3, m in enumerate(t["meanings_list"], 1):
                if i3 > 1:
                    print()
                meaning = "{index:>3}. {meanings}".format(
                    index=i3, meanings=", ".join(m["meaning"])
                )
                print_wrapped(meaning, sindent=indent, bold=True)
                for e in m["examples"]:
                    print()
                    print_wrapped(e[0], findent=indent + 2, sindent=indent + 2)
                    if e[1]:
                        print_wrapped(e[1], findent=indent + 2, sindent=indent + 3)


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
            pretty_print(translation, linewrap)
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
