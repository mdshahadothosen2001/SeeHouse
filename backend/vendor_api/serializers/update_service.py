from rest_framework import serializers

from shop.models import ShopModel


class UpdateServiceByVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopModel
        fields = ["id", "shop_title", "fields", "about", "delivery_days"]
