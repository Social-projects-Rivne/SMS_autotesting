# -*- coding: utf-8 -*-
"""
views.teachers

Module contains view functions for manage teachers.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse

from ...mainteacher.models.subject import Subjects
from ...mainteacher.models.teachers import Teachers

from ...teacher.models.groups import Groups
from ...teacher.models.teacher_subject import TeacherSubjects
from ...teacher.models.teacher_subject_group import TeacherSubjectGroups

from ...core.utils.access_control import access_control


@access_control('Завуч')
def teacher_subjects(request):
    """Teachers subjects groups list."""

    # get current user's data
    director = Teachers.objects.get(pk=request.session.get('teacher_id'))

    # get all teachers of director's school
    teachers = Teachers.objects.filter(state=1, school_id=director.school.id,
                                       role_id=3)

    # make list of teachers with assigned subjects and classes
    teachers_list = []
    for teacher in teachers:
        # get assigned subjects
        teacher_subjects = TeacherSubjects.objects.filter(
            teacher_id=teacher.pk)

        # set assigned groups for teacher subject
        subject_groups = []
        for teacher_subject in teacher_subjects:
            teacher_subject_groups = TeacherSubjectGroups.objects.filter(
                teacher_subject_id=teacher_subject.id).order_by('group')

            subject_groups.append({
                'id': teacher_subject.id,
                'subject': teacher_subject.subject.name,
                'groups': teacher_subject_groups,
            })

        teachers_list.append({
            'id': teacher.pk,
            'name': teacher.name,
            'subjects': subject_groups,
        })
    context = {'teachers': teachers_list, 'school_name': director.school.name}

    return render(request, 'director/manage_teachers.html', context)


@access_control('Завуч')
def add_teacher_subject(request, teacher_id):
    """Method for assign new subject for teacher."""

    subjects = Subjects.objects.all().order_by('name')

    context = {'list': subjects}

    # ajax checking of subject valid
    if request.is_ajax() and request.method == 'POST':
        ajax_subject_id = request.POST.get('value')
        teacher_subject = TeacherSubjects.objects.filter(teacher_id=teacher_id,
                                                         subject=ajax_subject_id)

        if len(teacher_subject) > 0:
            return JsonResponse({'status': 'Teacher has the same subject'},
                                status=400)
        else:
            return JsonResponse({'status': 'Subject is valid'}, status=200)

    # set new subject for teacher
    elif request.method == 'POST':
        subject_id = request.POST.get('manage_teachers_select')

        teacher_subject = TeacherSubjects(subject_id=subject_id,
                                          teacher_id=teacher_id)
        teacher_subject.save()
        return HttpResponseRedirect(reverse('manage_teachers'))

    return render(request, 'director/add_subject_group_form.html', context)


@access_control('Завуч')
def delete_teacher_subject(request, teacher_subject_id):
    """Method for delete teacher's subject."""

    teacher_subject = TeacherSubjects.objects.get(pk=teacher_subject_id)

    # if at least one group is assigned to teacher_subject -
    # return warning message
    teacher_subject_groups = TeacherSubjectGroups.objects.filter(
        teacher_subject_id=teacher_subject_id)
    removable_error = False
    if len(teacher_subject_groups) >= 1:
        removable_error = True

    context = {'teacher_subject': teacher_subject,
               'removable_error': removable_error}

    if request.method == 'POST':
        teacher_subject.delete()
        return HttpResponseRedirect(reverse('manage_teachers'))

    return render(request, 'director/confirm_delete.html', context)


@access_control('Завуч')
def add_teacher_subject_group(request, teacher_subject_id):
    """Method for assign new group for teacher_subject."""

   # get current user's data
    director = Teachers.objects.get(pk=request.session.get('teacher_id'))

    current_teacher_subject = TeacherSubjects.objects.get(
        pk=teacher_subject_id)
    groups = Groups.objects.filter(school_id=director.school.id)

    context = {'list': groups,
               'teacher_subject': current_teacher_subject}

    # ajax checking of group valid
    if request.is_ajax() and request.method == 'POST':
        ajax_group_id = request.POST.get('value')
        teacher_subject_groups = TeacherSubjectGroups.objects.filter(
            teacher_subject_id=teacher_subject_id, group_id=ajax_group_id)
        if len(teacher_subject_groups) > 0:
            return JsonResponse({'status': 'Teacher has the same group \
                                 for this subject'}, status=400)
        else:
            return JsonResponse({'status': 'Group is valid'}, status=200)

    # set new subject_group for teacher
    elif request.method == 'POST':
        group_id = request.POST.get('manage_teachers_select')

        teacher_subject_group = TeacherSubjectGroups(group_id=group_id,
                                         teacher_subject_id=teacher_subject_id)
        teacher_subject_group.save()
        return HttpResponseRedirect(reverse('manage_teachers'))

    return render(request, 'director/add_subject_group_form.html', context)


@access_control('Завуч')
def delete_teacher_subject_group(request, teacher_subject_group_id):
    """Method for delete teacher's subject_group."""

    teacher_subject_group = TeacherSubjectGroups.objects.get(
        pk=teacher_subject_group_id)

    context = {'teacher_subject_group': teacher_subject_group}

    if request.method == 'POST':
        teacher_subject_group.delete()
        return HttpResponseRedirect(reverse('manage_teachers'))

    return render(request, 'director/confirm_delete.html', context)
