# -*- coding: utf-8 -*-
"""
teacher.urls

This module contains url patterns for teacher.

:copyright: (c) 2015 by Sofia Kuzlo, Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from django.conf.urls import url


app_path = 'SMS.apps.teacher.views.'

urlpatterns = [
    # home page for teacher
    url(r'^$', app_path + 'groups.subject_group_list',
        name='subject_group_list'),

    # groups URLs
    url(r'^subject_group_list$',
        app_path + 'groups.subject_group_list', name='subject_group_list'),

    # journal URLs
    url(r'^class_journal/(?P<teacher_subject_group>\d+)/$',
        app_path + 'journal.marks_list', name='class_journal'),
    url(r'^class_journal_add_lesson/(?P<current_teacher_group>\d+)$',
        app_path + 'journal.add_lesson', name='class_journal_add_lesson'),
    url(r'^class_journal_update_lesson/(?P<group>\d+)/(?P<pk>\d+)$',
        app_path + 'journal.update_lesson',
        name='class_journal_update_lesson'),
    url(r'^class_journal_set_mark/(?P<current_teacher_group>\d+)/(?P<pk>\d+)/(?P<student>\d+)$',
        app_path + 'journal.set_mark', name='class_journal_set_mark'),
]
