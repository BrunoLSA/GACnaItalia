from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve
from places.views import home_page


class HomePageTest(TestCase):
    '''Tests for Home Page'''

    def test_root_url_resolves_to_home_page_view(self):
        '''home_page url should use home_page view'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'places/home.html')