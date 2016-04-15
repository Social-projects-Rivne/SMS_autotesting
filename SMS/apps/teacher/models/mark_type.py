# -*- coding: utf-8 -*-
"""
models.mark_type

This module contains model class for mark types.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class MarkTypes(models.Model):
    """This class is used to handle data about mark types in DB."""

    character = models.CharField(max_length=60)

    class Meta:
        """This class gives some options (metadata) attached to the model."""

        db_table = 'MarkTypes'

    def __unicode__(self):
        return '%s' % self.character
