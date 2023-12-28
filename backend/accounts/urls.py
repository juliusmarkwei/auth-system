from django.urls import path
from .views import UserAPIView, UserRetrieveUpdateAPIView, authenticate_user

app_name = "accounts"

urlpatterns = [
    path("create/", UserAPIView.as_view()),
    path("update/", UserRetrieveUpdateAPIView.as_view()),
    path("obtain_token/", authenticate_user),
]