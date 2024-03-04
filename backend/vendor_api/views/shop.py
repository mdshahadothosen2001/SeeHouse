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
            serializer = CreateServiceSerializer(
                data={**request.data, "vendor": vendor_id}
            )
            if serializer.is_valid():
                serializer.save()
                return Response("Successfully created this service!")
            else:
                return Response("Please provides valid data")
        return Response("You have no permission to update product")


class ServiceUpdateView(APIView):
    """This class permit to update their information about service"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        payload = tokenValidation(request)
        if payload.get("is_vendor") == True:

            instance = ShopModel.objects.get(vendor=payload.get("user_id"))
            serializer = UpdateServiceSerializer(
                instance=instance, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response("Your shop information has been updated!")
            else:
                return Response("Please provide valid data")
        return Response("You have no permission to update product")
