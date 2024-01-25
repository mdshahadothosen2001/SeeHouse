from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """This class is a custom serializer for obtaining authentication token"""

    @classmethod
    def get_token(cls, user):
        """Used to get token and set user data"""

        token = super().get_token(user)
        token["phone_number"] = user.phone_number
        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["user_type"] = user.user_type
        token["current_date"] = datetime.now().strftime("%Y:%m:%d")
        current_time = datetime.now().strftime("%I:%M:%p")
        token["current_time"] = current_time

        if "AM" in current_time:
            token["day_status"] = "Day"
        else:
            token["day_status"] = "Night"

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    """User can get access token and refresh token by thier email and password"""

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """Used to return access token and refresh token"""

        response = super().post(request, *args, **kwargs)
        access_token = str(response.data["access"])
        refresh_token = str(response.data["refresh"])

        token_data = {
            "access": access_token,
            "refresh": refresh_token,
        }

        token = access_token
        request.session["token"] = token

        return Response(token_data)


class login_view(APIView):
    """User can loggin with access token"""

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Used to return success message"""

        return Response({"message": "Welcome to the SeeHouse!"})
