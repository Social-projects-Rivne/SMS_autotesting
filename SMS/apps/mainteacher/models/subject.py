# -*- coding: utf-8 -*-
"""
models.subjects

This module contains model class for subjects.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class Subjects(models.Model):
    """Django model for Subjects table."""

    name = models.CharField(max_length=30)

    class Meta:
        """Inner class for Subjects model."""

        db_table = 'Subjects'
        managed = False

    def __unicode__(self):
        return '%s' % self.name
