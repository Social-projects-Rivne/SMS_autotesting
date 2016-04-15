# -*- coding: utf-8 -*-
"""
utils.email

Module contains functions for sending email in our project.

:copyright: (c) 2015 by Oleksii Omelchuk.
:license: BSD.
"""

import logging
from smtplib import SMTPException

from django.core.mail import send_mail


def pass_sending(name, to_email, login, password):
    """pass_sending(name, recipient, login, password)

    Take 4 string argumetns, compose letter and send it to recipient.
    """
    subject = u'Вітаємо в системі'
    message = u'''\tДоброго дня, {0}.

        Хочемо повідомити Вас, про реєстрацію в SMS.
        Вам було присвоєно логін: {1} та пароль: {2}
        Будь ласка, запам’ятайте й не поширюйте ці дані.

        З повагою, адміністрація сервісу.
        '''.format(name, login, password)
    to_email = to_email
    from_email = 'no_reply@sms.com'
    email_sending(subject, message, from_email, to_email)


def email_sending(subject, message, from_email, to_email):
    """email_sending(subject, message, from_email, to_email)

    Take 4 string argumetns and send email.
    """
    try:
        send_mail(subject, message, from_email, [to_email])
        logger = logging.getLogger('email_status')
        logger.info('"%s" message was sent to %s', subject, to_email)
    except SMTPException:
        message = u'Під час відправки листа "%s"/(%s) виникла помилка.' % \
            (subject, to_email)
        logger = logging.getLogger(__name__)
        logger.exception(message)
