from django.contrib import admin

from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "unit_number",
        "street_number",
        "address_line1",
        "address_line2",
        "city",
        "region",
        "postal_code",
        "country",
    )
    list_display_links = (
        "unit_number",
        "street_number",
        "address_line1",
        "address_line2",
        "city",
        "region",
        "postal_code",
        "country",
    )
    search_fields = (
        "unit_number",
        "street_number",
        "address_line1",
        "address_line2",
        "city",
        "region",
        "postal_code",
        "country",
    )
    list_per_page = 25


admin.site.register(Address, AddressAdmin)
