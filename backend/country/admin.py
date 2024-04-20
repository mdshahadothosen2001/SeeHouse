from django.contrib import admin

from .models import CountryModel


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 25


admin.site.register(CountryModel, CountryAdmin)
