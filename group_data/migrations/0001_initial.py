# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-16 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group_data',
            fields=[
                ('group_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
