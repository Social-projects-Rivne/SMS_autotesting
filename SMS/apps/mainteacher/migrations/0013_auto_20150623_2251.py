# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0012_auto_20150623_1054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roles',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='schools',
            options={'ordering': ['name'], 'managed': False},
        ),
        migrations.AlterModelOptions(
            name='subjects',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='teachers',
            options={'ordering': ['name'], 'managed': False},
        ),
    ]
