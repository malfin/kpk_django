from django.contrib.auth.models import User
from django.db import models

from mainapp.models import Hosting


class HostingBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hosting = models.ForeignKey(Hosting, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.hosting.name}'
