# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-08 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название новости')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Publish Date')),
                ('content', models.TextField(verbose_name='Описание')),
                ('img', models.ImageField(upload_to='Albums', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото на слайдер')),
                ('title', models.CharField(max_length=40, verbose_name='Название фото-слайдера')),
            ],
            options={
                'verbose_name_plural': 'Фотографии на слайдер',
                'verbose_name': 'Фото на слайдер',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название видео')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, verbose_name='Видео')),
            ],
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['title'], 'verbose_name': 'Альбом', 'verbose_name_plural': 'Альбомы'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(upload_to='Albums', verbose_name='Изображение альбома'),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Ссылка для альбома'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название альбома'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(upload_to='Photos', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galery.Item', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название фотографии'),
        ),
    ]