# -*- coding: utf-8 -*-
""" Tests for function 'Change role' as mainteacher on Selenium """

import unittest

from selenium import webdriver

from selenium.webdriver.support.ui import Select


class RoleTests(unittest.TestCase):
    
    """
    Class for testing function 'Change role' as mainteacher on Selenium
    """

    base_url_team = "http://smsautotesting-atqc.rhcloud.com/"
    login = "semuschenko"
    password = "pDk7jf"

    xpaths = {
        'inputUsername': "//input[@name='inputUsername']",
        'inputPassword': "//input[@name='inputPassword']",
        'loginButton': "//button[@type='submit']",
        'linkTeacher': "//a[@href='/mainteacher/teachers_list/']",
        'DirectortoTeacher': ".//*[@id='9']/td[3]/select",
        'TeachertoDirector': ".//*[@id='4']/td[3]/select",
        'DirectortoDirector': ".//*[@id='1']/td[3]/select",
        'TeachertoTeacher': ".//*[@id='15']/td[3]/select"
    }

    def setUp(self):
        """
        Fixture that creates a initial data and records for tests
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = self.base_url_team
        self.accept_next_alert = True

    def test_steps(self):
        """
        test steps for all cases
        """
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath(
            self.xpaths["inputUsername"]).send_keys(self.login)
        driver.find_element_by_xpath(
            self.xpaths["inputPassword"]).send_keys(self.password)
        driver.find_element_by_xpath(self.xpaths["loginButton"]).click()
        driver.find_element_by_link_text("Викладачі").click()

    def test01_director_teacher(self):
        """
        Test for Changing Role From Завуч to Викладач
        """
        self.test_steps()
        self.driver.find_element_by_xpath(
            self.xpaths["DirectortoTeacher"]).click()

        select = Select(self.driver.find_element_by_xpath(
            self.xpaths["DirectortoTeacher"]))
        select.select_by_value("3")

        current = self.driver.find_element_by_xpath(
            self.xpaths["DirectortoTeacher"]).get_attribute("value")
        self.assertEquals("3", current)

    def test02_teacher_director(self):
        """
        Test for Changing Role From Викладач to Завуч
        """
        self.test_steps()
        self.driver.find_element_by_xpath(
            self.xpaths["TeachertoDirector"]).click()

        select = Select(self.driver.find_element_by_xpath(
            self.xpaths["TeachertoDirector"]))
        select.select_by_value("2")

        current = self.driver.find_element_by_xpath(
            self.xpaths["TeachertoDirector"]).get_attribute("value")
        self.assertEquals("2", current)

    def test03_teacher_teacher(self):
        """
        Test for Changing Role From Викладач to Викладач
        """
        self.test_steps()
        self.driver.find_element_by_xpath(
            self.xpaths["TeachertoTeacher"]).click()

        select = Select(self.driver.find_element_by_xpath(
            self.xpaths["TeachertoTeacher"]))
        select.select_by_value("3")

        current = self.driver.find_element_by_xpath(
            self.xpaths["TeachertoTeacher"]).get_attribute("value")
        self.assertEquals("3", current)

    def test04_director_director(self):
        """
        Test for Changing Role From Завуч to Завуч
        """
        self.test_steps()
        self.driver.find_element_by_xpath(
            self.xpaths["DirectortoDirector"]).click()

        select = Select(self.driver.find_element_by_xpath(
            self.xpaths["DirectortoDirector"]))
        select.select_by_value("2")

        current = self.driver.find_element_by_xpath(
            self.xpaths["DirectortoDirector"]).get_attribute("value")
        self.assertEquals("2", current)

    def tearDown(self):
        """
        Fixture that deletes all preparation for tests
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)