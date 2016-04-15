# -*- coding: utf-8 -*-
"""
views.groups

Module contains view functions for manage groups.

:copyright: (c) 2015 by Sofia Kuzlo.
:license: BSD.
"""

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q

from ...teacher.models.groups import Groups
from ...teacher.models.students import Students
from ...mainteacher.models.teachers import Teachers

from ...core.utils.access_control import access_control


@access_control('Завуч')
def group_list(request):
    """Render groups list of school."""

    # get current user
    director = Teachers.objects.get(id=request.session.get('teacher_id'))
    # get all groups of school
    groups = Groups.objects.filter(school_id=director.school.id, state=1)

    context = {'groups': groups}
    # render groups listing page
    return render(request, 'director/group_list.html', context)


@access_control('Завуч')
def group_add(request):
    """Add group to school."""

    # get current user
    director = Teachers.objects.get(id=request.session.get('teacher_id'))
    # get teachers available as head of the group
    teachers = Teachers.objects.filter(school_id=director.school.id,
                                       groups__teacher=None,
                                       role=3,
                                       state=1)

    # ajax checking if group name is valid
    if request.is_ajax() and request.method == 'POST':
        return _group_name_validate(request)

    elif request.method == 'POST':
        if request.POST.get('add_button') is not None:
            # get data from form
            name = request.POST.get('name')
            teacher_id = request.POST.get('teacher')
            # create new group
            group = Groups(school_id=director.school.id,
                           name=name,
                           teacher_id=teacher_id)
            # save new group
            group.save()
            # redirect to groups listing page
            return HttpResponseRedirect(reverse('group_list'))

    context = {'teachers': teachers}
    # render group form
    return render(request, 'director/group_form.html', context)


@access_control('Завуч')
def group_edit(request, group_id):
    """Edit group in school."""

    # get current group
    group = Groups.objects.get(id=group_id)
    # get teachers available as head of the group
    teachers = _manage_head_teacher(request, group_id)

    # ajax checking if group name is valid
    if request.is_ajax() and request.method == 'POST':
        return _group_name_validate(request)

    elif request.method == 'POST':
        if request.POST.get('add_button') is not None:
            # change group data
            group.name = request.POST.get('name')
            group.teacher_id = request.POST.get('teacher')
            # save changes
            group.save()
            # redirect to groups listing page
            return HttpResponseRedirect(reverse('group_list'))

    context = {'group': group,
               'teachers': teachers}
    # render group form
    return render(request, 'director/group_form.html', context)


@access_control('Завуч')
def group_delete(request, group_id):
    """Delete group from school."""

    # get current group
    group = Groups.objects.get(id=group_id)
    # get students of the group
    students = Students.objects.filter(group=group_id, state=1)
    # define dictionary for errors
    errors = {}
    # create warning message in case the group is not empty
    if students:
        errors['students'] = u"Поточний клас не порожній і не може бути \
                               видаленим. Для його видалення, будь ласка, \
                               переведіть учнів до іншого класу."

    if request.method == 'POST':
        if request.POST.get('confirm_button') is not None:

            if not errors:
                # remove current group
                group.state = 0
                # remove head of the group
                group.teacher = None
                group.save()

        # redirect to groups listing page
        return HttpResponseRedirect(reverse('group_list'))

    context = {'instance': group,
               'errors': errors}
    # render delete confirmation window
    return render(request, 'director/confirmation.html', context)


def _group_name_validate(request):
    """Check if group name is valid"""

    # get current user
    director = Teachers.objects.get(id=request.session.get('teacher_id'))
    # get filled name from form
    ajax_group_name = request.POST.get('value')
    # get groups with this name
    groups = Groups.objects.filter(name=ajax_group_name,
                                   school_id=director.school.id,
                                   state=1)
    # check if group with this name exists and return corresponding status
    if groups:
        return JsonResponse({'status': 'Group with this name already \
                             exists'}, status=400)
    else:
        return JsonResponse({'status': 'Group name is valid'}, status=200)


def _manage_head_teacher(request, group_id):
    """Get teachers available as head of the group."""

    # get current group
    group = Groups.objects.get(id=group_id)
    # get current user
    director = Teachers.objects.get(id=request.session.get('teacher_id'))

    # define current head of group
    current_teacher = None
    # get current head of the group if exists
    if group.teacher:
        current_teacher = Teachers.objects.get(id=group.teacher.id)

    # get teachers available as head of the group
    if current_teacher:
        # containing current head of group
        teachers = (Teachers.objects.filter(school_id=director.school.id,
                                            role=3,
                                            state=1)
                                    .filter(Q(groups__teacher=None) |
                                            Q(id=group.teacher.id)))
    else:
        teachers = Teachers.objects.filter(school_id=director.school.id,
                                           groups__teacher=None,
                                           role=3,
                                           state=1)
    return teachers
