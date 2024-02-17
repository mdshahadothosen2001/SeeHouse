from django.db import models

from address.models import AddressModel
from user.models import UserAccount


class UserAddressModel(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(AddressModel, on_delete=models.DO_NOTHING)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"user: {self.user} - address: {self.address}"

    class Meta:
        verbose_name = "User Address"
        verbose_name_plural = "User Addresses"
        db_table = "user_address"
