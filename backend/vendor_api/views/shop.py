from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK

from vendor_api.serializers.shop import (
    UpdateServiceSerializer,
)
from shop.models import ShopModel
from utils.utils import tokenValidation


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
