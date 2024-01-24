from django.db import models

from subcategory.models import Subcategory


class Category(models.Model):
    subcategory = models.ManyToManyField(Subcategory)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = "product Category"
        verbose_name_plural = "Product Categories"
        db_table = "category"
