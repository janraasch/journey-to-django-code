from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import TestCase

from .models import Wish


class WishTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

    def test_wish_show(self):
        response = self.client.get(reverse("wishes:home"))
        self.assertContains(response, "I want to be a Django developer")

    def test_wish_update(self):
        response = self.client.post(reverse("wishes:home"), {"text": "I don't wanna be a fool!"})
        self.assertRedirects(response, reverse("wishes:home"))
        self.assertEqual(Wish.objects.get(user=self.user).text, "I don't wanna be a fool!")
