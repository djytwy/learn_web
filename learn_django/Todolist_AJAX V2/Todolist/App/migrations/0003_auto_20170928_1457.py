# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-09-28 06:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20170928_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='things',
            name='Delete_NO',
        ),
        migrations.RemoveField(
            model_name='things',
            name='Edit_NO',
        ),
    ]
