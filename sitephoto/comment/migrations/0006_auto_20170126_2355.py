# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-26 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0005_auto_20170126_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.FileField(upload_to='Albums', verbose_name='Фотография'),
        ),
    ]
