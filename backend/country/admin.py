from django.contrib import admin

from .models import CountryModel


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "country_name",
    )
    list_display_links = ("country_name",)
    search_fields = ("country_name",)
    list_per_page = 25


admin.site.register(CountryModel, CountryAdmin)
