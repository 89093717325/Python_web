from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', default='')
    description = models.CharField(max_length=1000, verbose_name='Описание', default='')
    date_start = models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')
    participants_number = models.IntegerField(default=0, validators=[MaxValueValidator(100)],
                                              verbose_name='Количество участников')
    is_private = models.BooleanField(default=False, verbose_name='Частное')

    class Meta:
        verbose_name_plural = 'События'
        verbose_name = 'Событие'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=90, verbose_name='Категория', default='')

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.title

# Create your models here.
