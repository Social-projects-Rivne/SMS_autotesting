# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schools',
            options={'ordering': ['name']},
        ),
    ]
