# -*- coding: utf-8 -*-
"""
teacher.apps

Module contains class which is used for loading teacher signals
module in AppConfig.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

from django.apps import AppConfig


class TecherAppConfig(AppConfig):
    name = 'SMS.apps.teacher'

    def ready(self):
        from SMS.apps.teacher import signals
