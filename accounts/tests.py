from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class UserRegistrationTest(TestCase):
    def test_registration_form(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'Complexpass123',
            'password2': 'Complexpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertTrue(User.objects.filter(username='testuser').exists())
