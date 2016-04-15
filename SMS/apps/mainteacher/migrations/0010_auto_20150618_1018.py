# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0009_auto_20150603_2247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roles',
            options={},
        ),
        migrations.AlterModelOptions(
            name='schools',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='subjects',
            options={},
        ),
        migrations.AlterModelOptions(
            name='teachers',
            options={'ordering': ['name']},
        ),
    ]
