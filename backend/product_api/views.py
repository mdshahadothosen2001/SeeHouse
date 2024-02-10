from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_list_or_404, get_object_or_404

from .serializers import ProductSerializer, ProductUpdateSerializer
from subcategory.models import Subcategory
from category.models import Category
from product.models import Product
from shop.models import Shop


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

        if not shop_name or not product_name or not product_code or not subcategory_name:
            raise ValidationError("Must required shop_name and product_name and product_code and subcategory") 
        
        shop_instance =  get_list_or_404(Shop, shop_name=shop_name.upper())
        subcategory_instance = get_list_or_404(Subcategory, subcategory_name=subcategory_name.upper())

        product_data = {
            "shop":shop_instance[0].id,
            "product_name":product_name,
            "product_code":product_code,
            "subcategory":subcategory_instance[0].id,
            "description":description,
            "stock":stock,
            "price":price,
            "rating":0
        }

        print("................", product_data)

        serializer = ProductSerializer(data=product_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"Created your product!"})
        else:
            return Response({"error":serializer.errors})


class ProductUpdateView(APIView):
    """Used for updating any existing product"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        id = request.data.get("id")

        if not  id:
            raise ValidationError("Must required product id") 
        
        product_instance =  get_object_or_404(Product, id=id)

        serializer = ProductUpdateSerializer(instance=product_instance, data=request.data, partial=True)
        print(serializer.is_valid(), serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"Updated your product!"})
        else:
            return Response({"error":serializer.errors})
