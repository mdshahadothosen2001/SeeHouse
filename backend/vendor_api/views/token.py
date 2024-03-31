from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from ..serializers.token import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """User can get access token and refresh token by thier email and password"""

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
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
