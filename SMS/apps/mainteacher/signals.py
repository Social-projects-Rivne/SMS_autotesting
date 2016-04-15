# -*- coding: utf-8 -*-
"""
mainteacher.signals

Module contains two functions django signals for logging actions of
Schools, Teachers models.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models.schools import Schools
from .models.teachers import Teachers


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Schools)
def log_school_events(sender, **kwargs):
    """Writes information about newly added, updated
    or deleted school into log.
    """
    school = kwargs['instance']
    if kwargs['created']:
        logger.info("School %s was inserted into the DB", school.name)
    elif school.state == 0:
        logger.info("School %s was deleted", school.name)
    else:
        logger.info("School %s was updated in the DB", school.name)


@receiver(post_save, sender=Teachers)
def log_teacher_events(sender, **kwargs):
    """Writes information about newly added, updated
    or deleted teacher into log.
    """
    teacher = kwargs['instance']
    if kwargs['created']:
        logger.info('Teacher %s(id:%s) was inserted to the DB', teacher.name,
                    teacher.id)
    elif teacher.state == 0:
        logger.info('Teacher %s(id:%s) was deleted', teacher.name, teacher.id)
    else:
        logger.info('Teacher %s(id:%s) was updated in the DB', teacher.name,
                    teacher.id)
