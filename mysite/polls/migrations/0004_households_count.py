# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170913_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='households',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
