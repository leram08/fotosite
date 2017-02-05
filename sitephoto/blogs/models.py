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


class Blogs(models.Model):
    def __str__(self):
        return self.title

    def get_absolute_url(self):     
        return reverse('project_detail', args=[self.id])

    def get_thumbnail(self):
        return self.img.url
    
    title = models.CharField("Название новости", max_length=60)
    publish_date = models.DateTimeField("Publish Date", auto_now_add=True)
    #content = models.TextField("Описание")
    news = models.TextField("Новость:")
    img = models.ImageField("Изображение",null=False, blank=False, upload_to='Albums')
    content = RichTextUploadingField(blank=True, default='', config_name='awesome_ckeditor')
