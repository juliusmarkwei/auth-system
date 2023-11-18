from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateAPIView
from .models import User
from rest_framework_jwt.utils import jwt, jwt_payload_handler
from core import settings
from django.contrib.auth.signals import user_logged_in


class CreateUserAPIView(ListCreateAPIView):
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


@api_view(["POST"])
@permission_classes(
    [
        AllowAny,
    ]
)
def authenticate_user(request):
    try:
        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.get(email=email, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details["name"] = "%s %s" % (user.first_name, user.last_name)
                user_details["token"] = token
                user_logged_in.send(sender=user.__class__, request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                raise e
        else:
            res = {
                "error": "can not authenticate with the given credentials or the account has been deactivated"
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)

    except KeyError:
        res = {"error": "please provide a email and a password"}
        return Response(res)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that

        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get("user", {})
        serializer = UserSerializer(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
