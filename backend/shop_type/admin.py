from django.contrib import admin

from .models import ShopType


class ShopTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "shop_type",
    )
    list_display_links = ("shop_type",)
    search_fields = ("shop_type",)
    list_per_page = 25


admin.site.register(ShopType, ShopTypeAdmin)
