# -*- coding: utf-8 -*-
__author__ = 'user'

import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException



class SmokeTests(unittest.TestCase):

    _login = "semuschenko"
    _password = "pDk7jf"

    _original_name = "Семищенко Христофор Онуфрійович"
    _original_email = "semuschenko@gmail.com"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://sms-rv016atqc.rhcloud.com"
        self.verificationErrors = []
        self.accept_next_alert = True

        self.driver.get(self.base_url + "/")
        self.driver.find_element_by_name("inputUsername").clear()
        self.driver.find_element_by_name("inputUsername").send_keys(self._login.decode('utf-8'))
        self.driver.find_element_by_name("inputPassword").clear()
        self.driver.find_element_by_name("inputPassword").send_keys(self._password.decode('utf-8'))
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.driver.find_element_by_xpath("//a[@href='/core/profile/']").click()


    def test_ui_presence(self):
        """
        01. Check, that user profile page is opened
        """
        driver = self.driver
        # self.assertIn("Профіль".decode('utf-8'),driver.page_source)
        # print(driver.find_element_by_xpath("//div[contains(.,'Профіль')]".decode('utf-8')).text)
        self.assertEqual("Профіль".decode('utf-8'),
            driver.find_element_by_xpath("//div[@class='col-md-12 lead']".decode('utf-8')).text)
            # driver.find_element_by_xpath("//div[contains(.,'Профіль')]".decode('utf-8')))
#//div[@class='col-md-12 lead']
        print("|",self._original_name.decode('utf-8'),"|")
        print("|",driver.find_element_by_xpath("//h3[@class='only-bottom-margin']").text,"|")
        # return
        self.assertEqual(self._original_name.decode('utf-8'),
            driver.find_element_by_xpath("//h3[@class='only-bottom-margin']").text)

        """
        02. Check, that user profile page contains button(link) to edit profile
        """

        """
        03. Check, that clicking on the link to edit profile opens the frame to edit profile opened
        """
        driver.find_element_by_xpath("//a[@href='/core/profile_edit/']").click()
        waiter = WebDriverWait(driver, 30)
        element = waiter.until(lambda x : x.find_element_by_xpath("//h3[contains(.,'Редагувати профіль')]"))

        """
        04. Check, that the frame to edit profile contains fields and buttons
        """
        driver.find_element_by_xpath("//input[@id='inputName']")
        driver.find_element_by_xpath("//input[@id='inputEmail']")
        driver.find_element_by_xpath("//a[contains(.,'Відмінити')]")
        driver.find_element_by_xpath("//button[@type='submit']")
        print("finish")

    def test_05(self):
        pass


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main(verbosity=2)