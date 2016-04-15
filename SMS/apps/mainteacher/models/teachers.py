# -*- coding: utf-8 -*-
"""
models.teachers

This module contains model class for teachers.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class Teachers(models.Model):
    """This class is used to handle data about teachers in DB."""

    name = models.CharField(max_length=60)
    login = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=180)
    role = models.ForeignKey('Roles', default=1)
    school = models.ForeignKey('Schools', blank=True, null=True)
    state = models.IntegerField(default=1, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)
    salt = models.CharField(max_length=100, null=True)

    class Meta:
        """This class gives some options (metadata) attached to the
        model.
        """

        db_table = 'Teachers'
        ordering = ['name']
        managed = False

    def __unicode__(self):
        return '%s' % self.name
