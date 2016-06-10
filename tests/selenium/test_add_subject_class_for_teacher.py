# -*- coding: utf-8 -*-
"""
Tests on Selenium WebDriver of an ability to add subject and class for teacher
"""

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class SchoolCRUDTests(unittest.TestCase):
    """
    Class with methods for testing an ability
    to add subject and class for teacher
    """

    baseurl = "https://smsauto-dvatqc.rhcloud.com"
    username = "zoshch"
    password = "df5sFdf"
    xpaths = {
        'inputUsername': "//input[@name='inputUsername']",
        'inputPassword': "//input[@name='inputPassword']",
        'submitButtonLogin': "button",
    }

    def SetUp(self):
        """ Fixture that creates all the preparations for tests """

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.accept_next_alert = True
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath(
            self.xpaths['inputUsername']).send_keys(
            self.username)

        self.driver.find_element_by_xpath(
            self.xpaths['inputPassword']).send_keys(
            self.password)

        self.driver.find_element_by_tag_name(
            self.xpaths['submitButtonLogin']).click()

    def tearDown(self):
        """ Fixture that deletes all the preparations for tests """

        self.driver.close()


