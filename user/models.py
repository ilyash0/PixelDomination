from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pixels_colored = models.PositiveIntegerField(default=0, verbose_name="Количество закрашенных пикселей")

    def __str__(self):
        return self.username
