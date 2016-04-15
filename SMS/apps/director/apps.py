# -*- coding: utf-8 -*-

from django.apps import AppConfig


class DirectorAppConfig(AppConfig):
    name = 'SMS.apps.director'

    def ready(self):
        from SMS.apps.director import signals
