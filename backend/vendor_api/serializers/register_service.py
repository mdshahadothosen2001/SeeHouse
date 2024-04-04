from rest_framework import serializers

from shop.models import ShopModel


class CreateServiceByVendorSerializer(serializers.ModelSerializer):
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
