# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-20 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Things',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('things', models.CharField(max_length=300)),
            ],
        ),
    ]