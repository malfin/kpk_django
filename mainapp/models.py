from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=128)
    image = models.ImageField('Картинка', upload_to='category', height_field=None, width_field=None, max_length=100,
                              null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Hosting(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название тарифа', max_length=128)
    desc = models.TextField(verbose_name='Описание тарифа', blank=True)
    prise = models.IntegerField(verbose_name='Цена', default=0)
    disk = models.CharField(verbose_name='Дисковое пространство', max_length=128)
    site = models.CharField(verbose_name='Сайты', max_length=128, blank=True)
    db = models.CharField(verbose_name='База Данных', max_length=128, blank=True)
    cpu = models.CharField(verbose_name='Нагрузка на цп', max_length=128)
    ram = models.CharField(verbose_name='Оперативная память', max_length=128, blank=True)
    traffic = models.CharField(verbose_name='Трафик', max_length=128)
    location = models.CharField(verbose_name='Локация', max_length=128)
    ddos = models.CharField(verbose_name='Защита от ДДОС', max_length=128)
    is_active = models.BooleanField(verbose_name='Активный тариф')
    image = models.ImageField(verbose_name='Картинка', upload_to='hosting', height_field=None, width_field=None, max_length=100,
                              null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'хостинг'
        verbose_name_plural = 'хостинги'
