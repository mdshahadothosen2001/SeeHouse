from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_list_or_404

from .serializers import (
    ProductCategorySerializer,
    ProductSubcategorySerializer,
    ProductModelSerializer,
    ProductUpdateSerializer,
)
from subcategory.models import SubcategoryModel
from category.models import CategoryModel
from product.models import ProductModel
from shop.models import ShopModel
from utils.utils import tokenValidation


class ProductCategoryListView(APIView):
    """This class used to return category list"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        categories = CategoryModel.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductSubCategoryListView(APIView):
    """This class take 'category_id' one argument and then response subcategory list"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        category_id = request.data.get("category_id")
        if not category_id:
            raise ValidationError("Must Required category_id")

        subcategories = SubcategoryModel.objects.filter(category_id=category_id)
        serializer = ProductSubcategorySerializer(subcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListView(APIView):
    """This class returns product categories and subcategories with products as nested"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        subcategory_id = request.data.get("subcategory_id")
        if not subcategory_id:
            raise ValidationError("Must Required subcategory_id")

        products = ProductModel.objects.filter(subcategory_id=subcategory_id)
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    """Used for creating new product"""

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        shop_name = request.data.get("shop_name")
        product_name = request.data.get("product_name")
        product_code = request.data.get("product_code")
        subcategory_name = request.data.get("subcategory_name")
        description = request.data.get("description")
        stock = request.data.get("stock")
        price = request.data.get("price")

        if (
            not shop_name
            or not product_name
            or not product_code
            or not subcategory_name
        ):
            raise ValidationError(
                "Must required shop_name and product_name and product_code and subcategory"
            )

        shop_instance = get_list_or_404(ShopModel, shop_name=shop_name)
        subcategory_instance = get_list_or_404(
            SubcategoryModel, subcategory_name=subcategory_name.upper()
        )

        product_data = {
            "shop": shop_instance[0].id,
            "product_name": product_name,
            "product_code": product_code,
            "subcategory": subcategory_instance[0].id,
            "description": description,
            "stock": stock,
            "price": price,
            "rating": 0,
        }

        serializer = ProductModelSerializer(data=product_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "Created your product!"})
        else:
            return Response({"error": serializer.errors})


class ProductUpdateView(APIView):
    """Used for updating any existing product"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        payload = tokenValidation(request)
        if payload.get("user_type") == "VENDOR":
            id = request.data.get("id")

            if not id:
                raise ValidationError("Must required product id")

            instance = ProductModel.objects.get(id=id)

            serializer = ProductUpdateSerializer(instance, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response("Updated your product!")
            else:
                return Response("Please provides valid data")
        return Response("You have no permission to create product")
