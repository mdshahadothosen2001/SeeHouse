from django.db import models


class ShopType(models.Model):
    shop_type = models.CharField(max_length=100)

    def __str__(self):
        return self.shop_type
    
    class Meta:
        verbose_name = "Shop Type"
        verbose_name_plural = "Shop types"
        db_table = "shop_type"
