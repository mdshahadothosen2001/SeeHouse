from rest_framework import serializers

from category.models import CategoryModel
from product.models import ProductModel

class ProductCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "category_name"]


class ProductSerializer(serializers.ModelSerializer):
    """This class serializing data for product model"""

    class Meta:
        model = ProductModel
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
        model = ProductModel
        fields = ["description", "stock", "price", "rating", "is_active"]
