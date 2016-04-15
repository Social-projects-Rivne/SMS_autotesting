# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0008_auto_20150530_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teachers',
            options={'ordering': ['name'], 'managed': False},
        ),
    ]
