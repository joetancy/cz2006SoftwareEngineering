# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-29 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20160916_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='latitude',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='longitude',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
