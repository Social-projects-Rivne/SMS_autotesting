# -*- coding: utf-8 -*-
"""
views.teachers

Module contains next view functions:
    teachers_list,
    teacher_add,
    teacher_update,
    teacher_delete,
    teachers_search.

These functions are used for managing teachers by main-teacher.

:copyright: (c) 2015 by Sofia Kuzlo and Oleksii Omelchuk.
:license: BSD.
"""

import thread
import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.db.models import Q

from ..models.teachers import Teachers
from ..models.schools import Schools
from ..models.roles import Roles
from ..forms import TeacherForm

from ..utils.pass_generate import random_pass
from ..utils.manage_teachers import ajax_teacher_managing, fire_school_director
from ..utils.email import pass_sending

from ...core.utils.hash_passwd import hash_password
from ...core.utils.access_control import access_control


@access_control('Головний вчитель')
def teachers_list(request):
    """Render teachers list."""
    if request.method == 'POST':
        ajax_teacher_managing(request)

    teacher = Teachers.objects.get(id=request.session['teacher_id'])
    # get all teachers (except main teachers)
    teachers = Teachers.objects.filter(state=1).exclude(role=1)
    # get all roles (except main teachers)
    roles = Roles.objects.filter().exclude(id=1)
    # get all schools
    schools = Schools.objects.filter(state=1)
    context = {'teachers': teachers,
               'roles': roles,
               'schools': schools,
               'teacher': teacher}

    return render(request, 'mainteacher/teacher_list.html', context)


@access_control('Головний вчитель')
def teacher_add(request):
    """Add teacher to db."""
    # get all schools
    schools = Schools.objects.filter(state=1)
    context = {'schools': schools}

    if request.method == "POST":
        form = TeacherForm(request.POST)

        value = request.POST.get('value')

        if request.POST.get('field') == 'login':
            # check login field on unique
            if len(Teachers.objects.filter(
                    login=value,
                    state=1)) > 0:
                return JsonResponse({'field': 'login',
                                     'status': 'Виберіть інший логін.'},
                                    status=400)
            else:
                return JsonResponse({'status': 'valid.'}, status=200)

        if request.POST.get('field') == 'email':
            # check email field on unique
            if len(Teachers.objects.filter(
                    email=value,
                    state=1)) > 0:
                return JsonResponse(
                    {'field': 'email',
                     'status': 'Виберіть іншу електронну пошту.'}, status=400)
            else:
                return JsonResponse({'status': 'valid.'}, status=200)

        if form.is_valid():
            # create the new teacher instance
            new_teacher = form.save(commit=False)
            # define password for new teacher and save instance
            new_teacher.role_id = 3

            password = random_pass()
            hashed_password = hash_password(password)
            new_teacher.password = hashed_password['hash']
            new_teacher.salt = hashed_password['salt']
            new_teacher.save()

            # send greeting message with personal information
            thread.start_new_thread(pass_sending, (
                new_teacher.name, new_teacher.email,
                new_teacher.login, password))
            # redirect to teachers list page
            return HttpResponseRedirect(reverse('teachers_list'))
        else:
            errors = form.errors
            return render(request, 'mainteacher/teacher_form.html',
                          {'schools': schools, 'errors': errors})

    return render(request, 'mainteacher/teacher_form.html', context)


@access_control('Головний вчитель')
def teacher_update(request, id):
    """Update teacher in db."""
    # creating a form to change an existing teacher
    teacher = Teachers.objects.get(id=id)

    # get all schools
    schools = Schools.objects.filter(state=1)
    context = {'teacher': teacher, 'schools': schools}

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            current_teacher = form.save(commit=False)
            # whether teacher's school was changed
            if current_teacher.school != teacher.school_id or \
                    current_teacher.school is None:
                # whether use is director set default role
                if current_teacher.role_id == 2:
                    current_teacher.role_id = 3
                    fire_school_director(current_teacher.id)
            current_teacher.save()
            # redirect to teachers list page
            return HttpResponseRedirect(reverse('teachers_list'))
        else:
            errors = form.errors
            return render(request, 'mainteacher/teacher_form.html',
                          {'schools': schools, 'errors': errors})
    return render(request, 'mainteacher/teacher_form.html', context)


@access_control('Головний вчитель')
def teacher_delete(request, id):
    """Delete teacher from db."""
    # get teacher to delete
    teacher = Teachers.objects.get(id=id)

    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('confirm_button') is not None:
            # whether user was a director of school clear school's director
            if teacher.role_id == 2:
                fire_school_director(teacher.id)
            # delete teacher
            teacher.state = 0
            teacher.save()

        # redirect to teachers list page
        return HttpResponseRedirect(reverse('teachers_list'))

    return render(request, 'mainteacher/confirmation.html',
                  {'instance': teacher})


@access_control('Головний вчитель')
def teachers_search(request):
    """Return formatted list with searched teacher objects."""
    search_text = request.GET.get('search_text')
    teachers = Teachers.objects.filter(Q(name__contains=search_text) |
                                       Q(login__contains=search_text) |
                                       Q(email__contains=search_text))

    data = []
    for teacher in teachers:
        context = {}
        context['id'] = teacher.id
        context['name'] = teacher.name
        context['login'] = teacher.login
        context['email'] = teacher.email
        context['password'] = teacher.password
        data.append(context)

    return HttpResponse(json.dumps(data), 'application/json')
