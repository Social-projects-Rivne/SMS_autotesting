# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0005_auto_20150501_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schools',
            options={'ordering': ['name'], 'managed': False},
        ),
        migrations.AlterModelOptions(
            name='teachers',
            options={'ordering': ['name'], 'managed': False},
        ),
    ]
