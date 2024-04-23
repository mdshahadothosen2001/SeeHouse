from django.db import models

from category.models import CategoryModel


class SubcategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.category.name} : {self.name}"

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
        db_table = "subcategory"
