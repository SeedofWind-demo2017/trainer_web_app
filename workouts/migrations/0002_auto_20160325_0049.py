# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 00:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedworkouts',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='workouts.Userwithworkouts'),
        ),
    ]