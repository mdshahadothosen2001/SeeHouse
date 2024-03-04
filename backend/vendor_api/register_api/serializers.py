from rest_framework import serializers

from user.models import Vendor


class VendorCreateSerializer(serializers.ModelSerializer):
    """This class serializing the data for new creating vendor user"""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = Vendor
        fields = [
            "id",
            "phone_number",
            "email",
            "is_vendor",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.is_vendor = True
        user.save()

        return user
