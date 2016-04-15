# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0004_auto_20150501_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='state',
            field=models.IntegerField(default=1, null=True, blank=True),
        ),
    ]
