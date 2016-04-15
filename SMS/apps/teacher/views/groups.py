# -*- coding: utf-8 -*-
"""
views.groups

Module contains groups view functions.

:copyright: (c) 2015 by Sofia Kuzlo.
:license: BSD.
"""

from django.shortcuts import render

from ..models.teacher_subject import TeacherSubjects
from ..models.teacher_subject_group import TeacherSubjectGroups

from ...mainteacher.models.teachers import Teachers

from ...core.utils.access_control import access_control


@access_control('Викладач')
def subject_group_list(request):
    """Render groups list according to subjects."""
    teacher_id = request.session.get('teacher_id')
    # get current teacher
    teacher = Teachers.objects.get(id=teacher_id)
    # get all subjects of teacher
    teacher_subjects = TeacherSubjects.objects.filter(teacher_id=teacher_id)
    teacher_subject_groups = TeacherSubjectGroups.objects.all()

    context = {'teacher_subjects': teacher_subjects,
               'teacher_subject_groups': teacher_subject_groups,
               'teacher': teacher}

    return render(request, 'teacher/subject_group_list.html', context)
