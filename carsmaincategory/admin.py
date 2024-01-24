from django.contrib import admin
from .models import *
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year','data_update', 'is_published', 'cat']
    list_display_links = ['id', 'title']
    ordering = ['data_update', 'title']
    list_editable = ['is_published']
    list_per_page = 5

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_display_links = ["id", "name"]
    list_per_page = 5
    ordering = ["id"]