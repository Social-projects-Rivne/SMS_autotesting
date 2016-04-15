# -*- coding: utf-8 -*-

from django.conf.urls import include, url

app_path = 'SMS.apps.director.views.'

urlpatterns = [
    # home page for director
    url(r'^$', app_path + 'groups.group_list', name='group_list'),

    # groups URLs
    url(r'^group_list/$', app_path + 'groups.group_list', name='group_list'),
    url(r'^group_add/$', app_path + 'groups.group_add', name='group_add'),
    url(r'^group_edit/(?P<group_id>\d+)$', app_path + 'groups.group_edit',
        name='group_edit'),
    url(r'^group_delete/(?P<group_id>\d+)$', app_path + 'groups.group_delete',
        name='group_delete'),

    # students URLs
    url(r'^student_list/(?P<group_id>\d+)$', app_path + 'students.student_list',
        name='student_list'),
    url(r'^student_add/(?P<group_id>\d+)$', app_path + 'students.student_add',
        name='student_add'),
    url(r'^student_edit/(?P<group_id>\d+)/(?P<student_id>\d+)$', app_path +
        'students.student_edit', name='student_edit'),
    url(r'^student_delete/(?P<group_id>\d+)/(?P<student_id>\d+)$', app_path +
        'students.student_delete', name='student_delete'),

    # teachers URLs
    url(r'^manage_teachers/$', app_path + 'teachers.teacher_subjects',
        name='manage_teachers'),

    url(r'^add_teacher_subject/(?P<teacher_id>\d+)$',
        app_path + 'teachers.add_teacher_subject',
        name='add_teacher_subject'),
    url(r'^delete_teacher_subject/(?P<teacher_subject_id>\d+)$',
        app_path + 'teachers.delete_teacher_subject',
        name='delete_teacher_subject'),

    url(r'^add_teacher_subject_group/(?P<teacher_subject_id>\d+)$',
        app_path + 'teachers.add_teacher_subject_group',
        name='add_teacher_subject_group'),
    url(r'^delete_teacher_subject_group/(?P<teacher_subject_group_id>\d+)$',
        app_path + 'teachers.delete_teacher_subject_group',
        name='delete_teacher_subject_group'),
]
