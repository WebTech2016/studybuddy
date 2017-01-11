# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20170108_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='major',
            field=models.CharField(choices=[('bachelorcollege', 'Bachelor College'), ('appliedmathematics', 'Applied Mathematics'), ('appliedphysics', 'Applied Physics'), ('architecture', 'Architecture, Urbanism and Building Sciences'), ('automotive', 'Automotive'), ('biomedicalengineering', 'Biomedical Engineering'), ('chemicalengineering', 'Chemical Engineering'), ('computerscience', 'Computer Science'), ('electricalengineering', 'Electrical Engineering'), ('industrialdesign', 'Industrial Design'), ('industrialengineering', 'Industrial Engineering'), ('mechanicalengineering', 'Mechanical Engineering'), ('psychologyandtechnology', 'Psychology and Technology'), ('sustainableinnovation', 'Sustainable Innovation')], default='computerscience', max_length=45),
        ),
        migrations.AlterField(
            model_name='resource',
            name='course',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='major', chained_model_field='major', on_delete=django.db.models.deletion.CASCADE, show_all=True, to='main.Course'),
        ),
    ]