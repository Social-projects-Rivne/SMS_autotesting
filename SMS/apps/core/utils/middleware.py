# -*- coding: utf-8 -*-
"""
utils.middleware

This module contains custom middleware classes for SMS project.

:copyright: (c) 2015 by Pavlo Zhmak and Oleksii Omelchuk.
:license: BSD.
"""

import logging
from datetime import datetime, timedelta

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from ...mainteacher.models.teachers import Teachers


class AutoLogout(object):
    """Call on request."""

    def process_request(self, request):
        """Check time user activity if timeout is over -logout."""
        try:
            if 'last_touch' in request.session:
                if (datetime.now() - request.session['last_touch'] >
                        timedelta(0, settings.AUTO_LOGOUT_DELAY * 60)):
                    for key in request.session.keys():
                        del request.session[key]
                    return HttpResponseRedirect(reverse('login'))
        except Exception, e:
            raise

        request.session['last_touch'] = datetime.now()


class TrackUsersMiddleware(object):
    """Middleware class for logging users request."""

    def process_request(self, request):
        """Write every user request in 'track_users' logger."""
        user_ip = (request.META.get('REMOTE_ADDR', '') or
                   request.META.get('HTTP_X_FORWARDED_FOR', ''))

        if 'teacher_id' in request.session:
            logged_user = Teachers.objects.get(
                pk=request.session['teacher_id'])

            logger = logging.getLogger('track_users')
            logger.debug('%s, %s, %s', logged_user.name, request.path, user_ip)
