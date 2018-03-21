from django.test import TestCase, Client
from django.urls import reverse


class TestIndex(TestCase):

    def set(self):
        self.client = Client()

    # Test if search page is accessible
    def test_contact_accessible(self):
        response = self.client.get(reverse('search'))

        self.assertTemplateUsed('scotDives/search.html')


 # Test search page content
    def test_contact_content(self):
        response = self.client.get(reverse('search'))

        self.assertTemplateUsed('scotDives/search.html')
        self.assertContains(response,
            "<input type='text' name='q' placeholder='Search pages' value=''/>")


