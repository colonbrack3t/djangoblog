from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from CV.models import CV_Entry, PersonalDetails


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

    def test_can_auth_user(self):
        user = User.objects.create(username="a")
        user.set_password("1234")
        user.save()
        self.assertTrue(self.client.login(username="a", password="1234"))

    def test_cannot_create_multiple_Personal_Details(self):
        pd1 = PersonalDetails.objects.create(name="Joe Bloggs", dob=datetime.now(), contactNumber="12345678900")
        pd2 = PersonalDetails.objects.create(name="Jane Bloggs", dob=datetime.now(), contactNumber="12345678900")
        self.assertEqual(PersonalDetails.objects.all().count(), 1)
        self.assertEqual(pd1.name, PersonalDetails.objects.first().name)
        self.assertNotEqual(pd2.name, PersonalDetails.objects.first().name)

    def test_display_personal_details(self):
        name = "joe blogs"
        dob = datetime.now()
        no = "12345678900"
        pd = PersonalDetails.objects.create(name=name, dob=dob, contactNumber=no)
        pd.save()
        response = self.client.get('/')
        html = response.content.decode()
        self.assertIn(name, html)
        self.assertIn(dob.strftime("%#d %b %Y"), html)  # default Django DateField format
        self.assertIn(no, html)

    def test_create_entry_returns_correct_html(self):
        response = self.client.get('/new/CV_Entry')
