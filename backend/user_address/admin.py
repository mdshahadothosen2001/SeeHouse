from django.contrib import admin

from .models import UserAddressModel


class UserAddressAdmin(admin.ModelAdmin):
    def user(self, obj):
        return obj.user.phone_number
    
    def address(self, obj):
        return obj.address.address_line1
    
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


admin.site.register(UserAddressModel, UserAddressAdmin)
