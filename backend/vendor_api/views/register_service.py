from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..serializers.register_service import CreateServiceByVendorSerializer
from utils.utils import tokenValidation


class CreateServiceByVendorView(APIView):
    """This class used to creating new shop that means service"""

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        payload = tokenValidation(request)
        if payload.get("is_vendor") == True:
            vendor_id = payload.get("user_id")
            serializer = CreateServiceByVendorSerializer(
                data={**request.data, "vendor": vendor_id}
            )
            if serializer.is_valid():
                serializer.save()
                return Response("Successfully created this service!")
            else:
                return Response(
                    "Please provides valid data", status=status.HTTP_201_CREATED
                )
        return Response(status=status.HTTP_400_BAD_REQUEST)
