# -*- coding: utf-8 -*-

from django.conf.urls import include, url


app_path = 'SMS.apps.core.views.'

urlpatterns = [
    url(r'^$',  app_path + 'login.sign_in'),
    url(r'^login/$',  app_path + 'login.sign_in', name='login'),
    url(r'^logout/$',  app_path + 'login.logout', name='logout'),

    # Profile URLs
    url(r'^profile/$',
        app_path + 'profile.profile_page', name='profile'),
    url(r'^profile_edit/$',
        app_path + 'profile.profile_edit', name='profile_edit'),
    url(r'^profile_edit_password/$',
        app_path + 'profile.profile_edit_password',
        name='profile_edit_password'),

    url(r'^img_upload/$',
        app_path + 'profile.img_upload', name='img_upload'),
]
