# -*- coding: utf-8 -*-
"""
mainteacher.urls

This module contains url patterns for mainteacher application.

:copyright: (c) 2015 by Oleksii Omelchuk, Sofia Kuzlo and Pavlo Zhmak.
:license: BSD.
"""

from django.conf.urls import include, url


app_path = 'SMS.apps.mainteacher.views.'

urlpatterns = [
    # home page for main teacher page
    url(r'^$', app_path + 'schools.schools_list',
        name='schools_list'),

    # schools URLs
    url(r'^schools_list/$', app_path + 'schools.schools_list',
        name='schools_list'),
    url(r'^school_add/$', app_path + 'schools.school_add',
        name='school_add'),
    url(r'^school_update/(?P<pk>\d+)$', app_path + 'schools.school_update',
        name='school_update'),
    url(r'^school_delete/(?P<pk>\d+)$', app_path + 'schools.school_delete',
        name='school_delete'),
    url(r'^schools_list/school_search/$', app_path + 'schools.schools_search',
        name='school_search'),

    # teachers URLs
    url(r'^teachers_list/$', app_path + 'teachers.teachers_list',
        name='teachers_list'),
    url(r'^teacher_add/$', app_path + 'teachers.teacher_add',
        name='teacher_add'),
    url(r'^teacher_update/(?P<id>\d+)$', app_path + 'teachers.teacher_update',
        name='teacher_update'),
    url(r'^teacher_delete/(?P<id>\d+)$', app_path + 'teachers.teacher_delete',
        name='teacher_delete'),
    url(r'^teachers_list/teacher_search/$',
        app_path + 'teachers.teachers_search', name='teacher_search'),
]
