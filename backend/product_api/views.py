from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_list_or_404

from subcategory.models import Subcategory
from category.models import Category
from product.models import Product


class ProductView(APIView):
    """This class returns product categories and subcategories with products as nested"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        subcategory_id = request.data.get("subcategory_id")
        if not subcategory_id:
            raise ValidationError("Must Required subcategory_id")
        
        products = get_list_or_404(Product, subcategory=subcategory_id)
        products_data = []
    
        for product in products:
            products_data += [{
                "id":product.id,
                "shop_name":product.shop.shop_name,
                "product_name":product.product_name,
                "product_code":product.product_code,
                "description":product.description,
                "stock":product.stock,
                "price":product.price,
                "rating":product.rating
            }]

        return Response({"product":products_data})


class ProductCategoryView(APIView):
    """This class used to return category list"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        categories = get_list_or_404(Category)

        category_data = []
        for category in categories:
            category_data += [
                {
                    "category_id":category.id,
                    "category_name":category.category_name
                }
            ]
        return Response(category_data)


class ProductSubCategoryView(APIView):
    """This class take 'category_id' one argument and then response subcategory list """

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        category_id = request.data.get("category_id")
        if not category_id:
            raise ValidationError("Must Required category_id")

        subcategories = get_list_or_404(Subcategory, category=category_id)

        subcategory_data = []
        for subcategory in subcategories:
            subcategory_data += [
                {
                    "id":subcategory.id,
                    "subcategory_name":subcategory.subcategory_name
                }
            ]

        return Response({"subcategory":subcategory_data})
