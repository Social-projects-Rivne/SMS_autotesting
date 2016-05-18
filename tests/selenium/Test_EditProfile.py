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

class TestPreparations(unittest.TestCase):
    _url = "http://sms-rv016atqc.rhcloud.com"
    _login = "semuschenko"
    _password = "pDk7jf"

    _original_name = "Семищенко Христофор Онуфрійович"
    _original_email = "semuschenko@gmail.com"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = self._url
        self.verificationErrors = []
        self.accept_next_alert = True

        self.driver.get(self.base_url + "/")
        driver = self.driver

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self._login.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self._password.decode('utf-8'))
        driver.find_element_by_xpath("//button[@type='submit']").click()

        self.driver.find_element_by_xpath("//a[@href='/core/profile/']").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class SmokeTests(TestPreparations):

    def setUp(self):
        super(SmokeTests, self).setUp()

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
        # print("|",self._original_name.decode('utf-8'),"|")
        # print("|",driver.find_element_by_xpath("//h3[@class='only-bottom-margin']").text,"|")
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
        element = waiter.until(lambda x: x.find_element_by_xpath("//h3[contains(.,'Редагувати профіль')]"))

        """
        04. Check, that the frame to edit profile contains fields and buttons
        """
        driver.find_element_by_xpath("//input[@id='inputName']")
        driver.find_element_by_xpath("//input[@id='inputEmail']")
        driver.find_element_by_xpath("//a[contains(.,'Відмінити')]")
        driver.find_element_by_xpath("//button[@type='submit']")
        # print("finish")


    def tearDown(self):
        super(SmokeTests,self).tearDown()


class PositiveTests(TestPreparations):
    _test_data = [
        ["Іванов Петро Степанович", "email@domain.com"],
        ["Стець Мар'яна Іванівна", "marjana.stetc@gmail.com"],
        ["Ворон-Розумна Анна-Марія Степанівна", "email@domain.com"],
        ["Ворон-Розумна Анна Степанівна", "email@domain.com"],
        ["Ворон Анна-Марія Степанівна", "email@domain.com"],
        ["Ворон Анна Степанівна", "voron-rozumna.anna-marija@many-many.domain.levels.gmail.com"],
    ]

    def setUp(self):
        super(PositiveTests,self).setUp()

    def _set_test_data(self):
        self.name = self._test_data[self.current_test][0]
        self.email = self._test_data[self.current_test][1]

    def _test_steps(self):

        self.passed = False

        driver = self.driver
        driver.find_element_by_xpath("//a[@href='/core/profile_edit/']").click()
        driver.implicitly_wait(10);
        # waiter = WebDriverWait(driver, 30)
        element = driver.find_element_by_xpath("//h3[contains(.,'Редагувати профіль')]")

        input_name = driver.find_element_by_xpath("//input[@id='inputName']")
        input_name.clear()
        input_name.send_keys(self.name.decode('utf-8'))
        input_name.send_keys(Keys.TAB)

        input_email = driver.find_element_by_xpath("//input[@id='inputEmail']")
        input_email.clear()
        input_email.send_keys(self.email.decode('utf-8'))
        input_email.send_keys(Keys.TAB)
        driver.find_element_by_xpath("//button[@name='confirm_button']").click()

        warnings = driver.find_elements_by_xpath("//span[@class='help-block']")
        for warning in warnings:
            msg = "Positive test failed - " + self.name + " " + self.email
            self.assertEquals("Некоректно введено ім'я.", warning.text, msg)
            self.assertEquals("Некоректно введено email.", warning.text, msg)

        # print(self.email)
        # print(driver.find_element_by_xpath(
        #                   "//div[@class='col-md-8']").text)

        self.assertIn(self.name.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

        self.assertIn(self.email.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)

        self.passed = True

    def test_05(self):
        self.current_test = 0
        self._set_test_data()
        self._test_steps()

    def test_06(self):
        self.current_test = 1
        self._set_test_data()
        self._test_steps()

    def test_07(self):
        self.current_test = 2
        self._set_test_data()
        self._test_steps()

    def test_08(self):
        self.current_test = 3
        self._set_test_data()
        self._test_steps()

    def test_09(self):
        self.current_test = 4
        self._set_test_data()
        self._test_steps()

    def test_10(self):
        self.current_test = 5
        self._set_test_data()
        self._test_steps()

    def tearDown(self):
        if self.passed:
            self.name = self._original_name
            self.email = self._original_email
            self._test_steps()

        super(PositiveTests,self).tearDown()

    # @classmethod
    # def tearDown(self):
    #
    #     self.name = self._original_name
    #     self.email = self._original_email
    #     # self._test_steps()


if __name__ == "__main__":
    unittest.main(verbosity=2)