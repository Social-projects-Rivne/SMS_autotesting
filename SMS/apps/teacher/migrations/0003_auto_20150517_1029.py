# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20150517_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='teacher_replace',
            field=models.ForeignKey(blank=True, to='mainteacher.Teachers', null=True),
        ),
    ]
