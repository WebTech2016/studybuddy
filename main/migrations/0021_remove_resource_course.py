# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20170103_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='course',
        ),
    ]
