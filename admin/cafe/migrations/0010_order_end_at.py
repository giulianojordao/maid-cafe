# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-15 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0009_auto_20200415_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='end_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
