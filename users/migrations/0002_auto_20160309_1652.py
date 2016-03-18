# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularaccount',
            name='goal',
            field=models.TextField(default='Goal'),
        ),
        migrations.AddField(
            model_name='regularaccount',
            name='profile_pic',
            field=models.ImageField(default='http://postimg.org/image/r8k7o4m95/', height_field=42, upload_to='', width_field=42),
        ),
        migrations.AddField(
            model_name='traineraccount',
            name='pastExperience',
            field=models.TextField(default='Past Experience'),
        ),
        migrations.AddField(
            model_name='traineraccount',
            name='profile_pic',
            field=models.ImageField(default='http://postimg.org/image/r8k7o4m95/', height_field=42, upload_to='', width_field=42),
        ),
    ]