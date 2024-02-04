from rest_framework import serializers

from shop.models import Shop


class CreateServiceSerializer(serializers.ModelSerializer):
    """It is serializing data then save to shop model"""

    class Meta:
        model = Shop
        fields = ["vendor", "shop_number", "shop_name", "shop_type", "shop_title", "fields", "about", "service_started", "rating", "is_active"]


class UpdateServiceSerializer(serializers.ModelSerializer):
    """It is serializing data then save to shop model for updating service information"""

    class Meta:
        model = Shop
        fields = ["id", "shop_title", "fields", "about", "delivery_days"]
