# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0010_auto_20150618_1018'),
    ]

    operations = [

        migrations.AddField(
            model_name='teachers',
            name='salt',
            field=models.CharField(max_length=180, null=True),
        ),

    ]
