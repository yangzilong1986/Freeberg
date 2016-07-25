# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-27 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocktracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='close',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='open',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='volume',
            field=models.IntegerField(null=True),
        ),
    ]