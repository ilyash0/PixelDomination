from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "date_joined", "is_staff", "pixels_colored"]
    list_filter = ["date_joined", "is_staff"]
    search_fields = ["username", "email"]
