# -*- coding: utf-8 -*-
"""
mainteacher.apps

Module contains class which is used for loading mainteacher signals
module in AppConfig.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

from django.apps import AppConfig


class MaintecherAppConfig(AppConfig):
    name = 'SMS.apps.mainteacher'

    def ready(self):
        from SMS.apps.mainteacher import signals
