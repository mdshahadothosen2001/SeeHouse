from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from datetime import datetime


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """This class is a custom serializer for obtaining authentication token"""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["phone_number"] = user.phone_number
        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["user_type"] = user.user_type
        token["is_active"] = user.is_active
        token["is_vendor"] = user.is_vendor
        token["is_staff"] = user.is_staff
        token["current_date"] = datetime.now().strftime("%Y:%m:%d")
        current_time = datetime.now().strftime("%I:%M:%p")
        token["current_time"] = current_time

        if "AM" in current_time:
            token["day_status"] = "Day"
        else:
            token["day_status"] = "Night"

        return token
