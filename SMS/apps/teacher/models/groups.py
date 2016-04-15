# -*- coding: utf-8 -*-
"""
models.groups

This module contains model class for groups.

:copyright: (c) 2015 by Sofia Kuzlo, Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class Groups(models.Model):
    """This class is used to handle data about groups in DB."""

    name = models.CharField(max_length=5)
    school = models.ForeignKey('mainteacher.Schools', blank=True, null=True)
    teacher = models.ForeignKey('mainteacher.Teachers', blank=True, null=True)
    state = models.IntegerField(default=1)

    class Meta:
        """This class gives some options (metadata) attached to the model."""

        db_table = 'Groups'
        ordering = ['name']

    def __unicode__(self):
        if self.school:
            return '%s - %s' % (self.school.name, self.name)
        else:
            return '%s' % self.name
