# -*- coding: utf-8 -*-
"""
mainteacher.forms

Module contains class form for adding/updating teachers.

:copyright: (c) 2015 by Sofia Kuzlo.
:license: BSD.
"""

from django.forms import ModelForm
from django.core.exceptions import ValidationError

from models.roles import Roles
from models.schools import Schools
from models.teachers import Teachers
from .utils.validation import Validate


class TeacherForm(ModelForm):
    """This class is the form class for teachers."""

    class Meta:
        model = Teachers
        fields = ['name', 'login', 'email', 'school']

    def clean_name(self):
        """Validate name field."""
        validate = Validate()
        name = self.cleaned_data['name']
        if not validate.check_name(name):
            raise ValidationError(u'Некоректно введено ім\'я.')
        return name

    def clean_login(self):
        """Validate login field."""
        validate = Validate()
        login = self.cleaned_data['login']
        if not validate.check_login(login):
            raise ValidationError(u'Некоректно введно логін.')
        return login

    def clean_email(self):
        """Validate email field."""
        validate = Validate()
        email = self.cleaned_data['email']
        if not validate.check_email(email):
            raise ValidationError(u'Некоректно введно email.')
        return email
