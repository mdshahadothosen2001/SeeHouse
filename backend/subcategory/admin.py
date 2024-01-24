from django.contrib import admin

from .models import Subcategory


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "subcategory_name",
        "display_products",
    )
    list_display_links = (
        "subcategory_name",
        "display_products",
    )
    search_fields = (
        "subcategory_name",
        "display_products",
    )
    list_per_page = 25
    
    def display_products(self, obj):
        return ", ".join([product.product_name for product in obj.product.all()])

    display_products.short_description = "products"

admin.site.register(Subcategory, SubcategoryAdmin)
