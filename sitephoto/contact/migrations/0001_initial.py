# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-03 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'ordering': ['name'],
                'verbose_name': 'Заказ',
            },
        ),
    ]
