# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-11 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180811_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='enroll_number',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
