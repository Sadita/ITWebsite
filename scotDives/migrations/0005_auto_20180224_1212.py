# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-24 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scotDives', '0004_divesitelist_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divesitelist',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
