import argparse
import logging
import sys
import textwrap
import urllib.request
import webbrowser

from pathlib import Path

from . import CONFIG_FILE, URL, HEADERS
from .core import WordNotFound
from .core import cache_lookup, get_config, parse
from .core import write_to_file, write_html_file, write_index_file

logger = logging.getLogger(__name__)


def pretty_print(translations, linewrap=0):

    def print_wrapped(text, width=linewrap, findent=0, sindent=0, bold=False):
        # don't use bold when stdout is pipe or redirect
        if bold and sys.stdout.isatty():
            text = "\033[0;1m" + text + "\033[0m"
        if width == 0:
            print(' '*findent, text)
        else:
            print(textwrap.fill(text, width=width,
                                initial_indent=' '*findent,
                                subsequent_indent=' '*sindent))

    indent = 5
    for i1, words in enumerate(translations):
        if i1 > 0:
            print("\n")
        for w in words:
            print_wrapped(w, bold=True)
        for i2, t in enumerate(translations[words]):
            if i2 > 0:
                print()
            part = t['part']
            if part:
                print("[{part}]".format(part=part))
            for i3, m in enumerate(t['meanings_list'], 1):
                if i3 > 1:
                    print()
                meaning = "{index:>3}. {meanings}".format(
                    index=i3, meanings=', '.join(m['meaning']))
                print_wrapped(meaning, sindent=indent, bold=True)
                for e in m['examples']:
                    print()
                    print_wrapped(e[0], findent=indent+2, sindent=indent+2)
                    print_wrapped(e[1], findent=indent+2, sindent=indent+3)


def get_parser():
    parser = argparse.ArgumentParser(
        prog='dikicli',
        description='Commandline interface for diki.pl'
    )
    translation = parser.add_argument_group('translation')
    translation.add_argument('word', nargs='?', help='word to translate')
    translation.add_argument('-w', '--linewrap', metavar='WIDTH',
                             help=('wrap lines longer than WIDTH;'
                                   ' set to 0 to disable wrapping'))
    html = parser.add_argument_group('html')
    html.add_argument('-i', '--display-index', action='store_true',
                      help='open index file in web browser')
    html.add_argument('--create-index', action='store_true',
                      help='regenerate index file')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    # FIXME: logging starts here

    # if ran with no arguments print usage and exit
    if len(sys.argv) == 1:
        # TODO: make usage more informative
        parser.print_usage()
        sys.exit(1)

    # configuration
    config = get_config(Path(CONFIG_FILE))

    data_dir = Path(config['dikicli']['data dir'])
    hist_file = Path(config['dikicli']['history file'])
    prefix = config['dikicli']['prefix']
    if args.linewrap:
        config['dikicli']['linewrap'] = args.linewrap
    linewrap = config['dikicli'].getint('linewrap')

    # handle word translation
    if args.word:
        word = args.word
        cached = cache_lookup(word, data_dir)
        if cached:
            logger.info("Printing cached: %s", word)
            pretty_print(cached, linewrap)
        else:
            req = urllib.request.Request(URL.format(word=word),
                                         headers=HEADERS)
            with urllib.request.urlopen(req) as response:
                try:
                    translation = parse(response.read())
                except WordNotFound as e:
                    print(str(e), file=sys.stderr)
                    sys.exit(1)

            pretty_print(translation, linewrap)
            write_to_file(hist_file, word, prefix)
            write_html_file(word, translation, data_dir)
            write_index_file(hist_file, prefix, data_dir)

    # open index file in browser
    if args.display_index:
        browser = config['dikicli']['web browser'].lower()
        if browser != 'default':
            if browser in webbrowser._browsers:
                b = webbrowser.get(browser)
            else:
                logger.warn("Couldn't find '%s' browser. "
                            "Falling back to default.", browser)
                # print("Couldn't find '{browser}' browser."
                #       " Falling back to default.".format(browser=browser),
                #       file=sys.stderr)
                browser = 'default'
                b = webbrowser.get()
        else:
            b = webbrowser.get()

        index_file = data_dir.joinpath('index.html')
        if not index_file.is_file():
            logger.error("Index file not found")
            # print("Index file not found!", file=sys.stderr)
            sys.exit(1)
        logger.info("Opening index.html in '%s' browser", browser)
        b.open(index_file.as_uri())
        sys.exit(0)
