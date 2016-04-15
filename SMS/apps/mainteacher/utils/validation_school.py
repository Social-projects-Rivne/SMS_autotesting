# -*- coding: utf-8 -*-
"""
utils.validation_school

Module contains school_validate_form function.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

from .validation import Validate
from ..models.teachers import Teachers


def school_validate_form(request, errors, data):
    """school_validate_form(request, dict, dict) -> dict, dict

    Take request with POST method and two collections.
    After validation, method returns two collections with errors and
    data. If validation was successfully finished errors dict will be
    empty.
    """
    validate = Validate()

    # validate user inputs
    name = request.POST.get('name', '').strip()
    if not name or not validate.check_school_name(name):
        errors['name'] = u"Назва школи введена некоректно"
    else:
        data['name'] = name

    address = request.POST.get('address', '').strip()
    if not address or not validate.check_school_address(address):
        errors['address'] = u"Адресса школи введена некоректно"
    else:
        data['address'] = address

    director = request.POST.get('director', '')
    if director:
        # check if a chosen director is exists
        directors = Teachers.objects.filter(id=director)
        if len(directors) != 1:
            errors['director'] = u"Некоректно вибраний директор"
        else:
            data['director_id'] = directors[0].id
    else:
        data['director_id'] = None

    return errors, data
