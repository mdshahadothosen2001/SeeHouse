from django.db import models

from product.models import Product


class Subcategory(models.Model):
    product = models.ManyToManyField(Product)
    subcategory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "product Subcategory"
        verbose_name_plural = "Product Subcategories"
        db_table = "subcategory"
