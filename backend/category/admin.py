from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category_name",
        "display_subcategories",
    )
    list_display_links = (
        "category_name",
        "display_subcategories",
    )
    search_fields = (
        "category_name",
        "display_subcategories",
    )
    list_per_page = 25
    
    def display_subcategories(self, obj):
        return ", ".join([subcategory.subcategory_name for subcategory in obj.subcategory.all()])

    display_subcategories.short_description = "subcategories"

admin.site.register(Category, CategoryAdmin)
