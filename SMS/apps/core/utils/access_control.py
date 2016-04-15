# -*- coding: utf-8 -*-
"""
utils.access_control

This decorator for check user access.

:copyright: (c) 2015 by Zhmak Pavlo.
:license: BSD.
"""

from django.http import Http404

from ...mainteacher.models.teachers import Teachers


def access_control(permission):
    """Check if user have any permission on this page."""

    def _method_wrapper(view_method):
        """Wrapper with functions to invoke the method."""

        def _arguments_wrapper(request, *args, **kwargs):
            """Wrapper with arguments to invoke the method."""
            if permission is not None and request.session['teacher_id']:
                user = Teachers.objects.get(id=request.session['teacher_id'])
                if (user.role.role_name.encode('utf-8').strip() !=
                        permission.strip()):
                    raise Http404("")

            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper
