# -*- coding: utf-8 -*-

import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from ..teacher.models.groups import Groups
from ..teacher.models.students import Students
from ..mainteacher.models.teachers import Teachers


@receiver(post_save, sender=Groups)
def log_groups_events(sender, **kwargs):
    """"""
    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    if kwargs['created']:
        logger.info(u'Director created group "%s"', group)
    elif group.state == 0:
        logger.info(u'Director delete group "%s"', group)
    else:
        logger.info(u'Director updated group "%s"', group)


@receiver(post_save, sender=Students)
def log_groups_events(sender, **kwargs):
    """"""
    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    if kwargs['created']:
        logger.info(u'Director inserted student %s-%s', student.name,
                    student.group.name)
    elif student.state == 0:
        logger.info(u'Director rejected student %s-%s', student.name,
                    student.group.name)
    elif student.state == 2:
        logger.info(u'Director graduated student %s-%s', student.name,
                    student.group.name)
    else:
        logger.info(u'Director updated student %s-%s', student.name,
                    student.group.name)