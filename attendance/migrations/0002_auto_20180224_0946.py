# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-24 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session',
            field=models.CharField(choices=[('', 'Please Come Back at the Specified Time. For more details, visit Home Page.')], default='No Attendence', max_length=25),
        ),
    ]
