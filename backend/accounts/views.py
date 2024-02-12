from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User, EmailConfirmationToken
from .utils import send_confirmation_email


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return User.objects.all()
    
    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(request.user, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    
    
class SendEmailConfirmationTokenAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        user = request.user
        if user != EmailConfirmationToken.objects.get(user=user).user:
            token = EmailConfirmationToken.objects.create(user=user)
        
        if user.is_verified:
            return Response({"message": "Email accournt already registerd with associated user"})
        else:
            token = EmailConfirmationToken.objects.get(user=user)
        send_confirmation_email(email=user.email, token_id=token.pk, user_id=user.pk)
        
        return Response(data=None, status=status.HTTP_201_CREATED)

