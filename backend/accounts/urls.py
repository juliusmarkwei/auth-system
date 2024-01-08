from django.urls import path
from .views import UserAPIView, SendEmailConfirmationTokenAPIView, UserInformationAPIView

app_name = "accounts"

urlpatterns = [
    path("", UserAPIView.as_view()),
    path("me/", UserInformationAPIView.as_view(), name="user_information_api_view"),
    path("send-confirmation-email/", SendEmailConfirmationTokenAPIView.as_view(), name="send_confirmation_email"),
]

