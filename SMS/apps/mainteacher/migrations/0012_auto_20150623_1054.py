# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0011_auto_20150618_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='password',
            field=models.CharField(max_length=180),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='salt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
