# -*- coding: utf-8 -*-
"""
models.teacher_subject

This module contains model class for teacher-subject relationship.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class TeacherSubjects(models.Model):
    """This class is used to handle data about teacher-subject relationship
    in DB.
    """

    subject = models.ForeignKey('mainteacher.Subjects')
    teacher = models.ForeignKey('mainteacher.Teachers')

    class Meta:
        """This class gives some options (metadata) attached to the model."""

        db_table = 'TeacherSubjects'

    def __unicode__(self):
        return '%s - %s' % (self.teacher.name, self.subject.name)
