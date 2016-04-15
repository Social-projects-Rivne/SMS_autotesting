# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0002_auto_20150430_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='schools',
            name='director',
            field=models.ForeignKey(default=1, to='mainteacher.Teachers'),
            preserve_default=False,
        ),
    ]
