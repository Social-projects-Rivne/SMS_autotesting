# -*- coding: utf-8 -*-
"""
models.roles

This module contains model class for roles.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class Roles(models.Model):
    """Django model for Roles table."""

    role_name = models.CharField(max_length=20)

    class Meta:
        """Inner class for Roles model."""

        db_table = 'Roles'
        managed = False

    def __unicode__(self):
        return '%s' % self.role_name
