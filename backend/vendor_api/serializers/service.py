from rest_framework import serializers

from shop.models import ShopModel


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopModel
        fields = ["id", "shop_name", "shop_type", "shop_title", "fields", "rating"]
