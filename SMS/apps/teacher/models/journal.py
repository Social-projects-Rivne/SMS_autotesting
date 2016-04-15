# -*- coding: utf-8 -*-
"""
models.journal

This module contains model class for journal.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class Journal(models.Model):
    """This class is used to handle data about journal in DB."""

    student = models.ForeignKey('Students')
    lesson = models.ForeignKey('Lessons')
    mark = models.IntegerField(blank=True, null=True)
    marktype = models.ForeignKey('MarkTypes')
    comment = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        """This class gives some options (metadata) attached to the model."""

        db_table = 'Journal'

    def __unicode__(self):
        return '%s - %s' % (self.lesson.date, self.student.name)
