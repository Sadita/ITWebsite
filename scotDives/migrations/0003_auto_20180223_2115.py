# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-23 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scotDives', '0002_diveclub_divespot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divespot',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
