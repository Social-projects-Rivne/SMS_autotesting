# -*- coding: utf-8 -*-
"""
utils.logging

Module contains logging settings and executes scripts for
log files rotations.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

import os

from ..settings import LOG_DIR, TRACK_USERS
from .log_directory import prepare_log_directory, prepare_out_log_file, \
                           prepare_err_log_file


# execute functions for daily log rotations
CUR_DIR_NAME = prepare_log_directory(LOG_DIR)
LOG_FILE_OUT = prepare_out_log_file(CUR_DIR_NAME)
LOG_FILE_ERR = prepare_err_log_file(CUR_DIR_NAME)

if not TRACK_USERS:
    TRACK_USERS = ['null']
else:
    TRACK_USERS = ['out_file']

# logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'out_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE_OUT,
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'err_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE_ERR,
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'err_file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'WARNING'),
        },
        'SMS.apps.core.views.login': {
            'handlers': ['console', 'out_file'],
            'level': 'INFO',
        },
        'SMS.apps.mainteacher.signals': {
            'handlers': ['console', 'out_file'],
            'level': 'INFO',
        },
        'SMS.apps.director.signals': {
            'handlers': ['console', 'out_file'],
            'level': 'INFO',
        },
        'SMS.apps.teacher.signals': {
            'handlers': ['console', 'out_file'],
            'level': 'INFO',
        },
        'SMS.apps.mainteacher.utils.email': {
            'handlers': ['console', 'err_file'],
            'level': 'WARNING',
        },
        'email_status': {
            'handlers': ['console', 'out_file'],
            'level': 'INFO',
        },
        'track_users': {
            'handlers': TRACK_USERS,
            'level': 'INFO',
        },
    }
}
