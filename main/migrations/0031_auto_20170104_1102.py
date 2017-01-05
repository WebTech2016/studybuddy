# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20170104_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resourcetype',
            field=models.CharField(choices=[('Summary', 'Summary'), ('Exam', 'Exam')], default='Summary', max_length=45),
        ),
    ]
