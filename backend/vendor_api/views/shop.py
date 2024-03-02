from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK

from django.core.cache import cache

from vendor_api.serializers.shop import (
    ServiceListSerializer,
    CreateServiceSerializer,
    UpdateServiceSerializer,
)
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
        payload = tokenValidation(request)
        if payload.get("is_vendor") == True:
            vendor_id = payload.get("user_id")
            shop_number = request.data.get("shop_number")
            shop_name = request.data.get("shop_name")
            shop_title = request.data.get("shop_title")
            fields = request.data.get("fields")
            service_started = request.data.get("service_started")
            about = request.data.get("about")
            shop_type_id = request.data.get("shop_type_id")

            if (
                not shop_name
                or not shop_number
                or not shop_type_id
                or not service_started
            ):
                raise ValidationError(
                    "Must required shop_name, shop_number, shop_type_id, service_started"
                )

            shop_data = {
                "vendor": vendor_id,
                "shop_name": shop_name.upper(),
                "shop_number": shop_number,
                "shop_type": shop_type_id,
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
                return Response("Please provides valid data")


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
