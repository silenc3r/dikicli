import argparse
import logging
import sys
import textwrap
import urllib.request
import webbrowser

from pathlib import Path

from . import CONFIG_FILE, DATA_DIR
from .core import WordNotFound
from .core import cache_lookup, get_config, parse
from .core import save_to_history, write_html_file, write_index_file

URL = 'https://www.diki.pl/{word}'
HEADERS = {'User-Agent': ('Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; '
                          'Trident/7.0;  rv:11.0) like Gecko')}

logger = logging.getLogger(__name__)


def pretty_print(translations, linewrap=0):
    """
    Pretty print translations.

    If linewrap is set to 0 disble line wrapping.

    :translations: dictionary of word translations
    :linewrap: maximum line lenght before wrapping
    """

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
    translation.add_argument('-w', '--linewrap', metavar='WIDTH', type=int,
                             help=('wrap lines longer than WIDTH;'
                                   ' set to 0 to disable wrapping'))
    html = parser.add_argument_group('html')
    html.add_argument('-i', '--display-index', action='store_true',
                      help='open index file in web browser')
    html.add_argument('--full', action='store_true',
                      help="display all words, even if prefix doesn't match")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    # this creates default config file if it doesn't exist
    config = get_config(Path(CONFIG_FILE))

    # if ran with no arguments print usage and exit
    if len(sys.argv) == 1:
        # TODO: make usage more informative
        parser.print_usage()
        sys.exit(1)

    if DATA_DIR:
        config['dikicli']['data dir'] = DATA_DIR
    data_dir = Path(config['dikicli']['data dir'])
    prefix = config['dikicli']['prefix']
    if args.linewrap:
        config['dikicli']['linewrap'] = str(args.linewrap)
    linewrap = config['dikicli'].getint('linewrap')

    if not data_dir.exists():
        logger.info("Creating directory: %s", data_dir)
        data_dir.mkdir()

    # handle word translation
    if args.word:
        logger.info("Translating word: %s", args.word)
        word = args.word
        cached = cache_lookup(word, data_dir)
        if cached:
            logger.info("Printing cached: %s", word)
            pretty_print(cached, linewrap)
        else:
            logger.info("Looking up online: %s", word)
            req = urllib.request.Request(URL.format(word=word),
                                         headers=HEADERS)
            with urllib.request.urlopen(req) as response:
                try:
                    logger.debug("Parsing response: %s", word)
                    translation = parse(response.read())
                except WordNotFound as e:
                    logger.error(str(e))
                    sys.exit(1)

            logger.debug("Printing: %s", word)
            pretty_print(translation, linewrap)
            save_to_history(word, prefix, data_dir)
            write_html_file(word, translation, data_dir)
            write_index_file(prefix, data_dir)
            write_index_file(prefix, data_dir, full=True)

    # open index file in browser
    if args.display_index:
        browser = config['dikicli']['web browser'].lower()
        if browser in webbrowser._browsers:
            b = webbrowser.get(browser)
        else:
            if browser != 'default':
                logger.warn("Couldn't find '%s' browser. "
                            "Falling back to default.", browser)
            b = webbrowser.get()

        index_file = 'index-full.html' if args.full else 'index.html'
        write_index_file(prefix, data_dir, full=args.full)
        logger.info("Opening %s in '%s'", index_file, b.name)
        b.open(data_dir.joinpath(index_file).as_uri())
        sys.exit(0)
