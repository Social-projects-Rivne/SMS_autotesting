# -*- coding: utf-8 -*-
"""
utils.pass_generate

Module contains random_pass function.

:copyright: (c) 2015 by Oleksii Omelchuk and Sofia Kuzlo.
:license: BSD.
"""

from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase, digits


def random_pass():
    """random_pass() -> str

    Generate random password which contains lowercase and uppercase
    letters, digits and special symbols. It's length is 8 symbols.
    """
    # create sequence of possible symbols
    possible_symbols = ascii_lowercase + ascii_uppercase + digits + '@#$%'

    # create sequence of required symbols
    required_symbols = (choice(ascii_lowercase) +
                        choice(ascii_uppercase) +
                        choice(digits) +
                        choice('@#$%'))

    # provide password with required symbols
    password = required_symbols

    # add random symbols to password from sequence of possible symbols
    for counter in range(4):
        password += choice(possible_symbols)

    # shuffle symbols in password
    password = list(password)
    shuffle(password)

    return ''.join(password)
