from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "preview", "is_published")
    list_filter = ("title",)
    search_fields = ("title", "content",)