from django.db import models



class uslugi_photo(models.Model):
	title = models.CharField("Название фото-услуги", max_length=200)
	description = models.TextField("Описание")

	class Meta:
		ordering = ['title']
		verbose_name = 'Фото-услуга'
		verbose_name_plural = 'Фото-услуги'
	def __str__(self):
		return(self.title)

class uslugi_video(models.Model):
	title = models.CharField("Название видео-услуги", max_length=200)
	description = models.TextField("Описание")

	class Meta:
		ordering = ['title']
		verbose_name = 'Видео-услуга'
		verbose_name_plural = ['Видео-услуги']
	def __str__(self):
		return(self.title)