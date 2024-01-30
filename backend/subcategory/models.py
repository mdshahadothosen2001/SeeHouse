from django.db import models

from category.models import Category


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    subcategory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subcategory_name
    
    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
        db_table = "subcategory"
