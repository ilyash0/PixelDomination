from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pixels_colored = models.PositiveIntegerField(default=0, verbose_name="Количество закрашенных пикселей")
    games_played = models.PositiveIntegerField(default=0, verbose_name="Сыграно игр")
    time_played = models.PositiveIntegerField(default=0, verbose_name="Время в игре")

    def __str__(self):
        return self.username
