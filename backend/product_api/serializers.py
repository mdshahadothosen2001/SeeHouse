from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """This class serializing data for product model"""

    class Meta:
        model = Product
        fields = [
            "id",
            "shop",
            "product_name",
            "product_code",
            "subcategory",
            "description",
            "stock",
            "price",
            "rating",
        ]


class ProductUpdateSerializer(serializers.ModelSerializer):
    """This class serializing data for product model objects update"""

    class Meta:
        model = Product
        fields = ["description", "stock", "price", "rating", "is_active"]
