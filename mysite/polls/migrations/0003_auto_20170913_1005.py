# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170913_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wateryield',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
