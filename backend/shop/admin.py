from django.contrib import admin
from django.utils.html import mark_safe

from .models import ShopModel


class ShopAdmin(admin.ModelAdmin):
    def shop_type(self, obj):
        return obj.shop_type.shop_type

    def user(self, obj):
        return obj.vendor.phone_number

    def display_image(self, obj):
        return mark_safe(
            '<img src="%s" style="max-width:70px; max-height:70px;" />'
            % obj.cover_photo
        )

    display_image.allow_tags = True
    display_image.short_description = "Image"

    list_display = (
        "id",
        "vendor",
        "shop_number",
        "name",
        "shop_type",
        "fields",
        "service_started",
        "title",
        "delivery_days",
        "display_image",
        "rating",
        "is_active",
    )
    list_display_links = (
        "vendor",
        "shop_number",
        "name",
        "shop_type",
        "fields",
        "service_started",
        "title",
        "display_image",
        "is_active",
    )
    search_fields = (
        "vendor__phone_number",
        "shop_number",
        "name",
        "shop_type",
        "fields",
        "is_active",
    )
    list_per_page = 25


admin.site.register(ShopModel, ShopAdmin)
