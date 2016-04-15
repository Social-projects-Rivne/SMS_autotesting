# -*- coding: utf-8 -*-
"""
utils.manage_teachers

Module contains four functions which is used in main-teacher's
functional:
    set_default_role()
    set_director_role()
    fire_school_director()
    ajax_teacher_managing()

For more information read doc-stings in particular function.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

from ..models.teachers import Teachers
from ..models.schools import Schools


def set_default_role(pk):
    """set_default_role(int) -> request to DB

    Get director_id and change role of director to teacher.
    """
    if pk:
        previous_director = Teachers.objects.get(id=pk)
        previous_director.role_id = 3
        previous_director.save()


def set_director_role(pk):
    """set_director_role(int) -> request to DB

    Get teacher ID and change role to director.
    """
    if pk:
        new_director = Teachers.objects.get(id=pk)
        new_director.role_id = 2
        new_director.save()


def fire_school_director(pk):
    """fire_school_director(int) -> request to DB

    Get school director id and remove director from it.
    """
    if pk:
        school = Schools.objects.get(director_id=pk)
        school.director_id = None
        school.save()


def ajax_teacher_managing(request):
    """ajax_teacher_managing(request) -> requests to DB

    Method handles changes teachers role, school director position,
    relocations teacher to other school.
    Method checks for there will be one director in a school.

    Note: it needs refactoring.
    """
    # define variables for data of request
    ajax_pk = request.POST.get('id')
    ajax_school = request.POST.get('school')
    ajax_role = request.POST.get('role')
    # get appropriate teacher
    teacher = Teachers.objects.get(id=ajax_pk)
    # get school of teacher
    if teacher.school_id:
        school = Schools.objects.get(id=teacher.school_id)

    # check whether teacher's role was changed
    if ajax_role:
        # change school director.
        # if we want to assign teacher's role as director
        if ajax_role == '2':
            # get previous director(s)
            prev_directors = Teachers.objects.filter(school_id=school.id,
                                                     role_id=2)
            # restore all previous school's directors
            for member in prev_directors:
                member.role_id = 3
                member.save()
            # assign current teacher as director
            school.director_id = teacher.id
        # if we want to fire current director
        elif ajax_role == '3' and teacher.role_id == 2:
            school.director_id = None
        school.save()
        # set to teacher chosen role
        teacher.role_id = ajax_role

    # check whether teacher's school was changed
    if ajax_school:
        if ajax_school == '0':
            ajax_school = None
            # if teacher has director role
        if teacher.role_id == 2:
            # set him/his default role
            teacher.role_id = 3
            # remove school's director position
            school.director_id = None
            school.save()
        # assign teacher to new school
        teacher.school_id = ajax_school
    # save changes
    teacher.save()
