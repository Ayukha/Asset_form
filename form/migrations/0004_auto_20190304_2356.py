# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-04 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20190304_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
