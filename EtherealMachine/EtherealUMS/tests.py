from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.username = 'test1'
        self.password = 'test987654'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        # Define the login URL
        url = reverse('login')  # Use the name you provided in urls.py
        data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(url, data, format='json')

        # Assert that the login was successful and a token is returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_failure_invalid_credentials(self):
        # Define the login URL
        url = reverse('login')  # Use the name you provided in urls.py
        data = {
            'username': self.username,
            'password': 'wrongpassword'  # Use a wrong password
        }
        response = self.client.post(url, data, format='json')

        # Assert that the login failed
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Invalid credentials')

    def test_login_failure_user_not_found(self):
        # Define the login URL
        url = reverse('login')  # Use the name you provided in urls.py
        data = {
            'username': 'nonexistentuser',  # Use a username that doesn't exist
            'password': 'testpassword123'
        }
        response = self.client.post(url, data, format='json')

        # Assert that the login failed
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Invalid credentials')
