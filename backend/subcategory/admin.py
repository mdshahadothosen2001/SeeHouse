from django.contrib import admin

from .models import SubcategoryModel


class SubcategoryAdmin(admin.ModelAdmin):
    def category(self, obj):
        return obj.category.category_name
    
    list_display = (
        "id",
        "subcategory_name",
        "category",
    )
    list_display_links = ("subcategory_name",)
    search_fields = ("subcategory_name",)
    list_per_page = 25


admin.site.register(SubcategoryModel, SubcategoryAdmin)
