from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import (
    ProductCategoryListSerializer,
    ProductSubcategoryListSerializer,
    ProductListSerializer,
    ProductUpdateSerializer,
)
from subcategory.models import SubcategoryModel
from category.models import CategoryModel
from product.models import ProductModel
from utils.utils import tokenValidation


class ProductCategoryListView(APIView):
    """This class used to return category list"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        categories = CategoryModel.objects.all()
        serializer = ProductCategoryListSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductSubCategoryListView(APIView):
    """This class take 'category_id' one argument and then response subcategory list"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        category_id = request.query_params.get("category_id")
        if not category_id:
            raise ValidationError("Must Required category_id")

        subcategories = SubcategoryModel.objects.filter(category_id=category_id)
        serializer = ProductSubcategoryListSerializer(subcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListView(APIView):
    """This class returns product categories and subcategories with products as nested"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        subcategory_id = request.data.get("subcategory_id")
        if not subcategory_id:
            raise ValidationError("Must Required subcategory_id")

        products = ProductModel.objects.filter(subcategory_id=subcategory_id)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    """Used for creating new product"""

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        payload = tokenValidation(request)
        if payload.get("user_type") == "VENDOR":
            serializer = ProductListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Created your product!")
            else:
                return Response("Please provides valid data")
        return Response("You have no permission to create product")


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
        return Response("You have no permission to update product")
