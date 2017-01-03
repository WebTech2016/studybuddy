# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_resource_resourcefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMajor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50)),
                ('major', models.CharField(choices=[('bachelorcollege', 'Bachelor College'), ('appliedmathematics', 'Applied Mathematics'), ('appliedphysics', 'Applied Physics'), ('architecture', 'Architecture, Urbanism and Building Sciences'), ('automotive', 'Automotive'), ('biomedicalengineering', 'Biomedical Engineering'), ('chemicalengineering', 'Chemical Engineering'), ('computerscience', 'Computer Science'), ('electricalengineering', 'Electrical Engineering'), ('industrialdesign', 'Industrial Design'), ('industrialengineering', 'Industrial Engineering'), ('mechanicalengineering', 'Mechanical Engineering'), ('psychologyandtechnology', 'Psychology and Technology'), ('sustainableinnovations', 'Sustaibable Innovation')], default='bachelorcollege', max_length=45)),
            ],
        ),
        migrations.RemoveField(
            model_name='resource',
            name='major',
        ),
        migrations.AddField(
            model_name='resource',
            name='courseandmajor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.CourseMajor'),
        ),
    ]
