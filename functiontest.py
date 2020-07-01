from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from selenium.webdriver.common.keys import Keys
import time
import unittest

MAX_WAIT = 10


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_go_to_blog_site(self):
        self.browser.get('http://localhost:8000')
        # check we are at the front page
        self.assertIn("Ludovico's Curriculum Vitae", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Ludovico's Curriculum Vitae", header_text)

        blog_button = self.browser.find_element_by_id('cv_blog_btn')
        blog_button.click()
        start_time = time.time()

        while True:
            try:
                self.assertIn("Ludovico's Blog", self.browser.title)
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_go_to_CV_site(self):
        self.browser.get('http://localhost:8000/blog')
        self.assertIn("Ludovico's Blog", self.browser.title)

        cv_button = self.browser.find_element_by_id('cv_blog_btn')
        cv_button.click()
        start_time = time.time()
        while True:
            try:
                self.assertIn("Ludovico's Curriculum Vitae", self.browser.title)
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_see_CV_entries(self):
        self.browser.get('http://localhost:8000')
        self.assertIn("Ludovico's Curriculum Vitae", self.browser.title)

        cv_entry = self.browser.find_elements_by_class_name("cv_entry")
        self.assertIn("Personal Details:", cv_entry)

    def test_can_log_in(self):
        self.browser.get('http://localhost:8000')
        log_in_btn = self.browser.find_element_by_id("login_btn")
        log_in_btn.click()
        time.sleep(1)  # todo: dont use magic sleeps
        # test user creds: testUser, qwertytest


if __name__ == '__main__':
    unittest.main(warnings='ignore')
