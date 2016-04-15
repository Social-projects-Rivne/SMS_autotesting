# -*- coding: utf-8 -*-
"""
utils.checking_functions

Module contains function for checking if lesson is editable depending of it's
date.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

from datetime import date


def check_editable(check_field):
    """check_editable(date) -> boolean

    Checking editable for inserted date.
    """
    if check_field == date.today():
        editable = True
    else:
        editable = False
    return editable
