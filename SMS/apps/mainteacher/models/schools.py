# -*- coding: utf-8 -*-
"""
models.schools

This module contains model class for schools.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class Schools(models.Model):
    """Django model for Schools table."""

    name = models.CharField(max_length=120)
    address = models.CharField(max_length=256, blank=True, null=True)
    director = models.ForeignKey('Teachers', blank=True, null=True)
    state = models.IntegerField(default=1, blank=True, null=True)

    class Meta:
        """Inner class for Schools model."""

        db_table = 'Schools'
        ordering = ['name']
        managed = False

    def __unicode__(self):
        """String presentation for model."""
        return '%s' % self.name
