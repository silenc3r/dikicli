import argparse
import logging
import logging.config
import os
import sys
import textwrap
import urllib.parse
import urllib.request
import webbrowser

from pathlib import Path

from .core import WordNotFound
from .core import Config
from .core import cache_lookup, parse
from .core import save_to_history, write_html_file, write_index_file

URL = 'https://www.diki.pl/{word}'
HEADERS = {'User-Agent': ('Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; '
                          'Trident/7.0;  rv:11.0) like Gecko')}


def get_env_path(var, type):
    """
    Get path from environment variable.

    If variable is defined but doesn't contain valid path raise exception.

    :var: variable name too lookup in env
    :type: wheter variable is file or directory

    :returns: path string or None
    :raises: FileNotFoundError
    """
    v = os.getenv(var)
    if v is None:
        return v
    if not os.path.exists(v):
        raise FileNotFoundError("ERROR: Invalid env '{var}': {type} does not exist"
                                "".format(var=var, type=type.capitalize()))
    if (type == 'file' and os.path.isfile(v)) or (type == 'directory' and os.path.isdir(v)):
        return os.path.abspath(v)
    else:
        raise FileNotFoundError("ERROR: Invalid env: '{var}' is not a {type}"
                                "".format(var=var, type=type))


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
            print(' ' * findent, text)
        else:
            print(textwrap.fill(text, width=width, initial_indent=' ' * findent,
                                subsequent_indent=' ' * sindent))

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
                    print_wrapped(e[0], findent=indent + 2, sindent=indent + 2)
                    if e[1]:
                        print_wrapped(e[1], findent=indent + 2, sindent=indent + 3)


def configure():
    # get env variables if defined
    try:
        CONFIG_FILE = get_env_path('DIKI_CONFIG_FILE', 'file')
        CACHE_DIR = get_env_path('DIKI_CACHE_DIR', 'directory')
        DATA_DIR = get_env_path('DIKI_DATA_DIR', 'directory')
        DEBUG = os.getenv('DIKI_DEBUG')
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    HOME = os.path.expanduser('~')
    CONFIG_FILE = CONFIG_FILE or os.path.join(
        os.getenv('XDG_CONFIG_HOME', os.path.join(HOME, '.config')), 'dikicli', 'diki.conf')
    CACHE_DIR = CACHE_DIR or os.path.join(
        os.getenv('XDG_CACHE_HOME', os.path.join(HOME, '.cache')), 'dikicli')
    DATA_DIR = DATA_DIR or os.path.join(
        os.getenv('XDG_DATA_HOME', os.path.join(HOME, '.local', 'share')), 'dikicli')

    # configure logging
    LOG_FILE = os.path.join(CACHE_DIR, 'diki.log')
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
            },
            'simple': {
                'format': '%(levelname)s: %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': logging.WARNING,
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': LOG_FILE,
                'maxBytes': 1048576,
                'backupCount': 5,
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'dikicli': {
                'handlers': ['file', 'console'],
                'level': logging.DEBUG if DEBUG else logging.INFO,
            },
        },
    })

    config = Config(CONFIG_FILE, DATA_DIR)
    config.read_config()
    return config


def get_parser():
    parser = argparse.ArgumentParser(
        prog='diki',
        description='Commandline interface for diki.pl'
    )
    parser.add_argument('--create-config', action='store_true',
                        help='create default configuration file')
    translation = parser.add_argument_group('translation')
    translation.add_argument('word', nargs='?', help='word to translate')
    translation.add_argument('-p', '--pol-eng', action='store_true',
                             help='translate polish word to english')
    translation.add_argument('-w', '--linewrap', metavar='WIDTH',
                             help=('wrap lines longer than WIDTH; set to 0 to disable wrapping'))
    html = parser.add_argument_group('html')
    html.add_argument('-i', '--display-index', action='store_true',
                      help='open index file in web browser')
    html.add_argument('--full', action='store_true',
                      help="display all words, even if prefix doesn't match")
    return parser


def main():
    logger = logging.getLogger(__name__)

    # parse commandline arguments
    parser = get_parser()
    args = parser.parse_args()

    # if ran with no arguments print usage and exit
    if len(sys.argv) == 1:
        # TODO: make usage more informative
        parser.print_usage()
        sys.exit(1)

    config = configure()

    data_dir = Path(config['data dir'])
    prefix = config['prefix']
    if args.linewrap:
        config['linewrap'] = args.linewrap
    linewrap = int(config['linewrap'])

    if not data_dir.exists():
        logger.info("Creating directory: %s", data_dir.as_posix())
        data_dir.mkdir()

    # create configuration file
    if args.create_config:
        config_file = config.create_default_config()
        print("New config file created: {}".format(config_file))
        sys.exit(0)

    # handle word translation
    if args.word:
        logger.info("Translating word: %s", args.word)
        word = args.word
        cached = cache_lookup(word, data_dir, native=args.pol_eng)
        if cached:
            logger.info("Printing cached: %s", word)
            pretty_print(cached, linewrap)
        else:
            logger.info("Looking up online: %s", word)
            quoted_word = urllib.parse.quote(word)
            req = urllib.request.Request(URL.format(word=quoted_word), headers=HEADERS)
            with urllib.request.urlopen(req) as response:
                try:
                    logger.debug("Parsing response: %s", word)
                    translation = parse(response.read(), native=args.pol_eng)
                except WordNotFound as e:
                    logger.error(str(e))
                    sys.exit(1)

            logger.debug("Printing: %s", word)
            pretty_print(translation, linewrap)
            write_html_file(word, translation, data_dir, native=args.pol_eng)
            if not args.pol_eng:
                save_to_history(word, prefix, data_dir)
                write_index_file(prefix, data_dir)
                write_index_file(prefix, data_dir, full=True)

    # open index file in browser
    if args.display_index:
        browser = config['web browser'].lower()
        if browser in webbrowser._browsers:
            b = webbrowser.get(browser)
        else:
            if browser != 'default':
                logger.warn("Couldn't find '%s' browser. Falling back to default.", browser)
            b = webbrowser.get()

        index_file = write_index_file(prefix, data_dir, full=args.full)
        logger.info("Opening %s in '%s'", index_file.as_posix(), b.name)
        b.open(index_file.as_uri())
        sys.exit(0)
