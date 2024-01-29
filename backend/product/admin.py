from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "product_code",
        "thumbnail",
        "stock",
        "price",
        "rating",
        "subcategory",
    )
    list_display_links = (
        "product_name",
        "product_code",
        "thumbnail",
        "price",
        "rating",
        "subcategory",
    )
    search_fields = (
        "product_name",
        "product_code",
        "price",
        "rating",
        "subcategory",
    )
    list_per_page = 25


admin.site.register(Product, ProductAdmin)
