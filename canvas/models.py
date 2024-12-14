from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

User = get_user_model()


class Canvas(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.JSONField(default=dict, verbose_name="Состояние пикселей")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Создатель полотна")

    def __str__(self):
        return f"Полотно {self.id}"

    class Meta:
        verbose_name = "Полотно"
        verbose_name_plural = "Полотна"


# Создание общего полотна с ID 0 при запуске миграций
@receiver(post_migrate)
def create_default_canvas(sender, **kwargs):
    if not Canvas.objects.filter(id=0).exists():
        Canvas.objects.create(id=0, owner=None, state={})
        print("Общее полотно создано.")
