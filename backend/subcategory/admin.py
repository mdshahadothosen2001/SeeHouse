from django.contrib import admin

from .models import Subcategory


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "subcategory_name",
    )
    list_display_links = ("subcategory_name",)
    search_fields = ("subcategory_name",)
    list_per_page = 25


admin.site.register(Subcategory, SubcategoryAdmin)
