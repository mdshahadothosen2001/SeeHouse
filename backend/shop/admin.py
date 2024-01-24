from django.contrib import admin

from .models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "vendor",
        "shop_number",
        "shop_name",
        "shop_type",
        "fields",
        "service_started",
        "shop_title",
        "delivery_days",
        "cover_image",
        "rating",
        "is_active",
    )
    list_display_links = (
        "vendor",
        "shop_number",
        "shop_name",
        "shop_type",
        "fields",
        "service_started",
        "shop_title",
        "cover_image",
        "is_active",
    )
    search_fields = (
        "vendor__phone_number",
        "shop_number",
        "shop_name",
        "shop_type",
        "fields",
        "is_active",
    )
    list_per_page = 25


admin.site.register(Shop, ShopAdmin)
