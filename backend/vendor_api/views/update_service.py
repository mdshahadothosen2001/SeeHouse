from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from shop.models import ShopModel
from utils.utils import tokenValidation
from utils.custom_permission import IsVendor
from ..serializers.update_service import UpdateServiceByVendorSerializer


class UpdateServiceByVendorView(APIView):
    """This class permit to update their information about service"""

    permission_classes = [IsVendor]

    def patch(self, request, *args, **kwargs):
        payload = tokenValidation(request)
        instance = ShopModel.objects.get(vendor=payload.get("user_id"))
        serializer = UpdateServiceByVendorSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                "Your shop information has been updated!", status=status.HTTP_200_OK
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)
