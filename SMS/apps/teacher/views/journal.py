# -*- coding: utf-8 -*-
"""
views.journal

Module contains journal view functions.

:copyright: (c) 2015 by Oleksii Omelchuk and Pavlo Zhmak.
:license: BSD.
"""

import datetime

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from ..models.teacher_subject_group import TeacherSubjectGroups
from ..models.journal import Journal
from ..models.lesson import Lessons
from ..models.students import Students
from ..models.mark_type import MarkTypes
from ..models.lesson_type import LessonTypes

from ..utils.checking_functions import check_editable

from ...mainteacher.models.subject import Subjects

from ...core.utils.access_control import access_control


@access_control('Викладач')
def marks_list(request, teacher_subject_group):
    """Return journal class page."""
    # get current teacher_subject_group
    teacher_subject_group = TeacherSubjectGroups.objects.get(
        id=teacher_subject_group)

    # data for template
    lessons = Lessons.objects.filter(
        teacher_subject_group_id=teacher_subject_group.id)
    journals = Journal.objects.all()
    students = Students.objects.filter(group=teacher_subject_group.group)
    subjects = Subjects.objects.all()

    # get current group's subjects
    group_subjects = TeacherSubjectGroups.objects.filter(
        teacher_subject__teacher=teacher_subject_group.teacher_subject.teacher,
        group=teacher_subject_group.group)

    context = {'lessons': lessons,
               'journals': journals,
               'students': students,
               'subjects': subjects,
               'current_teacher_group': teacher_subject_group,
               'group_subjects': group_subjects,
               'teacher': teacher_subject_group.teacher_subject.teacher}

    return render(request, 'teacher/journal.html', context)


@access_control('Викладач')
def add_lesson(request, current_teacher_group):
    """Return journal add lesson page."""
    lesson_types = LessonTypes.objects.all()

    if request.method == 'POST':

        teacher_group = TeacherSubjectGroups.objects.get(
            id=current_teacher_group)

        # get data from form
        date = request.POST.get('date').strip()
        # if user didn't set date - use current date
        if not date:
            date = datetime.date.today()
        lesson_type = request.POST.get('lesson_type')
        topic = request.POST.get('topic')
        homework = request.POST.get('homework')

        # create new lesson
        lesson = Lessons(date=date,
                         teacher_subject_group=teacher_group,
                         topic=topic,
                         lesson_type_id=lesson_type,
                         homework=homework)
        lesson.save()

        # redirect to page with journal
        return HttpResponseRedirect(reverse('class_journal',
                                            kwargs={'teacher_subject_group':
                                                    current_teacher_group}))
    return render(request, 'teacher/journal_form_lesson.html',
                  {'lesson_types': lesson_types})


@access_control('Викладач')
def update_lesson(request, group, pk):
    """Return page for update lesson."""
    # get lesson by id
    lesson = Lessons.objects.get(id=pk)

    if request.method == 'GET':
        lesson_types = LessonTypes.objects.all()
        context = {'lesson': lesson,
                   'lesson_types': lesson_types,
                   'editable': check_editable(lesson.date)}
        return render(request, 'teacher/journal_form_lesson.html', context)

    if request.method == 'POST':
        # change lesson
        lesson.topic = request.POST.get('topic')
        lesson.homework = request.POST.get('homework')
        lesson.lesson_type_id = request.POST.get('lesson_type')
        # save changes into db
        lesson.save()

        return HttpResponseRedirect(reverse('class_journal',
            kwargs={'teacher_subject_group': group}))


@access_control('Викладач')
def set_mark(request, current_teacher_group, pk, student):
    """set_mark(request, int, int, int) -> render page or request to DB

    Return set_mark form template.
    Take request, current_teacher_group_id, lesson_id, student_id.
    If journal data exist - update it.
    """
    redirect_link = reverse('class_journal', kwargs={'teacher_subject_group':
                                                     current_teacher_group})
    mark_types = MarkTypes.objects.all().exclude(id=3)
    lesson = Lessons.objects.get(id=pk)

    context = {'mark_types': mark_types,
               'editable': check_editable(lesson.date),
               'is_control': lesson.is_control()}

    # check if journal for current lesson/student exist
    journals = Journal.objects.filter(lesson_id=pk, student_id=student)
    if journals:
        journal = journals[0]
        context['journal'] = journal

    if request.method == 'POST':
        # get data from form
        mark = request.POST.get('mark')
        mark_type = request.POST.get('mark_type')
        if not mark_type:
            mark_type = '1'
        comment = request.POST.get('comment')
        if not comment:
            comment = ''
        lesson = Lessons.objects.get(id=pk)

        # logic for set absent for studetns
        # it doesn't look perfect, but it works:

        # if teacher didn't set mark - redirect to before page
        if mark == '' and mark_type == '1':
            return HttpResponseRedirect(redirect_link)
        # if student is absent and it's not control lesson set None mark
        elif ((mark_type == '2' or mark_type == '3') and
                not lesson.is_control()):
            mark = None
        # if student is absent and it's control lesson, and teacher
        # cassually set mark - we able to remove it out
        elif (mark == '' and (mark_type == '2' or mark_type == '3') and
                lesson.is_control()):
            mark = None
        # if we want to set mark for absent student control
        try:
            if (journal and (mark_type == '2' or mark_type == '3') and
                    lesson.is_control()):
                mark = mark
            # if student was absent at control lesson we able to set
            # mark later
            elif journal.marktype_id > 1 and lesson.is_control():
                mark = mark
                mark_type = journal.marktype_id
        except NameError:
            pass

        if 'journal' in context:
            # update journal
            journal.mark = mark
            journal.marktype_id = mark_type
            journal.comment = comment
        else:
            # fill data for new journal
            journal = Journal(
                student=Students.objects.get(id=student),
                lesson=lesson,
                mark=mark,
                marktype_id=mark_type,
                comment=comment)
        journal.save()

        return HttpResponseRedirect(redirect_link)

    return render(request, 'teacher/journal_set_mark.html', context)
