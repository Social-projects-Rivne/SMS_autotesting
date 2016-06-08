# -*- coding: utf-8 -*-
""" Tests for "Edit Profile" (testing with Selenium) """

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestPreparations(unittest.TestCase):

    """ Superclass with preparations for tests and initial data """

    base_url = "http://sms-rv016atqc.rhcloud.com"
    login = "semuschenko"
    password = "pDk7jf"

    original_name = "Семищенко Христофор Онуфрійович"
    original_email = "semuschenko@gmail.com"

    xpaths = {"frame_title": "//h3[contains(.,'Редагувати профіль')]",
              "edit_button": "//a[@href='/core/profile_edit/']",
              "input_name": "//input[@id='inputName']",
              "input_email": "//input[@id='inputEmail']",
              "confirm_btn": "//button[@name='confirm_button']",
              "cancel_btn": "//a[contains(.,'Відмінити')]",
              "warnings": "//span[@class='help-block']"}

    warnings = {"name": "Некоректно введено ім'я.",
                "email": "Некоректно введено email."}

    def __init__(self, *args, **kwargs):
        """  Define instance variables """

        super(TestPreparations, self).__init__(*args, **kwargs)

    def setUp(self):
        """ Fixture that creates a initial data and records for tests,
        initial test steps """

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.accept_next_alert = True

        self.driver.get(self.base_url + "/")
        driver = self.driver

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password.decode('utf-8'))
        driver.find_element_by_xpath("//button[@type='submit']").click()

        driver.find_element_by_xpath("//a[@href='/core/profile/']").click()

    def tearDown(self):
        """ Fixture that deletes all preparation for tests """

        self.driver.quit()


class SmokeTests(TestPreparations):

    """ Smoke tests for Edit Profile  - check UI elements presence """

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        super(SmokeTests, self).setUp()

    def tests_ui_presence(self):
        """
        01. Check, that user profile page is opened
        02. Check, that user profile page contains button(link) to edit profile
        03. Check, that clicking on the link to edit profile opens the frame to
            edit profile opened
        04. Check, that the frame to edit profile contains fields and buttons
        """

        driver = self.driver
        self.assertEqual("Профіль".decode('utf-8'),
                         driver.find_element_by_xpath(
                             "//div[@class='col-md-12 lead']".
                             decode('utf-8')).text)

        self.assertEqual(self.original_name.decode('utf-8'),
                         driver.find_element_by_xpath(
                             "//h3[@class='only-bottom-margin']").text)

        driver.find_element_by_xpath(
            "//a[@href='/core/profile_edit/']").click()

        # waiter = WebDriverWait(driver, 10)
        # waiter.until(lambda x: x.find_element_by_xpath(
        # self.xpaths["frame_title"]))
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.xpaths["frame_title"])

        driver.find_element_by_xpath(self.xpaths["input_name"])
        driver.find_element_by_xpath(self.xpaths["input_email"])
        driver.find_element_by_xpath(self.xpaths["cancel_btn"])
        driver.find_element_by_xpath(self.xpaths["confirm_btn"])

    def tearDown(self):
        """ Fixture that deletes all preparation for tests """

        super(SmokeTests, self).tearDown()


