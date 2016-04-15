# -*- coding: utf-8 -*-
"""
utils.set_base_template_variable

This module contains funсtion which allow to assign appropriate
application base_template.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

from django.contrib.sessions.models import Session

from ...mainteacher.models.teachers import Teachers


def set_base_template_variable(request):
    """set_base_template_variable(request) -> str

    Check user role and set base_template_variable for profile template.
    """
    teacher = Teachers.objects.get(id=request.session['teacher_id'])

    if u'Головний вчитель' == request.session['teacher_role']:
        base_template_variable = 'mainteacher/base_mainteacher.html'
    elif u'Завуч' == request.session['teacher_role']:
        base_template_variable = 'director/base_director.html'
    elif u'Викладач' == request.session['teacher_role']:
        base_template_variable = 'teacher/base_teacher.html'

    return base_template_variable
