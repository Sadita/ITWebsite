from django.test import TestCase, Client
from django.urls import reverse


class TestIndex(TestCase):

    def set(self):
        self.client = Client()

    # Test if contact page is accessible
    def test_contact_accessible(self):
        response = self.client.get(reverse('contact'))

        self.assertTemplateUsed('scotDives/clubmap.html')


 # Test contact page content
    def test_contact_content(self):
        response = self.client.get(reverse('contact'))

        self.assertTemplateUsed('scotDives/clubmap.html')
        self.assertContains(response,
            "If you would like to get in touch, please use the following email address:")

