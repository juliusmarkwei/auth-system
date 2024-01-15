from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
from accounts.models import EmailConfirmationToken
from rest_framework import status


class TestUserView(APITestCase):
    client = APIClient()
    User = get_user_model()
    
    def test_user_informatoin_api_view_requires_authentication(self):
        url = reverse("accounts:user_information_api_view")
        reponse = self.client.get(url)
        self.assertEqual(reponse.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_send_confirmation_email_requires_authentication(self):
        url = reverse("accounts:send_confirmation_email")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_send_email_confirmation_api_view_create_token(self):
        user = self.User.objects.create_user(
            email="banauz@erjunire.cf",
            username="banauz",
            first_name="Banauz",
            last_name="Erjunire",
            password="12345678",
            phone="12345678",
        )
        url = reverse("accounts:send_confirmation_email")
        self.client.force_authenticate(user=user)
        reponse = self.client.post(url)
        self.assertEqual(reponse.status_code, status.HTTP_201_CREATED)
        token = EmailConfirmationToken.objects.filter(user=user).first()
        self.assertIsNotNone(token)
        
