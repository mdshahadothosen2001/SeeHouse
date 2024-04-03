from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK

from django.core.cache import cache

from vendor_api.serializers.service import ServiceListSerializer
from shop.models import ShopModel


class ServiceListView(APIView):
    """Everybody can see service list"""

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        services = cache.get("services")
        if services is not None:
            return Response(services)
        services = ShopModel.objects.all()
        serializer = ServiceListSerializer(services, many=True)
        cache.set("services", [serializer.data], timeout=5)
        return Response(serializer.data, status=HTTP_200_OK)
