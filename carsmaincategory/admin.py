from django.contrib import admin, messages
from .models import *
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year','data_update', 'is_published', 'cat', 'brief_info']
    list_display_links = ['id', 'title']
    ordering = ['data_update', 'title']
    list_editable = ['is_published']
    list_per_page = 5
    actions = ["set_published", "set_draft"]
    search_fields = ["title", "cat__name"]
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ["cat__name", "is_published"]
    filter_horizontal = ["tags"]

    @admin.display(description="коротка інформація", ordering="content")
    def brief_info(self, car: Cars):
        return f"overall amount symbols of content:{len(car.content)}"

    @admin.action(description="publish up")
    def set_published(self, request, queryset):
        q = queryset.update(is_published=Cars.Status.PUBLISHED)
        self.message_user(request, f"Опубліковано {q} машини")

    @admin.action(description="draft up")
    def set_draft(self, request, queryset):
        q = queryset.update(is_published=Cars.Status.DRAFT)
        self.message_user(request, f"Деопубліковано {q} машини", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_display_links = ["id", "name"]
    list_per_page = 5
    ordering = ["id"]