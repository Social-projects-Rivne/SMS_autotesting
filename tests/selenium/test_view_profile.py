# -*- coding: utf-8 -*-
""" Tests for 'View Profile' function of roles
'teacher', 'mainteacher', 'director' (testing with Selenium)
"""

import unittest

from selenium import webdriver


class UiTests(unittest.TestCase):
    """ Basic tests for start page - check UI elements presence """

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://django-farinhate.rhcloud.com"
        self.accept_next_alert = True

    def test_ui_presence(self):
        """
        Check, that start page contains fields and buttons
        """
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_name("inputUsername")
        driver.find_element_by_name("inputPassword")
        driver.find_element_by_xpath("//button[contains(.,'Увійти')]")

    def tearDown(self):
        """ Fixture that deletes all preparation for tests """
        self.driver.quit()


class PositiveTests(unittest.TestCase):
    """ Tests for 'View profile' function of roles
    'teacher', 'mainteacher', 'director'
    """
    _list_login = ["semuschenko",
                   "zoshch",
                   "maximus"]
    _list_password = ["pDk7jf",
                      "df5sFdf",
                      "LKuJf3y"]
    _list_name = ["Семищенко Христофор Онуфрійович",
                  "Зощенко Іван Вікторович",
                  "Галицький Максим Генадійович"]
    _list_mail = ["semuschenko@gmail.com",
                  "zoshch@gmail.com",
                  "maximus@gmail.com"]
    _list_view_login = ["Логін: semuschenko",
                        "Логін: zoshch",
                        "Логін: maximus"]


    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://django-farinhate.rhcloud.com"
        self.accept_next_alert = True

    def _set_test_data(self):
        """ Creating initial data for tests """
        self.login = self._list_login[self.current_test]
        self.password = self._list_password[self.current_test]
        self.name = self._list_name[self.current_test]
        self.view_login = self._list_view_login[self.current_test]
        self.mail = self._list_mail[self.current_test]

    def _test_steps_xpath(self):
        """ tests steps for click element by xpath """
        self._set_test_data()

        driver = self.driver
        driver.get(self.base_url)

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password.decode('utf-8'))
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath(
            "//html/body/div[2]/div/div[1]/ul/li[4]/a").click()

        self.assertIn(self.mail.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[contains(@class,'col-md-8')]").text)
        self.assertIn(self.view_login.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.assertIn(self.name.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

    def _test_steps_link(self):
        """ tests steps for click element by link """
        self._set_test_data()

        driver = self.driver
        driver.get(self.base_url)

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password.decode('utf-8'))

        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u'Мій профіль').click()

        self.assertIn(self.mail.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[contains(@class,'col-md-8')]").text)
        self.assertIn(self.view_login.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.assertIn(self.name.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)
    def test01_view_main_teacher_xpath(self):
        """
        1. Button "Мій профіль" show profile for
        "Головний вчитель" (click element)
        """
        self.current_test = 0
        self._test_steps_xpath()

    def test02_view_director_xpath(self):
        """
        2. Button "Мій профіль" show profile for "Завуч" (click element)
        """
        self.current_test = 1
        self._test_steps_xpath()

    def test03_view_teacher_xpath(self):
        """
        3. Button "Мій профіль" show profile for "Викладач" (click element)
        """
        self.current_test = 2
        self._test_steps_xpath()

    def test04_view_main_teacher_xpath(self):
        """
        4. Button "Мій профіль" show profile for "Головний вчитель" (click link)
        """
        self.current_test = 0
        self._test_steps_link()

    def test05_view_director_xpath(self):
        """
        5.  Button "Мій профіль" show profile for "Завуч" (click link)
        """
        self.current_test = 1
        self._test_steps_link()

    def test06_view_teacher_xpath(self):
        """
        6. Button "Мій профіль" show profile for "Викладач" (click link)
        """
        self.current_test = 2
        self._test_steps_link()

    def tearDown(self):
        """ Fixture that deletes all preparation for tests """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
