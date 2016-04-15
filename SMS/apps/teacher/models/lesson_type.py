# -*- coding: utf-8 -*-
"""
models.lesson_type

This module contains model class for lesson types.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class LessonTypes(models.Model):
    """This class is used to handle data about lesson types in DB."""

    character = models.CharField(max_length=60)

    class Meta:
        """This class gives some options (metadata) attached to the model."""

        db_table = 'LessonTypes'

    def __unicode__(self):
        return '%s' % self.character
