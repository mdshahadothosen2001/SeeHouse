from django.contrib import admin

from .models import ReligionModel


class ReligionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 25


admin.site.register(ReligionModel, ReligionAdmin)
