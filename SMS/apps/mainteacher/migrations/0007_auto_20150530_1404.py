# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0006_auto_20150514_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teachers',
            options={'ordering': ['name']},
        ),
    ]
