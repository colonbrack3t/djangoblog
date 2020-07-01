from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from CV.models import CV_Entry


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_go_to_blog(self):
        response = self.client.get('/blog')
        self.assertEqual(response.status_code, 301)

    def test_display_all_cv_entries(self):
        CV_Entry.objects.create(text="item1", title="Item1")
        CV_Entry.objects.create(text="item2", title="Item2")

        response = self.client.get('/')
        self.assertIn('item1', response.content.decode())
        self.assertIn('item2', response.content.decode())

    def test_only_get_one_type_of_entry(self):

