from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True)
    about = models.TextField(verbose_name='Обо мне', blank=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'
