from django.conf import settings
from django.db import models
from django.utils.html import mark_safe

from subcategory.models import SubcategoryModel
from utils.models import CommonInfo
from shop.models import ShopModel


class ProductModel(CommonInfo):
    shop = models.ForeignKey(ShopModel, on_delete=models.DO_NOTHING)
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100, unique=True)
    subcategory = models.ForeignKey(SubcategoryModel, on_delete=models.DO_NOTHING)
    description = models.TextField()
    product_thumbnail = models.ImageField(
        upload_to="images/uploads/%Y/%m/%d", null=True, blank=True
    )
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)

    def thumbnail(self):
        if self.product_thumbnail != "":
            return mark_safe(
                '<img src="{}{}" width=auto height="20" />'.format(
                    f"{settings.MEDIA_URL}", self.product_thumbnail
                )
            )

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "product"
