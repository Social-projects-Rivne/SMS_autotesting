# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0007_auto_20150530_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='avatar',
            field=models.ImageField(null=True, upload_to='static/img/', blank=True),
        ),

    ]
