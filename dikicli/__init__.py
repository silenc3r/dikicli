import logging.config
import os
import sys

# APP_DIR = os.path.dirname(os.path.realpath(__file__))


def _get_env_path(var, type):
    """
    Get path from environment variable.

    If variable is defined but path isn't valid raise exception.

    :var: variable name too lookup in env
    :type: wheter variable is file or directory

    :returns: path string or None
    :raises: FileNotFoundError
    """
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


# get env variables if defined
try:
    CONFIG_FILE = _get_env_path('DIKI_CONFIG_FILE', 'file')
    CACHE_DIR = _get_env_path('DIKI_CACHE_DIR', 'directory')
    DATA_DIR = _get_env_path('DIKI_DATA_DIR', 'directory')
except FileNotFoundError as e:
    print(str(e), file=sys.stderr)
    sys.exit(1)

# set default paths
HOME = os.path.expanduser('~')
CONFIG_FILE = CONFIG_FILE or os.path.join(
    os.getenv('XDG_CONFIG_HOME', os.path.join(HOME, '.config')),
    'dikicli', 'diki.conf')
CACHE_DIR = CACHE_DIR or os.path.join(
    os.getenv('XDG_CACHE_HOME', os.path.join(HOME, '.cache')), 'dikicli')
DATA_DIR = DATA_DIR or os.path.join(
    os.getenv('XDG_DATA_HOME', os.path.join(HOME, '.local', 'share')),
    'dikicli')

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
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'dikicli': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        },
    },
})
