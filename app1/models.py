from django.db import models


class News(models.Model):

    class Meta:
        verbose_name = 'новость'    
        verbose_name_plural = 'новости'

    name = models.CharField(max_length=100, verbose_name='заголовок')
    description = models.CharField(max_length=250, verbose_name='краткое описание')
    content = models.TextField(verbose_name='контент')
    date = models.DateTimeField(verbose_name='дата добавление')
    is_published = models.BooleanField(default=True, verbose_name='публичность')

    def __str__(self):
        return f'{self.name} - {self.date}'
# Create your models here.
