# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 10:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name='last name')),
                ('phone_number', models.CharField(max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number (9 - 15 digits).', regex='^[0-9]{9,15}$')], verbose_name='phone number')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('id_number', models.CharField(max_length=20, null=True, unique=True, verbose_name='id number')),
                ('staff_number', models.CharField(max_length=30, null=True, unique=True, verbose_name='staff number')),
                ('activation_key', models.CharField(blank=True, max_length=40, null=True)),
                ('activation_key_expires', models.DateTimeField(blank=True, null=True)),
                ('verification_code', models.IntegerField(blank=True, null=True)),
                ('verification_code_expires', models.DateTimeField(blank=True, null=True)),
                ('account_verified_date', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('last_seen', models.DateTimeField(blank=True, null=True, verbose_name='last seen')),
                ('force_logout_date', models.DateTimeField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
                'ordering': ['id'],
                'permissions': (('create_deactivate_user', 'Accounts - Can add/deactivate a user'), ('edit_user', 'Accounts - Can edit details of a user')),
                'default_permissions': (),
            },
        ),
    ]
