from rest_framework import serializers

from user.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    """This class serializing the data for new creating vendor user"""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = Vendor
        fields = [
            "id",
            "phone_number",
            "email",
            "first_name",
            "last_name",
            "tin_number",
            "is_vendor",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user
