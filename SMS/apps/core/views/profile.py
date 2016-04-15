# -*- coding: utf-8 -*-
"""
views.teachers

These functions are used for managing user profile.

:copyright: (c) 2015 by Zhmak Pavlo and Sofia Kuzlo.
:license: BSD.
"""

import re

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.core.files.base import ContentFile

from ...mainteacher.models.teachers import Teachers

from ..utils.set_base_template_variable import set_base_template_variable

import StringIO
from PIL import Image


def profile_page(request):
    """Return profile page of current teacher."""

    teacher = Teachers.objects.get(id=request.session['teacher_id'])

    context = {'teacher': teacher,
               'base_template_variable': set_base_template_variable(request)}
    return render(request, 'core/profile.html', context)


def profile_edit(request):
    """Return page for edit profile current teacher."""

    teacher = Teachers.objects.get(id=request.session['teacher_id'])

    if request.method == 'POST':
        if request.POST.get('confirm_button') is not None:
            teacher.name = request.POST.get('name')
            teacher.email = request.POST.get('email')
            teacher.save()

        return HttpResponseRedirect(reverse('profile'))

    context = {'teacher': teacher}
    return render(request, 'core/profile_edit.html', context)


def profile_edit_password(request):
    """return page for editing current teacher's password"""

    teacher = Teachers.objects.get(id=request.session['teacher_id'])
    base_template_variable = set_base_template_variable(request)

    if request.method == 'POST':
        if request.POST.get('confirm_button') is not None:
            # define errors collection
            errors = {}
            password_old = request.POST.get('password-old').strip()
            password_new = request.POST.get('password-new').strip()
            password_confirm = request.POST.get('password-confirm').strip()

            password_pattern = (r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%])"
                                r"\S{6,}$")

            if (password_old != teacher.password or
                    password_new != password_confirm):
                errors['password_confirm'] = u'Старий пароль невірний або \
                                               невірно підтверджено новий.'

            if not re.match(password_pattern, password_new):
                errors['password_new'] = (u'Введіть комбінацію із щонайменше '
                    u'шести цифр, літер верхнього і нижнього регістру, а '
                    u'також спецсимволів зі списку "@#$%".')

            if not errors:
                teacher.password = password_confirm
                teacher.save()
                return HttpResponseRedirect(reverse('profile'))
            else:
                return render(request, 'core/profile_edit_password.html',
                              {'teacher': teacher,
                               'errors': errors,
                             'base_template_variable': base_template_variable})

    return render(request, 'core/profile_edit_password.html',
                  {'teacher': teacher,
                   'base_template_variable': base_template_variable})


def img_upload(request):
    """image upload to server"""

    teacher = Teachers.objects.get(id=request.session['teacher_id'])

    if request.method == 'GET':
        return render(request, 'core/file_upload.html', {})

    if request.method == 'POST':
        filename = request.FILES.get('img_file').name
        file_ext = request.FILES.get('img_file').content_type.split('/')[1]
        file_path = "media/user_avatars/" + filename

        try:
            infile = request.FILES.get('img_file')

            with Image.open(infile) as pil_image:
                # Check format of input image
                if pil_image.format not in ('GIF', 'JPEG', 'PNG'):
                    raise Exception(
                        "Unsupport image type. Please upload bmp, png or jpeg")
                # Check image size
                max_size = 4 * 1024 * 768
                width, height = pil_image.size
                if (width * height) > max_size:
                    raise Exception(
                        "Image too large")

                # Set teacher new avatar
                teacher.avatar.save(filename,
                                    pil_to_django(pil_image, file_ext))
                teacher.save()
        except Exception, e:
            raise

        return HttpResponseRedirect(reverse('profile'))


def pil_to_django(image, format="JPEG"):
    """Convert pil image to django object."""

    fobject = StringIO.StringIO()
    image.save(fobject, format=format)
    return ContentFile(fobject.getvalue())
