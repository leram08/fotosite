from django.db import models



class Orders(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField("Email")
    message=models.TextField("Сообщение")

    class Meta:
        ordering = ['name']
        verbose_name='Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return(self.name)
