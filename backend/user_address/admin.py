from django.contrib import admin

from .models import UserAddress


class UserAddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "address",
        "is_default",
    )
    list_display_links = (
        "user",
        "address",
    )
    search_fields = (
        "user",
        "address",
    )
    list_per_page = 25


admin.site.register(UserAddress, UserAddressAdmin)
