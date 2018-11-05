from django.test import TestCase
from django.urls import resolve
from django.shortcuts import resolve_url as r

from places.models import HistoricPlaces
from places.views import home_page


class HomePageTest(TestCase):
    """Tests for Home Page"""
    def setUp(self):
        self.point = HistoricPlaces.objects.create(
            title='ponto 1',
            description='monumento erguido em homenagem aos heróis da guerra',
            latitude=43.300,
            longitude=12.020,
        )
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_root_url_resolves_to_home_page_view(self):
        """home_page url should use home_page view"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_template(self):
        """home_page should use home.html template"""
        self.assertTemplateUsed(self.response, 'places/home.html')
