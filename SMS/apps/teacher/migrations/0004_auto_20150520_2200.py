# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20150517_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'LessonTypes',
            },
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='students',
            name='state',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='groups',
            name='state',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='journal',
            name='comment',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='lesson',
            field=models.ForeignKey(to='teacher.Lessons'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='marktype',
            field=models.ForeignKey(to='teacher.MarkTypes'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='student',
            field=models.ForeignKey(to='teacher.Students'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='students',
            name='group',
            field=models.ForeignKey(blank=True, to='teacher.Groups', null=True),
        ),
        migrations.AlterField(
            model_name='teachersubjectgroups',
            name='group',
            field=models.ForeignKey(to='teacher.Groups'),
        ),
        migrations.AlterField(
            model_name='teachersubjectgroups',
            name='teacher_subject',
            field=models.ForeignKey(to='teacher.TeacherSubjects'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='lesson_type',
            field=models.ForeignKey(default=1, to='teacher.LessonTypes'),
            preserve_default=False,
        ),
    ]
