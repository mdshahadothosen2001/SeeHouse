from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_list_or_404

from shop.models import Shop


class ServiceView(APIView):
    """This class response service list"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        services = get_list_or_404(Shop)

        service_data = []
        for service in services:
            service_data += [
                {
                    "vendor":service.vendor.first_name,
                    "shop_name":service.shop_name,
                    "shop_number":service.shop_number,
                    "shop_type":service.shop_type.shop_type,
                    "shop_title":service.shop_title,
                    "fields":service.fields,
                    "service_started":service.service_started,
                    "about":service.about,
                    "rating":service.rating
                }
            ]
        
        return Response({"service":service_data})
