from django.test import TestCase, Client
from django.urls import reverse


class TestIndex(TestCase):

    def set(self):
        self.client = Client()

    # Test if find a club page is accessible
    def test_contact_accessible(self):
        response = self.client.get(reverse('clubmap'))

        self.assertTemplateUsed('scotDives/clubmap.html')


 # Test find a club map return right content
    def test_contact_content(self):
        response = self.client.get(reverse('clubmap'))

        self.assertTemplateUsed('scotDives/clubmap.html')

        self.assertContains(response,
                            "Click to Show Location")


