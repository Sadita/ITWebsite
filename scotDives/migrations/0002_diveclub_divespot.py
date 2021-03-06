# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scotDives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiveClub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('latitude', models.CharField(default='default', max_length=50)),
                ('longitude', models.CharField(default='default', max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DiveSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('rating', models.CharField(max_length=10)),
                ('link', models.CharField(max_length=250)),
                ('picture', models.CharField(max_length=1000)),
            ],
        ),
    ]
