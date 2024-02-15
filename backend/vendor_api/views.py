from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_list_or_404, get_object_or_404

from .serializers import CreateServiceSerializer, UpdateServiceSerializer
from shop_type.models import ShopType
from shop.models import Shop


class CreateServiceView(APIView):
    """This class used to creating new shop that means service"""

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        vendor_id = request.user.id
        shop_number = request.data.get("shop_number")
        shop_name = request.data.get("shop_name")
        shop_title = request.data.get("shop_title")
        fields = request.data.get("fields")
        service_started = request.data.get("service_started")
        about = request.data.get("about")
        shop_type = request.data.get("shop_type")

        if not shop_name or not shop_number or not shop_type or not service_started:
            raise ValidationError("Must fulfil the required value")

        shop_type = shop_type.upper()
        shop_type_object = get_object_or_404(ShopType, shop_type=shop_type)

        shop_data = {
            "vendor": vendor_id,
            "shop_name": shop_name.upper(),
            "shop_number": shop_number,
            "shop_type": shop_type_object.id,
            "shop_title": shop_title,
            "fields": fields,
            "about": about,
            "service_started": service_started,
            "rating": 0,
            "is_active": True,
        }

        serializer = CreateServiceSerializer(data=shop_data)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully created this service!")
        else:
            return Response({"error": serializer.errors})


class ServiceView(APIView):
    """This class response service list"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        services = get_list_or_404(Shop)

        service_data = []
        for service in services:
            service_data += [
                {
                    "vendor": service.vendor.first_name,
                    "shop_name": service.shop_name,
                    "shop_number": service.shop_number,
                    "shop_type": service.shop_type.shop_type,
                    "shop_title": service.shop_title,
                    "fields": service.fields,
                    "service_started": service.service_started,
                    "about": service.about,
                    "rating": service.rating,
                }
            ]

        return Response({"service": service_data})


class ServiceUpdateView(APIView):
    """This class permit to update their information about service"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):

        instance = get_object_or_404(Shop, vendor=request.user.id)
        serializer = UpdateServiceSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response("Your information has been updated!")
        else:
            return Response({"error": serializer.errors})
