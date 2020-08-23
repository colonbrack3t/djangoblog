from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from selenium.webdriver.common.keys import Keys
import time
import unittest

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_go_to_blog_site_and_cv(self):
        self.browser.get(self.live_server_url)
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

    def test_can_log_in_and_create_cv_entry_and_edit_and_delete_and_log_out(self):
        self.browser.get(self.live_server_url)
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

        user = User.objects.create(username="testUser")
        user.set_password("qwertytest")
        user.save()
        usernameField.send_keys("testUser")
        passwordField.send_keys("qwertytest")
        submitBtn = self.browser.find_element_by_id("login_submit")
        submitBtn.click()
        self.checkIfAtHome()
        cvnew = self.browser.find_element_by_id("cvnew")
        cvnew.click()
        start_time = time.time()
        while True:
            try:
                eh = self.browser.find_element_by_id("editorHeader")
                self.assertIn("New CV Entry", eh.text)
                break
            except (WebDriverException, AttributeError) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
        id_text = self.browser.find_element_by_id('id_text')
        id_title = self.browser.find_element_by_id('id_title')
        submit = self.browser.find_element_by_id('id_submit')
        id_title.send_keys("Test Entry")
        id_text.send_keys("lorem ispum")
        submit.click()
        self.checkIfAtHome()
        title = self.browser.find_element_by_id("cvtitle_1")
        self.assertIn("Test Entry", title.text)
        # find just made entry
        self.browser.find_element_by_id("cvedit_1").click()
        start_time = time.time()
        while True:
            try:
                eh = self.browser.find_element_by_id("editorHeader")
                self.assertIn("Edit CV Entry", eh.text)
                break
            except (WebDriverException, AttributeError) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
        id_title = self.browser.find_element_by_id('id_title')
        submit = self.browser.find_element_by_id('id_submit')
        id_title.send_keys("2")

        submit.click()
        self.checkIfAtHome()
        title = self.browser.find_element_by_id("cvtitle_1")
        self.assertIn("Test Entry2", title.text)
        removebtn = self.browser.find_element_by_id("cvremove_1")
        removebtn.click()
        start_time = time.time()
        while True:
            EntryHere = True
            try:
                title = self.browser.find_element_by_id("cvtitle_1")
            except (WebDriverException, AttributeError) as e:
                EntryHere = False

            if not EntryHere:
                break
            elif time.time() - start_time > MAX_WAIT:
                self.assertTrue(False)
            time.sleep(0.5)
        self.browser.find_element_by_id("logout_link").click()

        start_time = time.time()
        while True:
            try:
                self.browser.find_element_by_id("login_btn")
                break
            except (WebDriverException, AttributeError) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)



    def checkIfAtHome(self):
        start_time = time.time()
        while True:
            try:
                self.browser.find_element_by_id("usergreeting")
                break
            except (WebDriverException, AttributeError) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
