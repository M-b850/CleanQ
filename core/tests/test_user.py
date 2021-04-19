from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creates a new user with email address with an email successful"""
        email = 'ababs@Formaloo.com'
        password = 'my-password@'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'My-password@')

    def test_create_superuser(self):
        """Test creates a new super user"""
        email = 'ababs@Formaloo.com'
        password = 'my-password@'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

