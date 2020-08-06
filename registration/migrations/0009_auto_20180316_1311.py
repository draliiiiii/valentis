# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20180316_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='child_age',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='child_dob',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
    ]
