# -*- coding: utf-8 -*-
"""
models.teacher_subject_group

This module contains model class for teacher-subject-group relationship.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

from __future__ import unicode_literals

from django.db import models


class TeacherSubjectGroups(models.Model):
    """This class is used to handle data about group joined to teacher-subject
    in DB.
    """

    group = models.ForeignKey('Groups')
    teacher_subject = models.ForeignKey('TeacherSubjects')

    class Meta:
        """This class gives some options (metadata) attached to the model."""

        db_table = 'TeacherSubjectGroups'

    def __unicode__(self):
        return 'group id:%s, teacher_subject id:%s' % (self.group.id,
                                                       self.teacher_subject.id)
