# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0003_schools_director'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teachers',
            options={},
        ),
        migrations.AddField(
            model_name='schools',
            name='state',
            field=models.IntegerField(default=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='schools',
            name='director',
            field=models.ForeignKey(blank=True, to='mainteacher.Teachers', null=True),
        ),
    ]
