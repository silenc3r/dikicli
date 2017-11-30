import argparse
import os
import sys
import textwrap
import urllib.request
import webbrowser

from pathlib import Path

from .core import URL, HEADERS
from .core import WordNotFound
from .core import cache_lookup, get_config, parse
from .core import write_to_file, write_html_file, write_index_file


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


def get_env(var):
    try:
        file = os.getenv(var)
        Path(file).stat()
        return file
    except TypeError:
        return None


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
    ENV_CONFIG_FILE = get_env('DIKI_CONFIG_FILE')
    ENV_CACHE_DIR = get_env('DIKI_CACHE_DIR')
    ENV_DATA_DIR = get_env('DIKI_DATA_DIR')
    ENV_HISTORY_FILE = get_env('DIKI_HIST_FILE')

    if ENV_CONFIG_FILE:
        config = get_config(Path(ENV_CONFIG_FILE))
    else:
        config = get_config()

    if ENV_CACHE_DIR:
        config['dikicli']['cache dir'] = ENV_CACHE_DIR
    if ENV_DATA_DIR:
        config['dikicli']['data dir'] = ENV_DATA_DIR
    if ENV_HISTORY_FILE:
        config['dikicli']['history file'] = ENV_HISTORY_FILE

    parser = get_parser()
    args = parser.parse_args()

    # if ran with no arguments print usage and exit
    if len(sys.argv) == 1:
        # TODO: make usage more informative
        parser.print_usage()
        sys.exit(1)

    # options
    cache_dir = Path(config['dikicli']['cache dir'])
    data_dir = Path(config['dikicli']['data dir'])
    hist_file = Path(config['dikicli']['history file'])
    prefix = config['dikicli']['prefix']
    if args.linewrap:
        config['dikicli']['linewrap'] = args.linewrap
    linewrap = config['dikicli'].getint('linewrap')

    # create cache and data dirs if they don't exist
    if not cache_dir.is_dir():
        cache_dir.mkdir(parents=True)
    if not data_dir.is_dir():
        data_dir.mkdir(parents=True)

    # create history file if it doesn't exist
    if not hist_file.is_file():
        parent = hist_file.parent()
        if not parent.exists():
            parent.mkdir(parents=True)
        hist_file.touch()

    # handle word translation
    if args.word:
        word = args.word
        cached = cache_lookup(word, data_dir)
        if cached:
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
        # TODO: add logging
        if browser != 'default':
            if browser in webbrowser._browsers:
                b = webbrowser.get(browser)
            else:
                print("Couldn't find '{browser}' browser."
                      " Falling back to default.".format(browser=browser),
                      file=sys.stderr)
                b = webbrowser.get()
        else:
            b = webbrowser.get()

        index_file = data_dir.joinpath('index.html')
        if not index_file.is_file():
            print("Index file not found!", file=sys.stderr)
            sys.exit(1)
        b.open(index_file.as_uri())
        sys.exit(0)
