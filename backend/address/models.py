from django.db import models

from country.models import CountryModel


class AddressModel(models.Model):
    unit_number = models.CharField(max_length=100, null=True, blank=True)
    street_number = models.CharField(max_length=100, null=True, blank=True)
    address_line1 = models.TextField()
    address_line2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.ForeignKey(CountryModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.address_line1

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        db_table = "address"
