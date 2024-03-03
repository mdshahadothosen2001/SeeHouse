from rest_framework import serializers

from category.models import CategoryModel
from subcategory.models import SubcategoryModel
from product.models import ProductModel


class ProductCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "category_name"]


class ProductSubcategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcategoryModel
        fields = ["id", "subcategory_name"]


class ProductListSerializer(serializers.ModelSerializer):
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
        ]


class ProductUpdateSerializer(serializers.ModelSerializer):
    """This class serializing data for product model objects update"""

    class Meta:
        model = ProductModel
        fields = ["description", "stock", "price", "rating", "is_active"]
