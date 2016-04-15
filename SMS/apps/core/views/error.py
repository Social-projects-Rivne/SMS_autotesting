# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
    """Return custom page for 404 error."""

    response = render_to_response('core/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
