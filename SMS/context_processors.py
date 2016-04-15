# -*- coding: utf-8 -*-
"""
SMS.context_processors

Module contains get_user_info function for making global LOGGED_USER
variable in all templates.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

from django.http import HttpRequest

from apps.mainteacher.models.teachers import Teachers


def get_user_info(request):
    """Make global template variable LOGGED_USER
    from session user_id.
    """
    try:
        logged_user = Teachers.objects.get(pk=request.session['teacher_id'])
    except KeyError:
        logged_user = None

    return {'LOGGED_USER': logged_user}
