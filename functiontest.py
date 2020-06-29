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

        blog_button = self.browser.find_element_by_id('blog_btn')
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


if __name__ == '__main__':
    unittest.main(warnings='ignore')
