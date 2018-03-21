from django.test import TestCase, Client
from django.urls import reverse


class TestIndex(TestCase):

    def set(self):
        self.client = Client()

    # Test if about page is accessible
    def test_about(self):
        response = self.client.get(reverse('index'))

        self.assertTemplateUsed('scotDives/index.html')

    # Test if divemap page is accessible
    def test_divemap(self):
        response = self.client.get(reverse('divemap'))

        self.assertTemplateUsed('scotDives/divemap.html')


    # Test if photogallery page is accessible
    def test_photogallery(self):
        response = self.client.get(reverse('photogallery'))

        self.assertTemplateUsed('scotDives/photogallery.html')

    # Test if divesites page is accessible
    def test_divesites(self):
        response = self.client.get(reverse('divesites'))

        self.assertTemplateUsed('scotDives/divesites.html')


    # Test if clubmap page is accessible
    def test_clubmap(self):
        response = self.client.get(reverse('clubmap'))

        self.assertTemplateUsed('scotDives/clubmap.html')


    # Test if sitemap page is accessible
    def test_sitemap(self):
        response = self.client.get(reverse('sitemap'))

        self.assertTemplateUsed('scotDives/sitemap.html')