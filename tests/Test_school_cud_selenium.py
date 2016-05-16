# -*- coding: utf-8 -*-
""" Tests on Selenium WebDriver of school CUD """

import unittest
from selenium import webdriver


class SchoolCUD(unittest.TestCase):
    """ Class with methods, for testing School CUD """
    _baseurl = "https://smsauto-dvatqc.rhcloud.com"
    _username = "semuschenko"
    _password = "pDk7jf"
    _nameWarning = u"Некоректно введено назву."
    _addressWarning = u"Некоректно введено адресу."

    _xpaths = {
        'inputUsername': "//input[@name='inputUsername']",
        'inputPassword': "//input[@name='inputPassword']",
        'submitButtonLogin': "button",
        'inputSchoolName': "//*[@id='inputSchoolName']",
        'inputSchoolAddress': "//*[@id='inputNumber']",
        'confirmAddEditButton': "//*[@id='add_button']"
    }

    _credentials = {
        'correctAddress': u'вул. Євгена Коновальця, 19',
        'correctName': u'Школа №28',
        'correctName2': u'Школа №80',
        'nameRoman': 'School #28',
        'addressRoman': 'Verbova Street, 35',
        'cyrrilicAddressWrong': u'Адреса 200',
        'cyrrilicNameWrong': u'Школа 100',
        'correctAddressForEdit': u'вул. Мельника, 67',
        'correctNameForEdit': u'Школа №25',
        'nameStartingLower': u'нвк "веселка"',
        'addressStartingUpper': u'ВУЛ. Макарова, 19'
    }

    def _insertCredetialsToAddSchool(self, driver, schoolName, address):
        """ Function to automate proccess of inserting the credentials """

        link = driver.find_element_by_link_text(u'+ Додати')
        link.click()
        # time.sleep(2)
        driver.find_element_by_xpath(self._xpaths['inputSchoolName']).send_keys(
            schoolName)
        driver.find_element_by_xpath(self._xpaths['inputSchoolAddress']).send_keys(
            address)
        # time.sleep(2)
        driver.find_element_by_xpath(self._xpaths['confirmAddEditButton']).click()

    def setUp(self):
        """ Fixture that creates all the preparations for tests """

        self.driver = webdriver.Firefox()

        self.driver.maximize_window()

        self.driver.implicitly_wait(30)

        self.accept_next_alert = True

        self.driver.get(self._baseurl)

        self.driver.find_element_by_xpath(self._xpaths['inputUsername']).send_keys(
            self._username)

        self.driver.find_element_by_xpath(self._xpaths['inputPassword']).send_keys(
            self._password)

        self.driver.find_element_by_tag_name(
            self._xpaths['submitButtonLogin']).click()

    def tearDown(self):
        """ Fixture that deletes all the preparations for tests """

        self.driver.close()

    def test_ui_to_add_schools_exists(self):
        """ Test to check whether windows to add school exists """

        driver = self.driver

        link = driver.find_element_by_link_text(u'+ Додати')

        link.click()

        # time.sleep(2)

        self.element = driver.find_element_by_tag_name('h3')

        self.assertEquals(u"Додати школу", self.element.text)

    def test_cancel_button(self):
        """
        Fields to enter credentials should be empty after cancel and retry
        """

        driver = self.driver

        link = driver.find_element_by_link_text(u'+ Додати')

        link.click()

        # time.sleep(2)

        driver.find_element_by_xpath(self._xpaths['inputSchoolName']).send_keys(
            self._credentials['correctName'])

        driver.find_element_by_xpath(self._xpaths['inputSchoolAddress']).send_keys(
            self._credentials['correctAddress'])

        link2 = driver.find_element_by_link_text('x')

        link2.click()

        link.click()

        # time.sleep(2)

        nameValue = driver.find_element_by_xpath(xpaths['inputSchoolName'])

        addressValue = driver.find_element_by_xpath(
            self._xpaths['inputSchoolAddress'])

        self.assertTrue(("" == nameValue.get_attribute('value')) and
                        ("" == addressValue.get_attribute('value')))

    def test_add_school_with_correct_credentials(self):
        """ New school should be added with correct credentials """

        driver = self.driver

        self._insertCredetialsToAddSchool(driver, self._credentials['correctName'],
                                    self._credentials['correctAddress'])

        src = driver.page_source

        if self._credentials['correctName'] in src:
            school_exists = True

        else:
            school_exists = False

        self.assertEqual(school_exists, True)

    def test_add_school_with_roman_name(self):
        """ Expected warning about incorrect name """

        driver = self.driver
        self._insertCredetialsToAddSchool(driver, self._credentials['nameRoman'],
                                    self._credentials['correctAddress'])
        src = driver.page_source

        if self._addressWarning in src:
            warning_exists = True

        else:
            warning_exists = False

        self.assertEqual(warning_exists, True)

    def test_add_school_with_roman_address(self):
        """ Expected warning about incorrect address """

        driver = self.driver

        self._insertCredetialsToAddSchool(driver, "", self._credentials['addressRoman'])

        src = driver.page_source

        if self._addressWarning in src:
            warning_exists = True

        else:
            warning_exists = False

        self.assertEqual(warning_exists, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
