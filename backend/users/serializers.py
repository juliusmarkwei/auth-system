from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True)
    class Meta(object):
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "address",
            "telephone",
            "date_joined",
            "password",
        )

        extra_kwargs = {"password": {"write_only": True}}
