from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_go_to_blog(self):
        response = self.client.get('/blog')
        self.assertEqual(response.status_code, 301)
