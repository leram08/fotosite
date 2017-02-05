from django.db import models


class Comment(models.Model):
    name = models.CharField("Имя",max_length=200)
    photo = models.FileField("Фотография",blank=False, upload_to='Albums')
    email = models.EmailField("Email")
    message = models.TextField("Ваш отзыв")
    date = models.DateTimeField(auto_now=True)
    check = models.BooleanField("Отображать отзыв",default=False)


    class Meta:
        ordering = ['date']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
	
    def __str__(self):
        return (self.name)