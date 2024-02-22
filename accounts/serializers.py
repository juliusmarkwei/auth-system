from djoser import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer, CharField


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
        
        
class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
        
class GroupCreateSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']
        extra_kwargs = {
            'name': {'required': True}
        }
        
class AddUserToGroupSerializer(ModelSerializer):
    username = CharField(max_length=150, required=True)
    group = CharField(max_length=150, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'group']
        extra_kwargs = {
            'username': {'required': True},
            'group': {'required': True}
        }