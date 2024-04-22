from django.contrib import admin

from .models import ProductModel


class ProductAdmin(admin.ModelAdmin):
    def category(self, obj):
        return obj.category.name

    def subcategory(self, obj):
        return obj.subcategory.name

    list_display = (
        "title",
        "category",
        "subcategory",
        "price",
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
