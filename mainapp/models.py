from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


# Типо блюда(гор.выпечка -> сами блюда)
class Web(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    prise = models.IntegerField(default=0)
    disk = models.CharField(max_length=128)
    site = models.CharField(max_length=128)
    db = models.CharField(max_length=128)
    cpu = models.CharField(max_length=128)
    traffic = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    ddos = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Веб'
        verbose_name_plural = 'Веб'


class Dedic(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    prise = models.IntegerField(default=0)
    prise_day = models.IntegerField(default=0)
    cpu = models.CharField(max_length=128)
    core = models.CharField(max_length=128)
    ram = models.CharField(max_length=128)
    disk = models.CharField(max_length=128)
    ipv4 = models.CharField(max_length=128)
    traffic = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    ddos = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Выделенный сервер'
        verbose_name_plural = 'Выделенные сервера'


class Vds(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)
    prise = models.IntegerField(default=0)
    cpu = models.CharField(max_length=128)
    core = models.CharField(max_length=128)
    ram = models.CharField(max_length=128)
    disk = models.CharField(max_length=128)
    ipv4 = models.CharField(max_length=128)
    traffic = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    ddos = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Виртуальный сервер'
        verbose_name_plural = 'Виртуальные сервера'
