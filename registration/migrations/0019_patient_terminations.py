# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-26 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_auto_20180324_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='terminations',
            field=models.CharField(blank=True, default='0', max_length=3, null=True),
        ),
    ]
