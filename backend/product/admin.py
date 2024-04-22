from django.contrib import admin
from django.utils.html import mark_safe

from .models import ProductModel


class ProductAdmin(admin.ModelAdmin):
    def category(self, obj):
        return obj.category.name

    def subcategory(self, obj):
        return obj.subcategory.name

    def display_image(self, obj):
        return mark_safe(
            '<img src="%s" style="max-width:70px; max-height:70px;" />' % obj.thumbnail
        )

    list_display = (
        "title",
        "category",
        "subcategory",
        "price",
        "display_image",
        "points",
        "rating",
    )
    list_display_links = (
        "title",
        "category",
        "subcategory",
        "price",
        "points",
        "rating",
    )
    search_fields = (
        "title",
        "category",
        "subcategory",
        "points",
        "rating",
    )
    list_filter = [
        "is_active",
    ]
    list_per_page = 25


admin.site.register(ProductModel, ProductAdmin)
