# -*- coding: utf-8 -*-
"""
utils.log_directory

Module contains three functions for preparing folder for log files of
current day.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

import os
from datetime import date


def prepare_log_directory(LOG_DIR):
    """prepare_log_directory(str) -> str

    Prepare log directory function. Take string path to
    BASE FIRECTORY, create current day log folder and return path
    to it.
    """
    # define current day log folder
    CUR_DIR_NAME = LOG_DIR + '/' + str(date.today())

    if not os.path.exists(CUR_DIR_NAME):
        os.makedirs(CUR_DIR_NAME)

    return CUR_DIR_NAME

def prepare_out_log_file(CUR_DIR_NAME):
    """prepare_out_log_file(str) -> str

    Take path to current log directory and make path to current
    out log file.
    """
    # define current day log files
    LOG_FILE_OUT = os.path.join(CUR_DIR_NAME, str(date.today()) + '.out')

    return LOG_FILE_OUT

def prepare_err_log_file(CUR_DIR_NAME):
    """prepare_err_log_file(str) -> str

    Take path to current log directory and make path to current
    error log file.
    """
    LOG_FILE_ERR = os.path.join(CUR_DIR_NAME, str(date.today()) + '.err')

    return LOG_FILE_ERR