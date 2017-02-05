from django.db import models
from django.conf import settings
from django.db.models.fields.files import ImageField, ImageFieldFile
from embed_video.fields import EmbedVideoField
from ckeditor_uploader.fields import RichTextUploadingField
import PIL
from PIL import Image
import os
from os import path
from django.core.urlresolvers import reverse

_MAX_SIZE = 500
	
class Item(models.Model):
    title = models.CharField("Название альбома",max_length=200)
    description = models.TextField("Описание")
    img = models.ImageField("Изображение альбома",null=False, blank=False, upload_to='Albums')
    slug = models.SlugField("Ссылка для альбома",max_length=100)
	
    class Meta:
        ordering = ['title']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
	
    def __str__(self):
        return (self.title)

		
class Photo(models.Model):
	item = models.ForeignKey(Item, verbose_name=u'Альбом')
	title = models.CharField("Название фотографии",max_length=100)
	img = models.ImageField("Фото", upload_to='Photos')

	
	class Meta:
		verbose_name = 'Фото'
		verbose_name_plural = 'Фотографии'
		
	def __str__(self):
		return self.title
		
		
	def image_img(self):
            image_path = os.path.join(settings.MEDIA_URL, self.img)
            image_path = image_path.replace('\\','/')
            return '<a href="'+ str(self.id)+'/"><img src="'+str(image_path) +'"/></a>'

            image_img.short_description = 'Картинка'
            image_img.allow_tags = True




class Slider(models.Model):
	image = models.ImageField("Фото на слайдер",)
	title = models.CharField("Название фото-слайдера",max_length=40)
	class Meta:
		verbose_name = 'Фото на слайдер'
		verbose_name_plural = 'Фотографии на слайдер'
	
	def __str__(self):
		return self.title
		
class Video(models.Model):
	title = models.CharField("Название видео",max_length=50)
	video = EmbedVideoField(blank=True, verbose_name='Видео')
	
