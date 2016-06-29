# -*- coding: utf-8 -*-
""" Tests for 'View Profile' function of roles
'teacher', 'mainteacher', 'director' (testing with Selenium)
"""

import unittest

from selenium import webdriver


class UiTests(unittest.TestCase):
    """
    Basic tests for start page - check UI elements presence
    """

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://smsautotesting-atqc.rhcloud.com"
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
    login_main = "semuschenko"
    login_director = "zoshch"
    login_teacher = "maximus"

    password_main = "pDk7jf"
    password_director = "df5sFdf"
    password_teacher = "LKuJf3y"

    name_main = u"Семищенко Христофор Онуфрійович"
    name_director = u"Зощенко Іван Вікторович"
    name_teacher = u"Галицький Максим Генадійович"

    mail_main = "semuschenko@gmail.com"
    mail_director = "zoshch@gmail.com"
    mail_teacher = "maximus@gmail.com"

    view_login_main = "Логін: semuschenko"
    view_login_director = "Логін: zoshch"
    view_login_teacher = "Логін: maximus"


    def setUp(self):
        """
        Fixture that creates a initial data and records for tests
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://smsautotesting-atqc.rhcloud.com"
        self.accept_next_alert = True


    def test01_view_main_teacher_xpath(self):
        """
        1. Button "Мій профіль" show profile for
        "Головний вчитель" (click element)
        """
        driver = self.driver
        driver.get(self.base_url)

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login_main.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password_main.decode('utf-8'))
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath(
            "//html/body/div[2]/div/div[1]/ul/li[4]/a").click()

        self.assertIn(self.mail_main.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[contains(@class,'col-md-8')]").text)
        self.assertIn(self.view_login_main.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.assertIn(self.name_main,
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

    def test02_view_director_xpath(self):
        """
        2. Button "Мій профіль" show profile for "Завуч" (click element)
        """
        driver = self.driver
        driver.get(self.base_url)

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login_director.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password_director.decode('utf-8'))
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath(
            "//html/body/div[2]/div/div[1]/ul/li[4]/a").click()

        self.assertIn(self.mail_director.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[contains(@class,'col-md-8')]").text)
        self.assertIn(self.view_login_director.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.assertIn(self.name_director,
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

    def test03_view_teacher_xpath(self):
        """
        3. Button "Мій профіль" show profile for "Викладач" (click element)
        """
        driver = self.driver
        driver.get(self.base_url)

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login_teacher.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password_teacher.decode('utf-8'))
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath(
            "//html/body/div[2]/div/div[1]/ul/li[4]/a").click()

        self.assertIn(self.mail_teacher.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[contains(@class,'col-md-8')]").text)
        self.assertIn(self.view_login_teacher.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.assertIn(self.name_teacher,
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

    def test04_view_main_teacher_xpath(self):
        """
        4. Button "Мій профіль" show profile for "Головний вчитель" (click link)
        """
        driver = self.driver
        driver.get(self.base_url)

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login_main.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password_main.decode('utf-8'))

        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u'Мій профіль').click()

        self.assertIn(self.mail_main.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[contains(@class,'col-md-8')]").text)
        self.assertIn(self.view_login_main.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.assertIn(self.name_main,
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

    def test05_view_director_xpath(self):
        """
        5.  Button "Мій профіль" show profile for "Завуч" (click link)
        """
        driver = self.driver
        driver.get(self.base_url)

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login_director.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password_director.decode('utf-8'))

        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u'Мій профіль').click()

        self.assertIn(self.mail_director.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[contains(@class,'col-md-8')]").text)
        self.assertIn(self.view_login_director.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.assertIn(self.name_director,
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

    def test06_view_teacher_xpath(self):
        """
        6. Button "Мій профіль" show profile for "Викладач" (click link)
        """
        driver = self.driver
        driver.get(self.base_url)

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login_teacher.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password_teacher.decode('utf-8'))

        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u'Мій профіль').click()

        self.assertIn(self.mail_teacher.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[contains(@class,'col-md-8')]").text)
        self.assertIn(self.view_login_teacher.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.assertIn(self.name_teacher,
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

    def tearDown(self):
        """
        Fixture that deletes all preparation for tests
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)