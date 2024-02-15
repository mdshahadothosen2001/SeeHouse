from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category_name",
    )
    list_display_links = ("category_name",)
    search_fields = ("category_name",)
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
