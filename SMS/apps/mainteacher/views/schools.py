# -*- coding: utf-8 -*-
"""
views.schools

Module contains next view functions:
    schools_list,
    school_add,
    school_update,
    school_delete,
    schools_search.

These functions are used for managing schools by main-teacher.

:copyright: (c) 2015 by Oleksii Omelchuk and Pavlo Zhmak.
:license: BSD.
"""

import json

from django.db.models import Q
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from ..models.schools import Schools
from ..models.teachers import Teachers

from ..utils.validation_school import school_validate_form
from ..utils.manage_teachers import set_default_role, set_director_role

from ...core.utils.access_control import access_control


@access_control('Головний вчитель')
def schools_list(request):
    """Return list of all schools."""
    teacher = Teachers.objects.get(id=request.session['teacher_id'])
    if request.method == 'POST':
        try:
            ajax_pk = request.POST.get('id')
            ajax_director_id = request.POST.get('director')
            # get appropriate school
            school = Schools.objects.get(id=ajax_pk)

            # change role for previous director
            if school.director_id:
                set_default_role(school.director_id)

            # change director
            school.director_id = ajax_director_id
            # save changes
            school.save()

            # change role for new director
            set_director_role(ajax_director_id)

        except ObjectDoesNotExist:
            return JsonResponse({'status': u'Не вдалася зміна посади'})

    schools = Schools.objects.filter(state=1)
    # show all members of current school
    for school in schools:
        school.members = Teachers.objects.filter(school=school, state=1)

    return render(request, 'mainteacher/school_list.html',
                  {'schools': schools,
                   'teacher': teacher})


@access_control('Головний вчитель')
def school_add(request):
    """School add method.

    Function renders school add form.
    Whether form was posted - validate data and saves it to DB.
    """

    # ajax checking if school name is valid
    if request.is_ajax() and request.method == 'POST':
        return _school_name_validate(request)

    elif request.method == 'POST':
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # define errors and data collections
            errors = {}
            data = {}

            school_validate_form(request, errors, data)

            # save school
            if not errors:
                # create school instance
                school = Schools(name=data['name'], address=data['address'])
                # save instance to DB
                school.save()

                # redirect to shools list
                return HttpResponseRedirect(reverse('schools_list'))
            else:
                return render(request, 'mainteacher/school_form.html',
                              {'errors': errors})

    return render(request, 'mainteacher/school_form.html')


@access_control('Головний вчитель')
def school_update(request, pk):
    """School update method.

    Function renders school update form.
    Whether form was posted - validate data and saves it to DB.
    """
    school = Schools.objects.get(id=pk)
    # show all teachers of current school
    school.members = Teachers.objects.filter(school=school, state=1)

    # ajax checking if school name is valid
    if request.is_ajax() and request.method == 'POST':
        return _school_name_validate(request)

    elif request.method == 'POST':
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # define errors and data collections
            errors = {}
            data = {}

            school_validate_form(request, errors, data)

            if not errors:
                # whether director was changed set default role for previous
                if school.director_id != data['director_id']:
                    set_default_role(school.director_id)

                # change school fileds
                for key in data:
                    school.__dict__[key] = data[key]
                school.save()

                # change role for new director
                set_director_role(school.director_id)

                # redirect to shools list
                return HttpResponseRedirect(reverse('schools_list'))
            else:
                return render(request, 'mainteacher/school_form.html',
                              {'school': school,
                               'errors': errors})
    return render(request, 'mainteacher/school_form.html',
                  {'school': school})


@access_control('Головний вчитель')
def school_delete(request, pk):
    """School delete method.

    Return delete-confirmation modal form.
    Whether form was posted - delete appropriate school.
    """
    school = Schools.objects.get(id=pk)

    if request.method == 'POST':
        # was form add button clicked?
        if request.POST.get('confirm_button') is not None:
            # get and delete school
            school.state = 0
            school.save()

            # change role for director
            if school.director_id:
                set_default_role(school.director_id)

        return HttpResponseRedirect(reverse('schools_list'))

    return render(request, 'mainteacher/confirmation.html',
                  {'instance': school})


@access_control('Головний вчитель')
def schools_search(request):
    """Return formatted list with searched school objects."""
    search_text = request.GET.get('search_text')
    schools = Schools.objects.filter(Q(name__contains=search_text) |
                                     Q(address__contains=search_text))

    data = []
    for school in schools:
        context = {}
        context['id'] = school.id
        context['name'] = school.name
        context['address'] = school.address
        if school.director:
            context['director'] = school.director.name
        data.append(context)

    return HttpResponse(json.dumps(data), 'application/json')


def _school_name_validate(request):
    """Check if group name is valid"""

    # get filled name from form
    ajax_school_name = request.POST.get('value')
    # get schools with this name
    schools = Schools.objects.filter(name=ajax_school_name, state=1)
    # check if group with this name exists and return corresponding status
    if schools:
        return JsonResponse({'status': 'School with this name already \
                             exists'}, status=400)
    else:
        return JsonResponse({'status': 'School name is valid'}, status=200)
