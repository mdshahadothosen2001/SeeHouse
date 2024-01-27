from rest_framework import serializers

from user.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """This serializer class used to serializing the customer model"""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ["id", "phone_number", "email", "first_name", "last_name", "is_customer", "password"]
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user