class PositiveTests(TestPreparations):

    """ Positive tests for Edit Profile with correct data,
    expected result - data in profile is changed """

    def __init__(self, *args, **kwargs):
        """  Define instance variables """

        super(PositiveTests, self).__init__(*args, **kwargs)
        self.name = ""
        self.email = ""
        self.passed = False

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        super(PositiveTests, self).setUp()

    def _test_steps(self):
        """ Common tests steps """

        driver = self.driver
        driver.find_element_by_xpath(self.xpaths["edit_button"]).click()

        driver.implicitly_wait(5)
        driver.find_element_by_xpath(self.xpaths["frame_title"])
        # waiter = WebDriverWait(driver, 5)
        # waiter.until(lambda x: x.find_element_by_xpath(self.xpaths["frame_title"]))

        input_name = driver.find_element_by_xpath(self.xpaths["input_name"])
        input_name.clear()
        input_name.send_keys(self.name.decode('utf-8'))
        input_name.send_keys(Keys.TAB)

        input_email = driver.find_element_by_xpath(self.xpaths["input_email"])
        input_email.clear()
        input_email.send_keys(self.email.decode('utf-8'))
        input_email.send_keys(Keys.TAB)
        driver.find_element_by_xpath(self.xpaths["confirm_btn"]).click()

        warnings = driver.find_elements_by_xpath(self.xpaths["warnings"])
        for warning in warnings:
            msg = "Positive test failed - " + self.name + " " + self.email
            self.assertNotEqual(self.warnings["name"].decode('utf-8'),
                                warning.text,
                                msg)
            self.assertNotEqual(self.warnings["email"].decode('utf-8'),
                                warning.text,
                                msg)

        self.assertIn(self.name.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

        self.assertIn(self.email.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.passed = True

    def test01_correct_name(self):
        """ Edit profile with correct data (first case) """

        self.name = "Іванов Петро Степанович"
        self.email = "email@domain.com"
        self._test_steps()

    def test02_correct_name(self):
        """ Edit profile with correct data (second case) """

        self.name = "Стець Мар'яна Іванівна"
        self.email = "marjana.stetc@gmail.com"
        self._test_steps()

    def test03_correct_name(self):
        """ Edit profile with correct data (third case) """

        self.name = "Ворон-Розумна Анна-Марія Степанівна"
        self.email = "email@domain.com"
        self._test_steps()

    def test04_correct_name(self):
        """ Edit profile with correct data (fourth case) """

        self.name = "Ворон-Розумна Анна Степанівна"
        self.email = "email@domain.com"
        self._test_steps()

    def test05_correct_name(self):
        """ Edit profile with correct data (fifth case) """

        self.name = "Ворон Анна-Марія Степанівна"
        self.email = "email@domain.com"
        self._test_steps()

    def test06_correct_name(self):
        """ Edit profile with correct data (sixth case) """

        self.name = "Ворон Анна Степанівна"
        self.email = "voron-rozumna.anna-marija@" \
                     "many-many.domain.levels.gmail.com"
        self._test_steps()

    def tearDown(self):
        """ Fixture that deletes all preparation for tests and restores
        original data """

        if self.passed:
            self.name = self.original_name
            self.email = self.original_email
            self._test_steps()

        super(PositiveTests, self).tearDown()


class NegativeTests(TestPreparations):

    """ Negative tests for Edit Profile with incorrect data,
    expected result - data in profile isn't changed """

    def __init__(self, *args, **kwargs):
        """  Define instance variables """

        super(NegativeTests, self).__init__(*args, **kwargs)
        self.name = ""
        self.email = ""
        self.passed = False

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        super(NegativeTests, self).setUp()

    def _test_steps_name(self):
        """ Common tests steps for name """

        driver = self.driver
        driver.find_element_by_xpath(self.xpaths["edit_button"]).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.xpaths["frame_title"])

        input_name = driver.find_element_by_xpath(self.xpaths["input_name"])
        input_name.clear()
        input_name.send_keys(self.name.decode('utf-8'))
        input_name.send_keys(Keys.TAB)

        input_email = driver.find_element_by_xpath(self.xpaths["input_email"])
        input_email.clear()
        input_email.send_keys(self.email.decode('utf-8'))
        input_email.send_keys(Keys.TAB)
        driver.find_element_by_xpath(self.xpaths["confirm_btn"]).click()

        msg1 = "Page changed, profile editing passed \n"
        msg2 = "Negative test failed - " + self.name + " " + self.email

        self.assertNotEqual(
            len(driver.find_elements_by_xpath(self.xpaths["frame_title"])),
            0, msg1 + msg2)

        warnings = driver.find_elements_by_xpath(self.xpaths["confirm_btn"])
        expected = self.warnings["name"]
        self.assertIsNot(
            any(expected.decode('utf-8') == warning.text
                for warning in warnings),
            msg2)

        self.passed = True

    def test01_empty_name(self):
        """ Edit profile with empty name """

        self.name = ""
        self.email = self.original_email
        self._test_steps_name()

    def test02_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "Мадонна"
        self.email = self.original_email
        self._test_steps_name()

    def test03_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "Мурзік Васильович"
        self.email = self.original_email
        self._test_steps_name()

    def test04_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "Василь Перебійніс"
        self.email = self.original_email
        self._test_steps_name()

    def test05_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "John"
        self.email = self.original_email
        self._test_steps_name()

    def test06_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "John Smith"
        self.email = self.original_email
        self._test_steps_name()

    def test07_incorrect_name(self):
        """  Edit profile with incorrect name """

        self.name = "John Alexander Smith"
        self.email = self.original_email
        self._test_steps_name()

    def test08_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "John A. Smith"
        self.email = self.original_email
        self._test_steps_name()

    def test09_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "бОРИС бОРИС бОРИСОВИЧ"
        self.email = self.original_email
        self._test_steps_name()

    def test10_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "Борис Борис Борисович Молодший"
        self.email = self.original_email
        self._test_steps_name()

    def test11_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "Cемищенко Xристофор Oнуфрійович"
        self.email = self.original_email
        self._test_steps_name()

    def test12_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "Семищенко_Христофор_Онуфрійович"
        self.email = self.original_email
        self._test_steps_name()

    def test13_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "Семищенко Христофор Онуфр1йович"
        self.email = self.original_email
        self._test_steps_name()

    def test14_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "Семищенко Христофор О."
        self.email = self.original_email
        self._test_steps_name()

    def test15_incorrect_name(self):
        """ Edit profile with incorrect name """

        self.name = "Семищенкомищенко Христофористофор " \
                    "Онуфрійовичуфрійовичуфрійович"
        self.email = self.original_email
        self._test_steps_name()

    def test16_incorrect_name(self):
        """ Edit profile with correct name that begins with spaces """

        self.name = self.original_name + "     "
        self.email = self.original_email
        self._test_steps_name()

    def test17_incorrect_name(self):
        """ Edit profile with correct name that ends with spaces """

        self.name = "     " + self.original_name
        self.email = self.original_email
        self._test_steps_name()

    def test18_incorrect_name(self):
        """ Edit profile with correct name that consists from spaces """

        self.name = "     "
        self.email = self.original_email
        self._test_steps_name()

    def _test_steps_email(self):
        """ Common tests steps for email """

        self.passed = False

        driver = self.driver
        driver.find_element_by_xpath(self.xpaths["edit_button"]).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.xpaths["frame_title"])

        input_name = driver.find_element_by_xpath(self.xpaths["input_name"])
        input_name.clear()
        input_name.send_keys(self.name.decode('utf-8'))
        input_name.send_keys(Keys.TAB)

        input_email = driver.find_element_by_xpath(self.xpaths["input_email"])
        input_email.clear()
        input_email.send_keys(self.email.decode('utf-8'))
        input_email.send_keys(Keys.TAB)
        driver.find_element_by_xpath(self.xpaths["confirm_btn"]).click()

        msg1 = "Page changed, profile editing passed \n"
        msg2 = "Negative test failed - " + self.name + " " + self.email

        self.assertNotEqual(
            len(driver.find_elements_by_xpath(self.xpaths["frame_title"])),
            0, msg1 + msg2)

        warnings = driver.find_elements_by_xpath(self.xpaths["confirm_btn"])
        expected = self.warnings["email"]
        self.assertIsNot(
            any(expected.decode('utf-8') == warning.text
                for warning in warnings),
            msg2)

        self.passed = True

    def test51_empty_email(self):
        """ Edit profile with empty email """

        self.name = self.original_name
        self.email = ""
        self._test_steps_email()

    def test52_incorrect_email(self):
        """ Edit profile with incorrect email """

        self.name = self.original_name
        self.email = "@gmail.com"
        self._test_steps_email()

    def test53_incorrect_email(self):
        """ Edit profile with incorrect email """

        self.name = self.original_name
        self.email = "address@.com"
        self._test_steps_email()

    def test54_incorrect_email(self):
        """ Edit profile with incorrect email """

        self.name = self.original_name
        self.email = "address@gmail"
        self._test_steps_email()

    def test55_incorrect_email(self):
        """ Edit profile with incorrect email """

        self.name = self.original_name
        self.email = "address@gmail@com"
        self._test_steps_email()

    def test56_incorrect_email(self):
        """ Edit profile with incorrect email """

        self.name = self.original_name
        self.email = "address.gmail.com"
        self._test_steps_email()

    def test57_incorrect_email(self):
        """ Edit profile with incorrect email """

        self.name = self.original_name
        self.email = "voron-rozumna.anna-marija@many-many.domain.levels.and." \
                     "some.more.domain.levels.for.email.testing.gmail.com"
        self._test_steps_email()

    def test58_incorrect_email(self):
        """ Edit profile with correct name that begins with spaces """

        self.name = self.original_name
        self.email = self.original_email + "     "
        self._test_steps_email()

    def test59_incorrect_email(self):
        """ Edit profile with correct name that ends with spaces """

        self.name = self.original_name
        self.email = "     " + self.original_email
        self._test_steps_email()

    def test60_incorrect_email(self):
        """ Edit profile with correct name that consists from spaces """

        self.name = self.original_name
        self.email = "     "
        self._test_steps_email()

    def _test_steps_restore(self):
        """ Common tests steps to restore state before tests """

        driver = self.driver
        driver.find_element_by_xpath(self.xpaths["edit_button"]).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.xpaths["frame_title"])

        input_name = driver.find_element_by_xpath(self.xpaths["input_name"])
        input_name.clear()
        input_name.send_keys(self.name.decode('utf-8'))
        input_name.send_keys(Keys.TAB)

        input_email = driver.find_element_by_xpath(self.xpaths["input_email"])
        input_email.clear()
        input_email.send_keys(self.email.decode('utf-8'))
        input_email.send_keys(Keys.TAB)
        driver.find_element_by_xpath(self.xpaths["confirm_btn"]).click()

        warnings = driver.find_elements_by_xpath(self.xpaths["confirm_btn"])
        for warning in warnings:
            msg = "Positive test failed - " + self.name + " " + self.email
            self.assertNotEqual(self.warnings["name"].decode('utf-8'),
                                warning.text,
                                msg)
            self.assertNotEqual(self.warnings["email"].decode('utf-8'),
                                warning.text,
                                msg)

        self.assertIn(self.name.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

        self.assertIn(self.email.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.passed = True

    def tearDown(self):
        """ Fixture that deletes all preparation for tests and restores
        original data """

        if not self.passed:
            self.name = self.original_name
            self.email = self.original_email
            self._test_steps_restore()

        super(NegativeTests, self).tearDown()


if __name__ == "__main__":
    unittest.main(verbosity=2)
