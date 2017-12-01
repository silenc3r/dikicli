import logging
import os
import sys
from pathlib import Path

URL = 'https://www.diki.pl/{word}'
HEADERS = {'User-Agent': ('Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; '
                          'Trident/7.0;  rv:11.0) like Gecko')}


def _get_env(var, type):
    v = os.getenv(var)
    if v is None:
        return v
    if not os.path.exists(v):
        raise FileNotFoundError(
            "ERROR: Invalid env '{var}': {type} does not exist"
            "".format(var=var, type=type.capitalize()))
    if ((type == 'file' and os.path.isfile(v))
            or (type == 'directory' and os.path.isdir(v))):
        return v
    else:
        raise FileNotFoundError("ERROR: Invalid env: '{var}' is not a {type}"
                                "".format(var=var, type=type))


APP_DIR = os.path.dirname(os.path.realpath(__file__))
HOME = os.path.expanduser('~')

# get env variables if defined
try:
    CONFIG_FILE = _get_env('DIKI_CONFIG_FILE', 'file')
    CACHE_DIR = _get_env('DIKI_CACHE_DIR', 'directory')
    DATA_DIR = _get_env('DIKI_DATA_DIR', 'directory')
    HISTORY_FILE = _get_env('DIKI_HIST_FILE', 'file')
except FileNotFoundError as e:
    print(str(e), file=sys.stderr)
    sys.exit(1)

# set default paths and create directories if needed
if not CONFIG_FILE:
    CONFIG_FILE = os.path.join(
        os.getenv('XDG_CONFIG_HOME', os.path.join(HOME, '.config')),
        'dikicli', 'diki.conf')
    parent = os.path.dirname(CONFIG_FILE)
    if not os.path.exists(parent):
        os.mkdir(parent)
if not CACHE_DIR:
    CACHE_DIR = os.path.join(
        os.getenv('XDG_CACHE_HOME', os.path.join(HOME, '.cache')),
        'dikicli')
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)
if not DATA_DIR:
    DATA_DIR = os.path.join(
        os.getenv('XDG_DATA_HOME', os.path.join(HOME, '.local', 'share')),
        'dikicli')
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
if not HISTORY_FILE:
    HISTORY_FILE = os.path.join(DATA_DIR, 'words.txt')
    if not os.path.exists(HISTORY_FILE):
        Path(HISTORY_FILE).touch()

LOG_PATH = os.path.join(CACHE_DIR, 'diki.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOG_PATH)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)
