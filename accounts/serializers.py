from djoser import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserCreateSerializer(serializers.UserCreateSerializer):
    class Meta(serializers.UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 're_password', 'phone']
        
        
class UserSerializer(serializers.UserSerializer):
    class Meta(serializers.UserSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'phone']

