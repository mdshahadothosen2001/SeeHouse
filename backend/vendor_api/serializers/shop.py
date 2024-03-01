from rest_framework import serializers

from shop.models import ShopModel


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopModel
        fields = ["id", "shop_name", "shop_type", "shop_title", "fields", "rating"]


class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopModel
        fields = [
            "vendor",
            "shop_number",
            "shop_name",
            "shop_type",
            "shop_title",
            "fields",
            "about",
            "service_started",
            "rating",
            "is_active",
        ]


class UpdateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopModel
        fields = ["id", "shop_title", "fields", "about", "delivery_days"]
