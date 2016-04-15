# -*- coding: utf-8 -*-
"""
SMS.urls

This module contains url patterns for SMS project.

:copyright: (c) 2015 by Sofia Kuzlo, Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('SMS.apps.core.urls')),
    url(r'^core/', include('SMS.apps.core.urls')),
    url(r'^mainteacher/', include('SMS.apps.mainteacher.urls')),
    url(r'^teacher/', include('SMS.apps.teacher.urls')),
    url(r'^director/', include('SMS.apps.director.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
