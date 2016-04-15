# -*- coding: utf-8 -*-
"""
teacher.signals

Module contains two functions django signals for logging actions of
Lesson and Journal models.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

import logging
import thread

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models.lesson import Lessons
from .models.journal import Journal


@receiver(post_save, sender=Lessons)
def log_lesson_events(sender, **kwargs):
    """Writes information about newly added or updated
    Lesson into log.
    """
    logger = logging.getLogger(__name__)

    lesson = kwargs['instance']
    if kwargs['created']:
        logger.info(u'%s created lesson "%s"',
            lesson.teacher_subject_group.teacher_subject.teacher, lesson)
    else:
        logger.info(u'%s updated lesson "%s"',
            lesson.teacher_subject_group.teacher_subject.teacher, lesson)


@receiver(post_save, sender=Journal)
def log_journal_events(sender, **kwargs):
    """Writes information about newly added or updated
    Journal into log.
    """
    logger = logging.getLogger(__name__)

    journal = kwargs['instance']
    if not journal.mark:
        journal.mark = ''
    if kwargs['created']:
        logger.info(u'Journal[mark:%s-%s] was set for %s, lesson[%s]',
                    journal.mark, journal.marktype, journal.student.name,
                    journal.lesson)
    else:
        logger.info(u'Journal[mark:%s-%s] was changed for %s, lesson[%s]',
                    journal.mark, journal.marktype, journal.student.name,
                    journal.lesson)
