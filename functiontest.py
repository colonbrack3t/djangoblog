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

    def test_can_go_to_blog_site_and_cv(self):
        self.browser.get('http://localhost:8000')
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

    def test_can_log_in_and_create_cv_entry(self):
        self.browser.get('http://localhost:8000')
        log_in_btn = self.browser.find_element_by_id("login_btn")
        log_in_btn.click()
        start_time = time.time()
        while True:
            try:
                usernameField = self.browser.find_element_by_id("id_username")
                passwordField = self.browser.find_element_by_id("id_password")
                break
            except (WebDriverException, AttributeError) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
        usernameField.send_keys("testUser")
        passwordField.send_keys("qwertytest")
        submitBtn = self.browser.find_element_by_id("login_submit")
        submitBtn.click()
        start_time = time.time()
        while True:
            try:
                self.assertIn("Hello testUser", self.browser.find_element_by_id("usergreeting").text)
                break
            except (WebDriverException, AttributeError) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
