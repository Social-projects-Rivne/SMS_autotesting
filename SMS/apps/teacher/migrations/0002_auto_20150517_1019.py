# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersubjects',
            name='subject',
            field=models.ForeignKey(to='mainteacher.Subjects'),
        ),
    ]
