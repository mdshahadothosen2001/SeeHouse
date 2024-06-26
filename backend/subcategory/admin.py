from django.contrib import admin

from .models import SubcategoryModel


class SubcategoryAdmin(admin.ModelAdmin):
    def category(self, obj):
        return obj.category.name

    list_display = (
        "id",
        "name",
        "category",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 25


admin.site.register(SubcategoryModel, SubcategoryAdmin)
