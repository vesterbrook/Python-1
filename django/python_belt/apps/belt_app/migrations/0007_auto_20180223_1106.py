# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-23 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0006_auto_20180223_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='apptime',
            field=models.TimeField(default='blank'),
        ),
    ]