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

    def setUp(self):
        """ Fixture that creates a initial data and records for tests,
        initial test steps
        """

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
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
        03. Check, that clicking on the link to edit profile opens the frame to edit profile opened
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

        # waiter = WebDriverWait(driver, 30)
        # waiter.until(lambda x: x.find_element_by_xpath("//h3[contains(.,'Редагувати профіль')]"))
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
    expected result - data in profile is changed
    """

    xpaths = TestPreparations.xpaths

    warnings = TestPreparations.warnings

    # test_data = [
    # ["Іванов Петро Степанович", "email@domain.com"],
    #     ["Стець Мар'яна Іванівна", "marjana.stetc@gmail.com"],
    #     ["Ворон-Розумна Анна-Марія Степанівна", "email@domain.com"],
    #     ["Ворон-Розумна Анна Степанівна", "email@domain.com"],
    #     ["Ворон Анна-Марія Степанівна", "email@domain.com"],
    #     ["Ворон Анна Степанівна",
    #      "voron-rozumna.anna-marija@many-many.domain.levels.gmail.com"],
    # ]

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        super(PositiveTests, self).setUp()

    # def _set_test_data(self):
    #     """ Creating initial data for each test """
    #
    #     self.name = self.test_data[self.current_test][0]
    #     self.email = self.test_data[self.current_test][1]

    def _test_steps(self):
        """ Common tests steps """

        self.passed = False

        driver = self.driver
        driver.find_element_by_xpath(self.xpaths["edit_button"]).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.xpaths["frame_title"])
        # waiter = WebDriverWait(driver, 30)
        # waiter.until(lambda x: x.find_element_by_xpath(self._xpaths["frame_title"]))

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
        """ 01. Edit profile with correct data (first case) """

        self.name = "Іванов Петро Степанович"
        self.email = "email@domain.com"
        self._test_steps()

    def test02_correct_name(self):
        """ 02. Edit profile with correct data (second case) """

        self.name = "Стець Мар'яна Іванівна"
        self.email = "marjana.stetc@gmail.com"
        self._test_steps()

    def test03_correct_name(self):
        """ 03. Edit profile with correct data (third case) """

        self.name = "Ворон-Розумна Анна-Марія Степанівна"
        self.email = "email@domain.com"
        self._test_steps()

    def test04_correct_name(self):
        """ 04. Edit profile with correct data (fourth case) """

        self.name = "Ворон-Розумна Анна Степанівна"
        self.email = "email@domain.com"
        self._test_steps()

    def test05_correct_name(self):
        """ 05. Edit profile with correct data (fifth case) """

        self.name = "Ворон Анна-Марія Степанівна"
        self.email = "email@domain.com"
        self._test_steps()

    def test06_correct_name(self):
        """ 06. Edit profile with correct data (sixth case) """

        self.name = "Ворон Анна Степанівна"
        self.email = "voron-rozumna.anna-marija@" \
                     "many-many.domain.levels.gmail.com"
        self._test_steps()

    def tearDown(self):
        """ Fixture that deletes all preparation for tests and restores
        original data
        """

        if self.passed:
            self.name = self.original_name
            self.email = self.original_email
            self._test_steps()

        super(PositiveTests, self).tearDown()


class NegativeTests(TestPreparations):
    """ Negative tests for Edit Profile with incorrect data,
    expected result - login is successful
    """

    xpaths = TestPreparations.xpaths

    warnings = TestPreparations.warnings

    original_name = TestPreparations.original_name
    original_email = TestPreparations.original_email

    # test_data_names = [
    # "",
    #     "Мадонна",
    #     "Мурзік Васильович",
    #     "Василь Перебійніс",
    #     "John",
    #     "John Smith",
    #     "John Alexander Smith",
    #     "John A. Smith",
    #     "бОРИС бОРИС бОРИСОВИЧ",
    #     "Борис Борис Борисович Молодший",
    #     "Cемищенко Xристофор Oнуфрійович",
    #     "Семищенко_Христофор_Онуфрійович",
    #     "Семищенко Христофор Онуфр1йович",
    #     "Семищенко Христофор О.",
    #     "Семищенкомищенко Христофористофор Онуфрійовичуфрійовичуфрійович",
    #     original_name + "     ",
    #     "     " + original_name,
    #     "     "]

    # test_data_emails = [
    #     "",
    #     "@gmail.com",
    #     "address@.com",
    #     "address@gmail",
    #     "address@gmail@com",
    #     "voron-rozumna.anna-marija@many-many.domain.levels.and."
    #     + "some.more.domain.levels.for.email.testing.gmail.com",
    #     original_email+"     ",
    #     "     " + original_email,
    #     "     "]

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        super(NegativeTests, self).setUp()

    # def _set_test_data_name(self):
    #     """ Creating initial data for each test """
    #
    #     self.name = self.test_data_names[self.current_test]
    #     self.email = self.original_email

    # def _set_test_data_email(self):
    #     """ Creating initial data for each test """
    #
    #     self.name = self.original_name
    #     self.email = self.test_data_emails[self.current_test]

    def _test_steps_name(self):
        """ Common tests steps """

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

        msg1 = "Page changed, profile editing passed"
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
        """ 01. Edit profile with empty name """

        self.name = ""
        self.email = self.original_email
        self._test_steps_name()

    def test02_incorrect_name(self):
        """ 02. Edit profile with incorrect name (first case) """

        self.name = "Мадонна"
        self.email = self.original_email
        self._test_steps_name()

    def test03_incorrect_name(self):
        """ 03. Edit profile with incorrect name (second case) """

        self.name = "Мурзік Васильович"
        self.email = self.original_email
        self._test_steps_name()

    def test04_incorrect_name(self):
        """ 04. Edit profile with incorrect name (third case) """

        self.name = "Василь Перебійніс"
        self.email = self.original_email
        self._test_steps_name()

    def test05_incorrect_name(self):
        """ 05. Edit profile with incorrect name (fourth case) """

        self.name = "John"
        self.email = self.original_email
        self._test_steps_name()

    def test06_incorrect_name(self):
        """ 06. Edit profile with incorrect name (fifth case) """

        self.name = "John Smith"
        self.email = self.original_email
        self._test_steps_name()

    def test07_incorrect_name(self):
        """ 07. Edit profile with incorrect name (sixth case) """

        self.name = "John Alexander Smith"
        self.email = self.original_email
        self._test_steps_name()

    def test08_incorrect_name(self):
        """ 08. Edit profile with incorrect name (seventh case) """

        self.name = "John A. Smith"
        self.email = self.original_email
        self._test_steps_name()

    def test09_incorrect_name(self):
        """ 09. Edit profile with incorrect name (eighth case) """

        self.name = "бОРИС бОРИС бОРИСОВИЧ"
        self.email = self.original_email
        self._test_steps_name()

    def test10_incorrect_name(self):
        """ 10. Edit profile with incorrect name (ninth case) """

        self.name = "Борис Борис Борисович Молодший"
        self.email = self.original_email
        self._test_steps_name()

    def test11_incorrect_name(self):
        """ 11. Edit profile with incorrect name (tenth case) """

        self.name = "Cемищенко Xристофор Oнуфрійович"
        self.email = self.original_email
        self._test_steps_name()

    def test12_incorrect_name(self):
        """ 12. Edit profile with incorrect name (eleventh case) """

        self.name = "Семищенко_Христофор_Онуфрійович"
        self.email = self.original_email
        self._test_steps_name()

    def test13_incorrect_name(self):
        """ 13. Edit profile with incorrect name (twelfth case) """

        self.name = "Семищенко Христофор Онуфр1йович"
        self.email = self.original_email
        self._test_steps_name()

    def test14_incorrect_name(self):
        """ 14. Edit profile with incorrect name (thirteenth case) """

        self.name = "Семищенко Христофор О."
        self.email = self.original_email
        self._test_steps_name()

    def test15_incorrect_name(self):
        """ 15. Edit profile with incorrect name (fourteenth case) """

        self.name = "Семищенкомищенко Христофористофор " \
                    "Онуфрійовичуфрійовичуфрійович"
        self.email = self.original_email
        self._test_steps_name()

    def test16_incorrect_name(self):
        """ 16. Edit profile with correct name that begins with spaces """

        self.name = self.original_name + "     "
        self.email = self.original_email
        self._test_steps_name()

    def test17_incorrect_name(self):
        """ 17. Edit profile with correct name that ends with spaces """

        self.name = "     " + self.original_name
        self.email = self.original_email
        self._test_steps_name()

    def test18_incorrect_name(self):
        """ 18. Edit profile with correct name that consists from spaces """

        self.name = "     "
        self.email = self.original_email
        self._test_steps_name()

    def _test_steps_email(self):
        """ Common tests steps """

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
        """ 51. Edit profile with empty email """

        self.name = self.original_name
        self.email = ""
        self._test_steps_email()

    def test52_incorrect_email(self):
        """ 52. Edit profile with incorrect email (first case) """

        self.name = self.original_name
        self.email = "@gmail.com"
        self._test_steps_email()

    def test53_incorrect_email(self):
        """ 53. Edit profile with incorrect email (second case) """

        self.name = self.original_name
        self.email = "address@.com"
        self._test_steps_email()

    def test54_incorrect_email(self):
        """ 54. Edit profile with incorrect email (third case) """

        self.name = self.original_name
        self.email = "address@gmail"
        self._test_steps_email()

    def test55_incorrect_email(self):
        """ 55. Edit profile with incorrect email (fourth case) """

        self.name = self.original_name
        self.email = "address@gmail@com"
        self._test_steps_email()

    def test56_incorrect_email(self):
        """ 56. Edit profile with incorrect email (fourth case) """

        self.name = self.original_name
        self.email = "address.gmail.com"
        self._test_steps_email()

    def test57_incorrect_email(self):
        """ 57. Edit profile with incorrect email (fifth case) """

        self.name = self.original_name
        self.email = "voron-rozumna.anna-marija@many-many.domain.levels.and." \
                     "some.more.domain.levels.for.email.testing.gmail.com"
        self._test_steps_email()

    def test58_incorrect_email(self):
        """ 58. Edit profile with correct name that begins with spaces """

        self.name = self.original_name
        self.email = self.original_email + "     "
        self._test_steps_email()

    def test59_incorrect_email(self):
        """ 59. Edit profile with correct name that ends with spaces """

        self.name = self.original_name
        self.email = "     " + self.original_email
        self._test_steps_email()

    def test60_incorrect_email(self):
        """ 60. Edit profile with correct name that consists from spaces """

        self.name = self.original_name
        self.email = "     "
        self._test_steps_email()

    def _test_steps_restore(self):
        """ Common tests steps """

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
        original data
        """

        if not self.passed:
            self.name = self.original_name
            self.email = self.original_email
            self._test_steps_restore()

        super(NegativeTests, self).tearDown()


if __name__ == "__main__":
    unittest.main(verbosity=2)
