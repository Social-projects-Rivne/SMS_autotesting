# -*- coding: utf-8 -*-
"""
utils.hash_passwd

These functions work with password hash.

:copyright: (c) 2015 by Zhmak Pavlo.
:license: BSD.
"""

import uuid
import hashlib


def hash_password(password):
    """Hashing password and add salt."""
    salt = uuid.uuid4().hex
    return {'hash': (hashlib.sha512(salt.encode() +
                                    password.encode()).hexdigest()),
            'salt': salt}


def check_password(hashed_password, user_password, salt):
    """Check password by hash."""
    return (hashed_password == hashlib.sha512(salt.encode() +
                                              user_password
                                              .encode()).hexdigest())
