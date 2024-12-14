from django.contrib import admin
from .models import Canvas


@admin.register(Canvas)
class CanvasAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "owner_id"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["id", "owner_id"]
    readonly_fields = ["created_at", "updated_at"]
    # list_editable = ["updated_at"]
