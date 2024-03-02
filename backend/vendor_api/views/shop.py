from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK

from django.shortcuts import get_object_or_404
from django.core.cache import cache

from vendor_api.serializers.shop import (
    ServiceListSerializer,
    CreateServiceSerializer,
    UpdateServiceSerializer,
)
from shop_type.models import ShopTypeModel
from shop.models import ShopModel
from utils.utils import tokenValidation


class ServiceListView(APIView):
    """This class response service list"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        services = cache.get("services")
        if services is not None:
            return Response(services)
        services = ShopModel.objects.all()
        serializer = ServiceListSerializer(services, many=True)
        cache.set("services", [serializer.data], timeout=5)
        return Response(serializer.data, status=HTTP_200_OK)


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
        shop_type_object = get_object_or_404(ShopTypeModel, shop_type=shop_type)

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


class ServiceUpdateView(APIView):
    """This class permit to update their information about service"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        payload = tokenValidation(request)
        if payload.get("user_type") == "VENDOR":

            instance = ShopModel.objects.get(vendor=request.user.id)
            serializer = UpdateServiceSerializer(
                instance=instance, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response("Your shop information has been updated!")
            else:
                return Response("Please provide valid data")
        return Response("You have no permission to update product")
