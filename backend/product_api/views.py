from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404, get_list_or_404

from subcategory.models import Subcategory
from category.models import Category
from product.models import Product


class ProductView(APIView):
    """This class returns product categories and subcategories with products as nested"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        subcategory_id = request.data.get("subcategory")
        if not subcategory_id:
            raise ValueError("Must Required subcategory id")
        
        subcategory_data = get_object_or_404(Subcategory, id=subcategory_id)
        
        products = get_list_or_404(Product)
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
