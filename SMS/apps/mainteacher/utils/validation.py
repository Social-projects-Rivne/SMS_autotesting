# -*- coding: utf-8 -*-
"""
utils.validation

Module contains Validate class for checking user's input data.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

import re


class Validate(object):
    """Class for checking input data with regular expressions ."""

    # regex patterns
    email_pattern = (r"^[a-z0-9]+([a-z0-9_\.-])+@[a-z0-9-]+\.([a-z]{2,4}\.)?"
                     r"[a-z]{2,4}$")
    login_pattern = r"^[A-Za-z0-9_]+$"
    school_name_pattern = (ur"^(НВК|НВК-ліцей|ЗОШ|Школа|Гімназія) "
                           ur"[№\'\"\-]{1}[А-Яа-яҐґЄєІіЇї0-9.,’\-\s]+[\'\"]?$")
    school_address_pattern = (ur"^вул. [А-Яа-яҐґЄєІіЇї’\-\s]+[\'\"]{0,2}, "
                              ur"\d+[а]?$")
    name_pattern = (ur"^[А-ЯҐЄІЇ]{1}[а-яґєії]+ [А-ЯҐЄІЇ]{1}[а-яґєії]+ "
                    ur"[А-ЯҐЄІЇ]{1}[а-яґєії]+$")

    def check_email(self, input_str):
        """Check email."""
        return re.match(self.email_pattern, input_str)

    def check_login(self, input_str):
        """Check login."""
        return re.match(self.login_pattern, input_str)

    def check_name(self, input_str):
        """Check cyrillic text."""
        return re.match(self.name_pattern, input_str, re.UNICODE)

    def check_school_name(self, input_str):
        """Check if school name was inserted correctly."""
        return re.match(self.school_name_pattern, input_str, re.UNICODE)

    def check_school_address(self, input_str):
        """Check if school address was inserted correctly."""
        return re.match(self.school_address_pattern, input_str, re.UNICODE)
