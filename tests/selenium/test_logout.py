# -*- coding: utf-8 -*-
""" Tests on Selenium WebDriver logout function"""


import unittest
from selenium import webdriver

xpaths = {
    'inputUsername': "//input[@name='inputUsername']",
    'inputPassword': "//input[@name='inputPassword']",
    'submitButtonLogin': "button"
}


class logout_main(unittest.TestCase):
    """Class with methods, for testing logout by main teacher"""

    _baseurl = "http://ss-alexeyvasiluk.rhcloud.com/"
    _login_main = "semuschenko"
    _password_main = "pDk7jf"

    def setUp(self):
        """Fixture that creates all the preparations for tests"""
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self._baseurl)
        self.driver.find_element_by_xpath(xpaths['inputUsername']).send_keys(
            self._login_main)
        self.driver.find_element_by_xpath(xpaths['inputPassword']).send_keys(
            self._password_main)
        self.driver.find_element_by_tag_name(xpaths['submitButtonLogin']).\
            click()

    def tearDown(self):
        """Fixture that deletes all the preparations for tests"""
        self.driver.close()

    def test_logout_main_teacher(self):
        """Test to check logout function as main teacher"""
        driver = self.driver
        link = driver.find_element_by_id("logout")
        link.click()
        self.element = driver.find_element_by_tag_name(
            xpaths['submitButtonLogin'])
        self.assertIsNotNone(self.element)


class Logout_director(unittest.TestCase):
    """Class with methods, for testing logout by director"""

    _baseurl = "http://ss-alexeyvasiluk.rhcloud.com/"
    _login_director = "zoshch"
    _password_director = "df5sFdf"

    def setUp(self):
        """Fixture that creates all the preparations for tests"""
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self._baseurl)
        self.driver.find_element_by_xpath(xpaths['inputUsername']).send_keys(
            self._login_director)
        self.driver.find_element_by_xpath(xpaths['inputPassword']).send_keys(
            self._password_director)
        self.driver.find_element_by_tag_name(xpaths['submitButtonLogin']).\
            click()

    def tearDown(self):
        """Fixture that deletes all the preparations for tests"""
        self.driver.close()

    def test_logout_director(self):
        """Test to check logout function as director"""
        driver = self.driver
        link = driver.find_element_by_id("logout")
        link.click()
        self.element = driver.find_element_by_tag_name(
            xpaths['submitButtonLogin'])
        self.assertIsNotNone(self.element)


class Logout_teacher(unittest.TestCase):
    """Class with methods, for testing logout by teacher"""

    _baseurl = "http://ss-alexeyvasiluk.rhcloud.com/"
    _login_teacher = "maximus"
    _password_teacher = "LKuJf3y"

    def setUp(self):
        """Fixture that creates all the preparations for tests"""
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self._baseurl)
        self.driver.find_element_by_xpath(xpaths['inputUsername']).send_keys(
            self._login_teacher)
        self.driver.find_element_by_xpath(xpaths['inputPassword']).send_keys(
            self._password_teacher)
        self.driver.find_element_by_tag_name(xpaths['submitButtonLogin']).\
            click()

    def tearDown(self):
        """Fixture that deletes all the preparations for tests"""
        self.driver.close()

    def test_logout_teacher(self):
        """Test to check logout function as teacher"""
        driver = self.driver
        link = driver.find_element_by_id("logout")
        link.click()
        self.element = driver.find_element_by_tag_name(
            xpaths['submitButtonLogin'])
        self.assertIsNotNone(self.element)


if __name__ == "__main__":
    unittest.main(verbosity=1)
