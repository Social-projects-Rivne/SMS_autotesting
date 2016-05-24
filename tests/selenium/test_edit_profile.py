# -*- coding: utf-8 -*-
""" Tests for "Edit Profile" (testing with Selenium) """

import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestPreparations(unittest.TestCase):
    """ Superclass with preparations for tests and initial data """

    _url = "http://sms-rv016atqc.rhcloud.com"
    _login = "semuschenko"
    _password = "pDk7jf"

    _original_name = "Семищенко Христофор Онуфрійович"
    _original_email = "semuschenko@gmail.com"

    _xpaths = {"frame_title": "//h3[contains(.,'Редагувати профіль')]",
               "edit_button": "//a[@href='/core/profile_edit/']",
               "input_name": "//input[@id='inputName']",
               "input_email": "//input[@id='inputEmail']",
               "confirm_btn": "//button[@name='confirm_button']",
               "warnings": "//span[@class='help-block']"}

    _warnings = {"name": "Некоректно введено ім'я.",
                 "email": "Некоректно введено email."}

    def setUp(self):
        """ Fixture that creates a initial data and records for tests,
        initial test steps
        """

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = self._url
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
        03. Check, that clicking on the link to edit profile opens the frame to edit profile opened
        04. Check, that the frame to edit profile contains fields and buttons
        """

        driver = self.driver
        self.assertEqual("Профіль".decode('utf-8'),
                         driver.find_element_by_xpath(
                             "//div[@class='col-md-12 lead']".
                             decode('utf-8')).text)

        self.assertEqual(self._original_name.decode('utf-8'),
                         driver.find_element_by_xpath(
                             "//h3[@class='only-bottom-margin']").text)

        driver.find_element_by_xpath(
            "//a[@href='/core/profile_edit/']").click()

        # waiter = WebDriverWait(driver, 30)
        # waiter.until(lambda x: x.find_element_by_xpath("//h3[contains(.,'Редагувати профіль')]"))
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//h3[contains(.,'Редагувати профіль')]")

        driver.find_element_by_xpath("//input[@id='inputName']")
        driver.find_element_by_xpath("//input[@id='inputEmail']")
        driver.find_element_by_xpath("//a[contains(.,'Відмінити')]")
        driver.find_element_by_xpath("//button[@type='submit']")

    def tearDown(self):
        """ Fixture that deletes all preparation for tests """

        super(SmokeTests, self).tearDown()


class PositiveTests(TestPreparations):
    """ Positive tests for Edit Profile with correct data,
    expected result - data in profile is changed
    """

    _xpaths = TestPreparations._xpaths

    _warnings = TestPreparations._warnings

    _test_data = [
        ["Іванов Петро Степанович", "email@domain.com"],
        ["Стець Мар'яна Іванівна", "marjana.stetc@gmail.com"],
        ["Ворон-Розумна Анна-Марія Степанівна", "email@domain.com"],
        ["Ворон-Розумна Анна Степанівна", "email@domain.com"],
        ["Ворон Анна-Марія Степанівна", "email@domain.com"],
        ["Ворон Анна Степанівна",
         "voron-rozumna.anna-marija@many-many.domain.levels.gmail.com"],
    ]

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        super(PositiveTests, self).setUp()

    def _set_test_data(self):
        """ Creating initial data for each test """

        self.name = self._test_data[self.current_test][0]
        self.email = self._test_data[self.current_test][1]

    def _test_steps(self):
        """ Common tests steps """

        self.passed = False

        driver = self.driver
        driver.find_element_by_xpath(self._xpaths["edit_button"]).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self._xpaths["frame_title"])
        # waiter = WebDriverWait(driver, 30)
        # waiter.until(lambda x: x.find_element_by_xpath(self._xpaths["frame_title"]))

        input_name = driver.find_element_by_xpath(self._xpaths["input_name"])
        input_name.clear()
        input_name.send_keys(self.name.decode('utf-8'))
        input_name.send_keys(Keys.TAB)

        input_email = driver.find_element_by_xpath(self._xpaths["input_email"])
        input_email.clear()
        input_email.send_keys(self.email.decode('utf-8'))
        input_email.send_keys(Keys.TAB)
        driver.find_element_by_xpath(self._xpaths["confirm_btn"]).click()

        warnings = driver.find_elements_by_xpath(self._xpaths["warnings"])
        for warning in warnings:
            msg = "Positive test failed - " + self.name + " " + self.email
            self.assertNotEqual(self._warnings["name"].decode('utf-8'),
                                warning.text,
                                msg)
            self.assertNotEqual(self._warnings["email"].decode('utf-8'),
                                warning.text,
                                msg)

        self.assertIn(self.name.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

        self.assertIn(self.email.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.passed = True

    def test_05(self):
        """ 05. Edit profile with correct data (first case) """

        self.current_test = 0
        self._set_test_data()
        self._test_steps()

    def test_06(self):
        """ 06. Edit profile with correct data (second case) """

        self.current_test = 1
        self._set_test_data()
        self._test_steps()

    def test_07(self):
        """ 07. Edit profile with correct data (third case) """

        self.current_test = 2
        self._set_test_data()
        self._test_steps()

    def test_08(self):
        """ 08. Edit profile with correct data (fourth case) """

        self.current_test = 3
        self._set_test_data()
        self._test_steps()

    def test_09(self):
        """ 09. Edit profile with correct data (fifth case) """

        self.current_test = 4
        self._set_test_data()
        self._test_steps()

    def test_10(self):
        """ 10. Edit profile with correct data (sixth case) """

        self.current_test = 5
        self._set_test_data()
        self._test_steps()

    def tearDown(self):
        """ Fixture that deletes all preparation for tests and restores
        original data
        """

        if self.passed:
            self.name = self._original_name
            self.email = self._original_email
            self._test_steps()

        super(PositiveTests, self).tearDown()


class NegativeTests(TestPreparations):
    """ Negative tests for Edit Profile with incorrect data,
    expected result - login is successful
    """

    _xpaths = TestPreparations._xpaths

    _warnings = TestPreparations._warnings

    _original_name = TestPreparations._original_name
    _original_email = TestPreparations._original_email

    _test_data_names = [
        "",
        "Мадонна",
        "Мурзік Васильович",
        "Василь Перебійніс",
        "John",
        "John Smith",
        "John Alexander Smith",
        "John A. Smith",
        "бОРИС бОРИС бОРИСОВИЧ",
        "Борис Борис Борисович Молодший",
        "Cемищенко Xристофор Oнуфрійович",
        "Семищенко_Христофор_Онуфрійович",
        "Семищенко Христофор Онуфр1йович",
        "Семищенко Христофор О.",
        "Семищенкомищенко Христофористофор Онуфрійовичуфрійовичуфрійович",
        _original_name + "     ",
        "     " + _original_name,
        "     "]

    _test_data_emails = [
        "",
        "@gmail.com",
        "address@.com",
        "address@gmail",
        "address@gmail@com",
        "voron-rozumna.anna-marija@many-many.domain.levels.and."
        + "some.more.domain.levels.for.email.testing.gmail.com",
        _original_email+"     ",
        "     " + _original_email,
        "     "]

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        super(NegativeTests, self).setUp()

    def _set_test_data_name(self):
        """ Creating initial data for each test """

        self.name = self._test_data_names[self.current_test]
        self.email = self._original_email

    def _set_test_data_email(self):
        """ Creating initial data for each test """

        self.name = self._original_name
        self.email = self._test_data_emails[self.current_test]

    def _test_steps_name(self):
        """ Common tests steps """

        self.passed = False

        driver = self.driver
        driver.find_element_by_xpath(self._xpaths["edit_button"]).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self._xpaths["frame_title"])

        input_name = driver.find_element_by_xpath(self._xpaths["input_name"])
        input_name.clear()
        input_name.send_keys(self.name.decode('utf-8'))
        input_name.send_keys(Keys.TAB)

        input_email = driver.find_element_by_xpath(self._xpaths["input_email"])
        input_email.clear()
        input_email.send_keys(self.email.decode('utf-8'))
        input_email.send_keys(Keys.TAB)
        driver.find_element_by_xpath(self._xpaths["confirm_btn"]).click()

        msg1 = "Page changed, profile editing passed"
        msg2 = "Negative test failed - " + self.name + " " + self.email

        self.assertNotEqual(
            len(driver.find_elements_by_xpath(self._xpaths["frame_title"])),
            0, msg1 + msg2)

        warnings = driver.find_elements_by_xpath(self._xpaths["confirm_btn"])
        expected = self._warnings["name"]
        self.assertIsNot(
            any(expected.decode('utf-8') == warning.text
                for warning in warnings),
            msg2)

        self.passed = True

    def _test_steps_email(self):
        """ Common tests steps """

        self.passed = False

        driver = self.driver
        driver.find_element_by_xpath(self._xpaths["edit_button"]).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self._xpaths["frame_title"])

        input_name = driver.find_element_by_xpath(self._xpaths["input_name"])
        input_name.clear()
        input_name.send_keys(self.name.decode('utf-8'))
        input_name.send_keys(Keys.TAB)

        input_email = driver.find_element_by_xpath(self._xpaths["input_email"])
        input_email.clear()
        input_email.send_keys(self.email.decode('utf-8'))
        input_email.send_keys(Keys.TAB)
        driver.find_element_by_xpath(self._xpaths["confirm_btn"]).click()

        msg1 = "Page changed, profile editing passed \n"
        msg2 = "Negative test failed - " + self.name + " " + self.email

        self.assertNotEqual(
            len(driver.find_elements_by_xpath(self._xpaths["frame_title"])),
            0, msg1 + msg2)

        warnings = driver.find_elements_by_xpath(self._xpaths["confirm_btn"])
        expected = self._warnings["email"]
        self.assertIsNot(
            any(expected.decode('utf-8') == warning.text
                for warning in warnings),
            msg2)

        self.passed = True

    def _test_steps_restore(self):
        """ Common tests steps """

        self.passed = False

        driver = self.driver
        driver.find_element_by_xpath(self._xpaths["edit_button"]).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self._xpaths["frame_title"])

        input_name = driver.find_element_by_xpath(self._xpaths["input_name"])
        input_name.clear()
        input_name.send_keys(self.name.decode('utf-8'))
        input_name.send_keys(Keys.TAB)

        input_email = driver.find_element_by_xpath(self._xpaths["input_email"])
        input_email.clear()
        input_email.send_keys(self.email.decode('utf-8'))
        input_email.send_keys(Keys.TAB)
        driver.find_element_by_xpath(self._xpaths["confirm_btn"]).click()

        warnings = driver.find_elements_by_xpath(self._xpaths["confirm_btn"])
        for warning in warnings:
            msg = "Positive test failed - " + self.name + " " + self.email
            self.assertNotEqual(self._warnings["name"].decode('utf-8'),
                                warning.text,
                                msg)
            self.assertNotEqual(self._warnings["email"].decode('utf-8'),
                                warning.text,
                                msg)

        self.assertIn(self.name.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//h3[@class='only-bottom-margin']").text)

        self.assertIn(self.email.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//div[@class='col-md-8']").text)
        self.passed = True

    def test_11_empty_name(self):
        """ 11. Edit profile with empty name """

        self.current_test = 0
        self._set_test_data_name()
        self._test_steps_name()

    def test_12_incorrect_name(self):
        """ 12. Edit profile with incorrect name (first case) """

        self.current_test = 1
        self._set_test_data_name()
        self._test_steps_name()

    def test_13_incorrect_name(self):
        """ 13. Edit profile with incorrect name (second case) """

        self.current_test = 2
        self._set_test_data_name()
        self._test_steps_name()

    def test_14_incorrect_name(self):
        """ 14. Edit profile with incorrect name (third case) """

        self.current_test = 3
        self._set_test_data_name()
        self._test_steps_name()

    def test_15_incorrect_name(self):
        """ 15. Edit profile with incorrect name (fourth case) """

        self.current_test = 4
        self._set_test_data_name()
        self._test_steps_name()

    def test_16_incorrect_name(self):
        """ 16. Edit profile with incorrect name (fifth case) """

        self.current_test = 5
        self._set_test_data_name()
        self._test_steps_name()

    def test_17_incorrect_name(self):
        """ 17. Edit profile with incorrect name (sixth case) """

        self.current_test = 6
        self._set_test_data_name()
        self._test_steps_name()

    def test_18_incorrect_name(self):
        """ 18. Edit profile with incorrect name (seventh case) """

        self.current_test = 7
        self._set_test_data_name()
        self._test_steps_name()

    def test_19_incorrect_name(self):
        """ 19. Edit profile with incorrect name (eighth case) """

        self.current_test = 8
        self._set_test_data_name()
        self._test_steps_name()

    def test_20_incorrect_name(self):
        """ 20. Edit profile with incorrect name (ninth case) """

        self.current_test = 9
        self._set_test_data_name()
        self._test_steps_name()

    def test_21_incorrect_name(self):
        """ 21. Edit profile with incorrect name (tenth case) """

        self.current_test = 10
        self._set_test_data_name()
        self._test_steps_name()

    def test_22_incorrect_name(self):
        """ 22. Edit profile with incorrect name (eleventh case) """

        self.current_test = 11
        self._set_test_data_name()
        self._test_steps_name()

    def test_23_incorrect_name(self):
        """ 23. Edit profile with incorrect name (twelfth case) """

        self.current_test = 12
        self._set_test_data_name()
        self._test_steps_name()

    def test_24_incorrect_name(self):
        """ 24. Edit profile with incorrect name (thirteenth case) """

        self.current_test = 13
        self._set_test_data_name()
        self._test_steps_name()

    def test_25_incorrect_name(self):
        """ 25. Edit profile with incorrect name (fourteenth case) """

        self.current_test = 14
        self._set_test_data_name()
        self._test_steps_name()

    def test_26_incorrect_name(self):
        """ 26. Edit profile with correct name that begins with spaces """

        self.current_test = 15
        self._set_test_data_name()
        self._test_steps_name()

    def test_27_incorrect_name(self):
        """ 27. Edit profile with correct name that ends with spaces """

        self.current_test = 16
        self._set_test_data_name()
        self._test_steps_name()

    def test_28_incorrect_name(self):
        """ 28. Edit profile with correct name that consists from spaces """

        self.current_test = 17
        self._set_test_data_name()
        self._test_steps_name()

    def test_29_empty_email(self):
        """ 26. Edit profile with empty email """

        self.current_test = 0
        self._set_test_data_email()
        self._test_steps_email()

    def test_30_incorrect_email(self):
        """ 30. Edit profile with incorrect email (first case) """

        self.current_test = 1
        self._set_test_data_email()
        self._test_steps_email()

    def test_31_incorrect_email(self):
        """ 31. Edit profile with incorrect email (second case) """

        self.current_test = 2
        self._set_test_data_email()
        self._test_steps_email()

    def test_32_incorrect_email(self):
        """ 32. Edit profile with incorrect email (third case) """

        self.current_test = 3
        self._set_test_data_email()
        self._test_steps_email()

    def test_33_incorrect_email(self):
        """ 33. Edit profile with incorrect email (fourth case) """

        self.current_test = 4
        self._set_test_data_email()
        self._test_steps_email()

    def test_34_incorrect_email(self):
        """ 34. Edit profile with incorrect email (fifth case) """

        self.current_test = 5
        self._set_test_data_email()
        self._test_steps_email()

    def test_35_incorrect_email(self):
        """ 35. Edit profile with correct name that begins with spaces """

        self.current_test = 6
        self._set_test_data_email()
        self._test_steps_email()

    def test_36_incorrect_email(self):
        """ 36. Edit profile with correct name that ends with spaces """

        self.current_test = 7
        self._set_test_data_email()
        self._test_steps_email()

    def test_37_incorrect_email(self):
        """ 37. Edit profile with correct name that consists from spaces """

        self.current_test = 8
        self._set_test_data_email()
        self._test_steps_email()

    def tearDown(self):
        """ Fixture that deletes all preparation for tests and restores
        original data
        """

        if not self.passed:
            self.name = self._original_name
            self.email = self._original_email
            self._test_steps_restore()

        super(NegativeTests, self).tearDown()


if __name__ == "__main__":
    unittest.main(verbosity=2)
