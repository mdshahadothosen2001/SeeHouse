from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CustomerSerializer
from user.models import Customer


class CustomerRegisterView(APIView):
    """This class creating new user as customer"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password = request.data.get("password")

        if not phone_number or not email or not password:
            raise ValidationError("Must required phone_number and email and password")
        
        is_member = Customer.objects.filter(phone_number=phone_number).values()
        if len(is_member) !=0:
            return Response("You have already account at SeeHouse")
        
        customer_data = {
            "phone_number":phone_number,
            "email":email,
            "first_name":first_name,
            "last_name":last_name,
            "is_customer":True,
            "password":password
        }

        serializer = CustomerSerializer(data=customer_data)
        if serializer.is_valid():
            serializer.save()

            return Response("Completed your registration process!")

        return Response("Incompleted registration, Please provide valid data")