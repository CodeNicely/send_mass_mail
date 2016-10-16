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
            name='user_data',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=120, null=True)),
                ('user_emailid', models.CharField(max_length=120, unique=True)),
                ('group_id', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
    ]