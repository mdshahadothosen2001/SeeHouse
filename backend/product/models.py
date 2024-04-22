from django.db import models

from utils.models import CommonInfo
from shop.models import ShopModel
from category.models import CategoryModel
from subcategory.models import SubcategoryModel


class ProductModel(CommonInfo):
    shop = models.ForeignKey(ShopModel, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    subcategory = models.ForeignKey(SubcategoryModel, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200)
    detail = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    points = models.PositiveSmallIntegerField(null=True, blank=True)
    thumbnail = models.URLField()
    images = models.JSONField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "product"
