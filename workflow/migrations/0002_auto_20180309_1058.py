# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 07:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sent_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 9, 10, 58, 18, 204039), verbose_name='sent at'),
        ),
    ]
