# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170103_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='major',
        ),
        migrations.AddField(
            model_name='resource',
            name='major',
            field=models.ManyToManyField(to='main.Major'),
        ),
    ]
