from djoser import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserCreateSerializer(serializers.UserCreateSerializer):
    class Meta(serializers.UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 're_password', 'phone', 'is_active', 'is_phone_verified']
        extra_kwargs = {
            'password': {'write_only': True},
            're_password': {'write_only': True},
            'is_active': {'read_only': True},
            'is_phone_verified': {'read_only': True},
        }
        