# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 11:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('major', models.CharField(choices=[('bachelorcollege', 'Bachelor College'), ('appliedmathematics', 'Applied Mathematics'), ('appliedphysics', 'Applied Physics'), ('architecture', 'Architecture, Urbanism and Building Sciences'), ('automotive', 'Automotive'), ('biomedicalengineering', 'Biomedical Engineering'), ('chemicalengineering', 'Chemical Engineering'), ('computerscience', 'Computer Science'), ('electricalengineering', 'Electrical Engineering'), ('industrialdesign', 'Industrial Design'), ('industrialengineering', 'Industrial Engineering'), ('mechanicalengineering', 'Mechanical Engineering'), ('psychologyandtechnology', 'Psychology and Technology'), ('sustainableinnovations', 'Sustaibable Innovation')], default='bachelorcollege', max_length=45)),
                ('resourcetype', models.CharField(choices=[('summary', 'Summary'), ('practiceexam', 'Practice Exam'), ('oldexam', 'Old Exam')], default='summary', max_length=45)),
                ('upload_date', models.DateTimeField(blank=True, null=True)),
                ('uploadedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
