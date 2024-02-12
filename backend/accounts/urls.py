from django.urls import path
from .views import UserAPIView, SendEmailConfirmationTokenAPIView

app_name = "accounts"

urlpatterns = [
    path("", UserAPIView.as_view()),
    path("send-confirmation-email", SendEmailConfirmationTokenAPIView.as_view(), name="send_confirmation_email"),
]
