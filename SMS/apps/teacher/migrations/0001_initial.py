# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainteacher', '0006_auto_20150514_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
                ('state', models.IntegerField(default=1, null=True, blank=True)),
                ('school', models.ForeignKey(blank=True, to='mainteacher.Schools', null=True)),
                ('teacher', models.ForeignKey(blank=True, to='mainteacher.Teachers', null=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.IntegerField(null=True, blank=True)),
                ('comment', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'Journal',
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('topic', models.CharField(max_length=200)),
                ('homework', models.CharField(max_length=200)),
                ('teacher_replace', models.ForeignKey(to='mainteacher.Teachers', blank=True)),
            ],
            options={
                'db_table': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='MarkTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'MarkTypes',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('group', models.ForeignKey(to='teacher.Groups', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'Students',
            },
        ),
        migrations.CreateModel(
            name='TeacherSubjectGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.ForeignKey(to='teacher.Groups', blank=True)),
            ],
            options={
                'db_table': 'TeacherSubjectGroups',
            },
        ),
        migrations.CreateModel(
            name='TeacherSubjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.ForeignKey(to='teacher.Groups')),
                ('teacher', models.ForeignKey(to='mainteacher.Teachers')),
            ],
            options={
                'db_table': 'TeacherSubjects',
            },
        ),
        migrations.AddField(
            model_name='teachersubjectgroups',
            name='teacher_subject',
            field=models.ForeignKey(blank=True, to='teacher.TeacherSubjects', null=True),
        ),
        migrations.AddField(
            model_name='lessons',
            name='teacher_subject_group',
            field=models.ForeignKey(to='teacher.TeacherSubjectGroups'),
        ),
        migrations.AddField(
            model_name='journal',
            name='lesson',
            field=models.ForeignKey(blank=True, to='teacher.Lessons', null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='marktype',
            field=models.ForeignKey(blank=True, to='teacher.MarkTypes', null=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='student',
            field=models.ForeignKey(blank=True, to='teacher.Students', null=True),
        ),
    ]
