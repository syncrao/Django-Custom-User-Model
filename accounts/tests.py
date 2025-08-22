from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class AuthenticationBackendTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="rao",
            email="rao@test.com",
            phone="1234567890",
            password="pass123"
        )

    def test_login_with_username(self):
        user = authenticate(username="rao", password="pass123")
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)

    def test_login_with_email(self):
        user = authenticate(username="rao@test.com", password="pass123")
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)

    def test_login_with_phone(self):
        user = authenticate(username="1234567890", password="pass123")
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)

    def test_login_wrong_password(self):
        user = authenticate(username="rao", password="wrongpass")
        self.assertIsNone(user)

    def test_login_nonexistent_user(self):
        user = authenticate(username="nouser", password="pass123")
        self.assertIsNone(user)
