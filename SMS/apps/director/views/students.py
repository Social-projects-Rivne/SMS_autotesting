# -*- coding: utf-8 -*-
"""
views.students

Module contains view functions for manage students.

:copyright: (c) 2015 by Sofia Kuzlo.
:license: BSD.
"""

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q

from ...teacher.models.groups import Groups
from ...teacher.models.students import Students
from ...mainteacher.models.teachers import Teachers

from ...core.utils.access_control import access_control


@access_control('Завуч')
def student_list(request, group_id):
    """Render students list of the group."""

    # get students of the current group
    students = Students.objects.filter(group_id=group_id, state=1)
    # select available groups for students transfer
    groups = _select_groups(request, group_id)
    # get current group name
    group_name = Groups.objects.get(id=group_id).name

    # ajax method for changing group and state of student
    if request.method == 'POST':
        # get data
        ajax_id = request.POST.get('id')
        ajax_group = request.POST.get('group')
        ajax_state = request.POST.get('state')

        # get current student
        student = Students.objects.get(id=ajax_id)

        if ajax_group:
            # change student group
            student.group_id = ajax_group

        if ajax_state:
            # change student state
            student.state = ajax_state

        # save changes
        student.save()

    context = {'students': students,
               'groups': groups,
               'group_id': group_id,
               'group_name': group_name}
    # render students listing page
    return render(request, 'director/student_list.html', context)


@access_control('Завуч')
def student_add(request, group_id):
    """Add student to the group."""

    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            # get student data from form
            name = request.POST.get('name')
            # create new student
            student = Students(group_id=group_id,
                               name=name)
            # save new student
            student.save()
            # redirect to students listing page
            return HttpResponseRedirect(reverse('student_list',
                                                kwargs={'group_id': group_id}))

    context = {'group_id': group_id}
    # render student form
    return render(request, 'director/student_form.html', context)


@access_control('Завуч')
def student_edit(request, group_id, student_id):
    """Edit student in the group."""

    # get current student
    student = Students.objects.get(id=student_id)
    # select available groups for students transfer
    groups = _select_groups(request, group_id)

    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            # change student data
            student.name = request.POST.get('name')
            student.group_id = request.POST.get('group')
            student.state = request.POST.get('state')
            # save changes
            student.save()
            # redirect to students listing page
            return HttpResponseRedirect(reverse('student_list',
                                                kwargs={'group_id': group_id}))

    context = {'student': student,
               'groups': groups,
               'group_id': group_id}
    # render student form
    return render(request, 'director/student_form.html', context)


@access_control('Завуч')
def student_delete(request, group_id, student_id):
    """Delete student from the group."""

    # get current student
    student = Students.objects.get(id=student_id)

    if request.method == 'POST':
        if request.POST.get('confirm_button') is not None:
            # remove student
            student.state = 0
            # save changes
            student.save()
        # redirect to  students listing page
        return HttpResponseRedirect(reverse('student_list',
                                            kwargs={'group_id': group_id}))

    context = {'instance': student,
               'group_id': group_id}
    # render delete confirmation window
    return render(request, 'director/confirmation.html', context)


def _select_groups(request, group_id):
    """Select available groups for students transfer depending on student's
       current group.
    """

    # get current user
    director = Teachers.objects.get(id=request.session.get('teacher_id'))

    # get current group
    current_group = Groups.objects.get(id=group_id)

    if (current_group.name.startswith('10') or
        current_group.name.startswith('11')):
        # available grades for students of grades 10-11
        current_grade = int(current_group.name[:2])
        next_grade = current_grade + 1
    else:
        # available grades for students of other grades
        current_grade = int(current_group.name[:1])
        next_grade = current_grade + 1

    # get available groups for students of the first grade
    if current_grade == 1:
        groups = (Groups.objects.filter(school_id=director.school.id, state=1)
                                .filter(Q(name__startswith=current_grade) |
                                        Q(name__startswith=next_grade))
                                .exclude(Q(name__startswith='10') |
                                         Q(name__startswith='11')))
    # get available groups for students of other grades
    else:
        groups = (Groups.objects.filter(school_id=director.school.id, state=1)
                                .filter(Q(name__startswith=current_grade) |
                                        Q(name__startswith=next_grade)))
    return groups
