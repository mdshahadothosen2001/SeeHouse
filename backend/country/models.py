from django.db import models


class CountryModel(models.Model):
    country_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        db_table = "country"
