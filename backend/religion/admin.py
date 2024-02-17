from django.contrib import admin

from .models import ReligionModel


class ReligionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "religion_name",
    )
    list_display_links = ("religion_name",)
    search_fields = ("religion_name",)
    list_per_page = 25


admin.site.register(ReligionModel, ReligionAdmin)
