from django.conf import settings
from django.db import models
from django.utils.html import mark_safe

from user.models import Vendor
from utils.models import TimeStamp
from shop_type.models import ShopTypeModel


class ShopModel(TimeStamp):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    shop_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    shop_name = models.CharField(max_length=100, unique=True)
    shop_type = models.ForeignKey(
        ShopTypeModel, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    shop_title = models.CharField(max_length=100, null=True, blank=True)
    fields = models.CharField(max_length=100, null=True, blank=True)
    service_started = models.DateField(auto_now=False, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    delivery_days = models.PositiveSmallIntegerField(null=True, blank=True)
    cover_photo = models.ImageField(
        upload_to="images/uploads/shop_cover_photo", null=True, blank=True
    )
    rating = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def cover_image(self):
        if self.cover_photo != "":
            return mark_safe(
                '<img src="{}{}" width=auto height="20" />'.format(
                    f"{settings.MEDIA_URL}", self.cover_photo
                )
            )

    def __str__(self):
        return self.shop_name

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"
        db_table = "shop"
