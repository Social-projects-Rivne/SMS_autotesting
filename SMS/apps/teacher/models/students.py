# -*- coding: utf-8 -*-
"""
models.students

This module contains model class for students.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class Students(models.Model):
    """This class is used to handle data about students in DB."""

    name = models.CharField(max_length=60)
    group = models.ForeignKey('Groups', blank=True, null=True)
    state = models.IntegerField(default=1)

    class Meta:
        """This class gives some options (metadata) attached to the model."""

        db_table = 'Students'
        ordering = ['name']

    def __unicode__(self):
        return '%s' % self.name
