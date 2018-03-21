from urllib import response

from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import auth
from scotDives.models import UserProfile


class TestUser(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create(username="user1")
        self.user.first_name = "first"
        self.user.last_name = "last"
        self.user.email = "test@test.com"
        self.user.password = make_password("password")

        self.user.save()

        self.profile = UserProfile(user=self.user)
        self.profile.save()

        self.client = Client()

    # Test if user exist
    def test_user_exists(self):
        self.assertIsNotNone(self.user, "User not null")
        profile = self.user.userprofile
        self.assertIsNotNone(profile, "Profile not null")


    # Test if user is logged in
    def test_user_login(self):
        self.client.login(username="user1", password="password")

        user = auth.get_user(self.client)

        self.assertTrue(user.is_authenticated(), "User is authenticated")


    # Test if logged in users see Welcome message in the index page
    def test_login_welcome(self):
        self.client.login(username="user1", password="password")

        user = auth.get_user(self.client)

        response = self.client.get(reverse('index'))
        self.assertTemplateUsed('scotDives/index.html')
        self.assertContains(response, "Welcome to ScotDives")


    # Test if User is logged out
    def test_user_logout(self):
        self.client.login(username="user1", password="password")

        user = auth.get_user(self.client)

        self.client.logout()
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated(), "User not authenticated after log out")
        self.assertTrue(user.is_anonymous(), "User is anonymous after log out")
