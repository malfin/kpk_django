from django.db import models


# Hosting_Category


class Category(models.Model):
    name = models.CharField('Название категории', max_length=128)
    image = models.ImageField('Картинка', upload_to='static/img', height_field=None, width_field=None, max_length=100,
                              null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Web(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField('Название тарифа', max_length=128)
    desc = models.TextField('Описание тарифа', blank=True)
    prise = models.IntegerField('Цена', default=0)
    disk = models.CharField('Дисковое пространство', max_length=128)
    site = models.CharField('Сайты', max_length=128)
    db = models.CharField('База Данных', max_length=128)
    cpu = models.CharField('Нагрузка на цп', max_length=128)
    traffic = models.CharField('Трафик', max_length=128)
    location = models.CharField('Локация', max_length=128)
    ddos = models.CharField('Защита от ДДОС', max_length=128)
    is_active = models.BooleanField('Активный тариф')
    image = models.ImageField('Картинка', upload_to='static/img', height_field=None, width_field=None, max_length=100,
                              null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Веб'
        verbose_name_plural = 'Веб'


class Dedic(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField('Название тарифа', max_length=128)
    desc = models.TextField('Описание тарифа', blank=True)
    prise = models.IntegerField('Цена', default=0)
    disk = models.CharField('Дисковое пространство', max_length=128)
    cpu = models.CharField('Процессор', max_length=128)
    ram = models.CharField('Оперативная память', null=True, max_length=20)
    traffic = models.CharField('Трафик', max_length=128)
    location = models.CharField('Локация', max_length=128)
    ddos = models.CharField('Защита от ДДОС', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Выделенный сервер'
        verbose_name_plural = 'Выделенные сервера'
