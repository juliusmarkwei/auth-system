from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True)
    class Meta(object):
        model = User
        fields = (
            "id",
            "username",
            "is_verified",
            "email",
            "first_name",
            "last_name",
            "address",
            "phone",
            "date_joined",
            "updated_at",
            "password"
        )

        extra_kwargs = {"password": {"write_only": True}}
