from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_list_or_404

from category.models import Category


class ProductView(APIView):
    """This class returns product categories and subcategories with products as nested"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        categories = get_list_or_404(Category)

        product_response_data = {"categories": []}

        for category in categories:
            subcategories_data = []

            for subcategory in category.subcategory.all():
                products_data = []

                for product in subcategory.product.all():
                    product_data = {
                        "product_name": product.product_name,
                        "product_code": product.product_code,
                    }
                    products_data.append(product_data)

                subcategory_data = {
                    subcategory.subcategory_name: products_data
                }
                subcategories_data.append(subcategory_data)

            category_data = {
                "category_name": category.category_name,
                "subcategory_names": subcategories_data
            }

            product_response_data["categories"].append(category_data)

        return Response({"product":product_response_data})
