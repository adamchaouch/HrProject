from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class AuthAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('usermanagement:create_user')
        self.login_url = reverse('usermanagement:token_obtain_pair')
        self.user_data = {
            "email": "test@example.com",
            "user_name": "testuser",
            "first_name": "Test",
            "password": "testpassword",
            "is_freelancer": True,
            "is_client": False,
            "is_job_seeker": False,
            "about": "I am a test user.",
            "is_active":True
            }

    def test_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        

    def test_login(self):
        user = User.objects.create_user(**self.user_data)
        login_data = {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        }
        response = self.client.post(self.login_url, login_data, format='json')
        print(response,login_data),
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the token is present in the response

    # Create similar test methods for token refresh and logout if needed
