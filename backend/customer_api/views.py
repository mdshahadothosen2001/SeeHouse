from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q

from .serializers import CustomerCreateSerializer
from user.models import UserAccount


class CustomerRegisterView(APIView):
    """This class creating new user as customer"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = CustomerCreateSerializer(
            data={**request.data, "is_customer": True}
        )
        if serializer.is_valid():
            serializer.save()

            return Response("Completed your registration process!")

        return Response("Incompleted registration, Please provide valid data")
