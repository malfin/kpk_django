from django.db import models


# Hosting_Category


class Category(models.Model):
    name = models.CharField('Название категории', max_length=128)

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
    db = models.CharField('БД', max_length=128)
    cpu = models.CharField('Нагрузка на цп', max_length=128)
    traffic = models.CharField('Трафик', max_length=128)
    location = models.CharField('Локация', max_length=128)
    ddos = models.CharField('Защита от ДДОС', max_length=128)
    is_active = models.BooleanField('Активный тариф', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Веб'
        verbose_name_plural = 'Веб'
