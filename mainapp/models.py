from django.db import models


# Hosting_Category


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


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
