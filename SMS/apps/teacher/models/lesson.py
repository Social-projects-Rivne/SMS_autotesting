# -*- coding: utf-8 -*-
"""
models.lessons

This module contains model class for lessons.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class Lessons(models.Model):
    """This class is used to handle data about lesson in DB."""

    date = models.DateField()
    topic = models.CharField(max_length=200)
    homework = models.CharField(max_length=200)
    lesson_type = models.ForeignKey('LessonTypes')
    teacher_subject_group = models.ForeignKey('TeacherSubjectGroups')
    teacher_replace = models.ForeignKey('mainteacher.Teachers',
                                        blank=True,
                                        null=True)

    class Meta:
        """This class gives some options (metadata) attached to the model."""

        db_table = 'Lessons'
        ordering = ['date']

    def __unicode__(self):
        return '%s group:%s - subject:%s' % (
            self.date,
            self.teacher_subject_group.group.name,
            self.teacher_subject_group.teacher_subject.subject.name)

    def is_control(self):
        """Method for checking whether lesson is control."""
        if self.lesson_type.id == 3:
            return True
        else:
            return False
