from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q

from .serializers import VendorCreateSerializer
from user.models import UserAccount


class VendorRegisterView(APIView):
    """This class used to creating new vendor"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        password = request.data.get("password")

        if not phone_number or not email or not password:
            raise ValidationError("Must required phone_number and email and password")

        # check this phone_number exists or email using complex query with OR operation,
        is_member = UserAccount.objects.filter(
            Q(phone_number=phone_number) | Q(email=email)
        ).values()
        if is_member:
            if len(is_member) != 0:
                return Response("You have already account at SeeHouse")

        serializer = VendorCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Completed your registration process")

        return Response("Incompleted your registration process")
