from django.urls import path
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView

app_name = "users"

urlpatterns = [
    path("create/", CreateUserAPIView.as_view()),
    path("update/", UserRetrieveUpdateAPIView.as_view()),
]
