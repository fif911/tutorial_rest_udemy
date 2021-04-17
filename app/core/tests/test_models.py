# we have to use this function to get user model (not directly User)
from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@example.com"
        password = "Testpass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalized
        Just for tutorial. (Don't works for me without normalizing anyway)
        """
        email = "test@EXAMPLE.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password='password',
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        # means everything we run here should raise ValueError.
        # If it doesnt - test will fail
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="",
                password="password",
            )

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="password",
            )

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            email="admin@admin.com",
            password="password",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)