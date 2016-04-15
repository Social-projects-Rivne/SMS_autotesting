# -*- coding: utf-8 -*-
"""
views.login

These functions are used for sign in user into system and logout.

:copyright: (c) 2015 by Zhmak Pavlo.
:license: BSD.
"""

import logging

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from ...mainteacher.utils.validation import Validate
from ...mainteacher.models.teachers import Teachers

from ...core.utils.hash_passwd import check_password


logger = logging.getLogger(__name__)


def sign_in(request):
    """Return usert page by username and password if
    exist in DB."""

    context = {}

    if request.method == 'POST':
        user = list()
        # data from login form
        userlogin = request.POST.get('inputUsername').strip()
        password = request.POST.get('inputPassword').strip()
        # validate login and password
        validate = Validate()
        if validate.check_login(userlogin):

            user = Teachers.objects.filter(login=userlogin,
                                           state=1)
            # if current user exist in system
            if user:
                # check hashed password
                if user[0].salt is not None:
                    if (not check_password(user[0].password,
                                           password, user[0].salt)):
                        return render(request, 'core/login.html', context)
                # if password not hashed
                else:
                    user = Teachers.objects.filter(login=userlogin,
                                                   password=password,
                                                   state=1)

        if len(user) > 0:
            # get first user with current name and password
            user = user[0]

            # who is mainteacher?
            mainteachers = Teachers.objects.filter(
                role__role_name='Головний вчитель')
            directors = Teachers.objects.filter(
                role__role_name='Завуч')

            request.session['teacher_id'] = user.id
            request.session['teacher_role'] = user.role.role_name

            # write this event into the log
            logger.info(u'%s-%s logged on to the system', user.role.role_name,
                        user.name,)

            if user in mainteachers:
                return HttpResponseRedirect(reverse('schools_list'))
            if user in directors:
                return HttpResponseRedirect(reverse('group_list'))
            else:
                return HttpResponseRedirect(reverse('subject_group_list'))

        else:
            logger.warning('Failed authentication attempt for %s', userlogin)

            return render(request, 'core/login.html', context)

    context['correct'] = True
    return render(request, 'core/login.html', context)


def logout(request):
    """Clear session data and return on page for sign in"""

    logged_user = Teachers.objects.get(pk=request.session['teacher_id'])

    logger.info(u'User "%s" logged out', logged_user.name)
    for key in request.session.keys():
        del request.session[key]

    return HttpResponseRedirect(reverse('login'))
