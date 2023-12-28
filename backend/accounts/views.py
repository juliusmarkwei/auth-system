from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User, EmailConfirmationToken
from .utils import send_confirmation_email


class UserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def get(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(request.user)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get("user", {})
        serializer = UserSerializer(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserInformationAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        email = user.email
        is_verified = user.is_verified
        
        payload = {"email": email, "is_verified": is_verified}
        return Response(data=payload, status=status.HTTP_200_OK)
    
    
class SendEmailConfirmationTokenAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        user = request.user
        token = EmailConfirmationToken.objects.create(user=user)
        send_confirmation_email(email=user.email, token_id=token.pk, user_id=user.pk)
        
        return Response(data=None, status=status.HTTP_201_CREATED)