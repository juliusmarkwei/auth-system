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
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        # Adding the below line made it work for me.
        instance.is_active = True
        if password is not None:
            # Set password does the hash, so you don't need to call make_password 
            instance.set_password(password)
        instance.save()
        return instance

