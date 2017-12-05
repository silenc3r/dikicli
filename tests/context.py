import logging.config
import os
import sys

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, basedir)

TEST_DIR = os.path.dirname(os.path.realpath(__file__))

logfile = os.path.join(basedir, 'test_log.txt')

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': logfile,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'dikicli': {
            'handlers': ['file'],
            'level': logging.DEBUG,
        },
    },
})
