# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-21 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
