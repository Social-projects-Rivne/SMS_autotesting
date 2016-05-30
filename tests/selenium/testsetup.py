#  -*- coding: utf-8 -*-
"""
Test setup class that implements test preparations
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestSetup(unittest.TestCase):

    """ Parent class with preparations for main tests
    """

    def setUp(self, url='http://smsautotesting-atqc.rhcloud.com/',
              user='test_admin', password='Install_new!'):
        """ General preparations for all tests"""
        self.driver = webdriver.Firefox()
        self._appurl = url
        self._username = user
        self._password = password

        # Preparation actions for all test cases
        driver = self.driver
        driver.maximize_window()
        driver.get(self._appurl)

        elem = driver.find_element_by_name('inputUsername')
        elem.send_keys(self._username)
        elem.send_keys(Keys.TAB)
        elem = driver.find_element_by_name('inputPassword')
        elem.send_keys(self._password)
        elem.send_keys(Keys.ENTER)

    def tearDown(self):
        """ Close browser after each test"""
        self.driver.close()


