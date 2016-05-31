# -*- coding: utf-8 -*-
""" Tests on Selenium WebDriver of school CRUD """

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class SchoolCRUDTests(unittest.TestCase):
    """ Class with methods, for testing School CRUD """

    _baseurl = "https://smsauto-dvatqc.rhcloud.com"
    _username = "semuschenko"
    _password = "pDk7jf"
    _warnings = {
        'incorrectName': u"Некоректно введено назву.",
        'incorrectAddress': u"Некоректно введено адресу.",
        'alreadyExistsName': u"Школа з такою назвою вже існує."
    }
    _xpaths = {
        'inputUsername': "//input[@name='inputUsername']",
        'inputPassword': "//input[@name='inputPassword']",
        'submitButtonLogin': "button",
        'inputSchoolName': "//*[@id='inputSchoolName']",
        'inputSchoolAddress': "//*[@id='inputNumber']",
        'confirmAddEditButton': "//*[@id='add_button']",
        'buttonEditSchool': "//*[@id='5']/td[4]/a[1]",
        'selectionOfDiretor': "//select[@name='director']",
        'buttonDeleteSchool': "//*[@id='100']/td[4]/a[2]"

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
        'addressStartingUpper': u'ВУЛ. Макарова, 19',
        'schoolToDelete': u'вул. Тестова, 1'
    }

    def _credetials_to_add_school(self, driver, school_name, address):
        """ Function to automate proccess of inserting the credentials """

        driver.find_element_by_link_text(u'+ Додати').click()
        driver.find_element_by_xpath(
            self._xpaths['inputSchoolName']).send_keys(
            school_name)
        driver.find_element_by_xpath(
            self._xpaths['inputSchoolAddress']).send_keys(
            address)

        driver.find_element_by_xpath(
            self._xpaths['confirmAddEditButton']).click()

    def _credetials_to_edit_school(self,
                                   driver,
                                   school_name,
                                   address,
                                   xpath_of_school_to_edit,
                                   xpath_of_director):
        """ Function to automate proccess of inserting the credentials """

        driver.find_element_by_xpath(xpath_of_school_to_edit).click()
        input_name_area = driver.find_element_by_xpath(
            self._xpaths['inputSchoolName'])
        input_address_area = driver.find_element_by_xpath(
            self._xpaths['inputSchoolAddress'])
        input_name_area.clear()
        input_name_area.send_keys(school_name)
        input_address_area.clear()
        input_address_area.send_keys(address)

        driver.find_element_by_xpath(
            xpath_of_director).click()

        select = Select(driver.find_element_by_xpath(xpath_of_director))

        select.select_by_value('12')
        driver.find_element_by_xpath(
            self._xpaths['confirmAddEditButton']).click()

    def _check_for_element_existence(self, driver, warning):
        """ Function to check whether element exists on the web-page """

        self.page_content = driver.page_source
        if warning in self.page_content:
            warning_exists = True
        else:
            warning_exists = False

        return warning_exists

    def setUp(self):
        """ Fixture that creates all the preparations for tests """

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.accept_next_alert = True
        self.driver.get(self._baseurl)
        self.driver.find_element_by_xpath(
            self._xpaths['inputUsername']).send_keys(
            self._username)

        self.driver.find_element_by_xpath(
            self._xpaths['inputPassword']).send_keys(
            self._password)

        self.driver.find_element_by_tag_name(
            self._xpaths['submitButtonLogin']).click()

    def tearDown(self):
        """ Fixture that deletes all the preparations for tests """

        self.driver.close()

    def test01_ui_to_add_schools_exists(self):
        """ Test to check whether windows to add school exists """

        self.driver.find_element_by_link_text(u'+ Додати').click()
        self.element = self.driver.find_element_by_tag_name('h3')

        self.assertEquals(u"Додати школу", self.element.text)

    def test02_cancel_button(self):
        """
        Fields to enter credentials should be empty after cancel and retry
        """

        link = self.driver.find_element_by_link_text(u'+ Додати')
        link.click()
        self.driver.find_element_by_xpath(
            self._xpaths['inputSchoolName']).send_keys(
            self._credentials['correctName'])
        self.driver.find_element_by_xpath(
            self._xpaths['inputSchoolAddress']).send_keys(
            self._credentials['correctAddress'])
        link2 = self.driver.find_element_by_link_text('x')
        link2.click()
        link.click()
        name_value = self.driver.find_element_by_xpath(self._xpaths[
                                                           'inputSchoolName'])
        address_value = self.driver.find_element_by_xpath(
            self._xpaths['inputSchoolAddress'])

        self.assertTrue(("" == name_value.get_attribute('value')) and
                        ("" == address_value.get_attribute('value')))

    def test03_add_school_with_correct_credentials_POSITIVE(self):
        """ New school should be added with correct credentials """

        self._credetials_to_add_school(self.driver,
                                       self._credentials['correctName'],
                                       self._credentials[
                                           'correctAddress'])
        self.driver.refresh()
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._credentials['correctName']), True)

    def test04_add_school_with_roman_name_NEGATIVE(self):
        """ Expected warning about incorrect name """

        self._credetials_to_add_school(self.driver,
                                       self._credentials['nameRoman'],
                                       self._credentials[
                                           'correctAddress'])

        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectName']), True)

    def test05_add_school_with_roman_address_NEGATIVE(self):
        """ Expected warning about incorrect address """

        self._credetials_to_add_school(self.driver,
                                       "",
                                       self._credentials[
                                           'addressRoman'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectAddress']), True)

    def test06_add_school_with_empty_name_NEGATIVE(self):
        """ Expected warning about incorrect name """

        self._credetials_to_add_school(self.driver, "",
                                       self._credentials[
                                           'correctAddress'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectName']), True)

    def test07_add_school_with_empty_address_NEGATIVE(self):
        """ Expected warning about incorrect address """

        self._credetials_to_add_school(self.driver,
                                       self._credentials[
                                           'correctNameForEdit'],
                                       "")
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectAddress']), True)

    def test08_add_school_with_wrong_cyrrilic_name_NEGATIVE(self):
        """ Expected warning about incorrect name """

        self._credetials_to_add_school(self.driver,
                                       self._credentials[
                                           'cyrrilicNameWrong'],
                                       "")
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectName']), True)

    def test09_add_school_with_wrong_cyrrilic_address_NEGATIVE(self):
        """ Expected warning about incorrect address """

        self._credetials_to_add_school(self.driver, "",
                                       self._credentials[
                                           'cyrrilicAddressWrong'], )
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectAddress']), True)

    def test10_add_school_with_already_exists_name_NEGATIVE(self):
        """ Expected warning about already existing name for school """

        self._credetials_to_add_school(self.driver,
                                       self._credentials[
                                           'correctName'],
                                       self._credentials[
                                           'correctAddress'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['alreadyExistsName']), True)

    def test11_add_school_with_name_lower_case_NEGATIVE(self):
        """ Expected warning about incorrect name """

        self._credetials_to_add_school(self.driver,
                                       self._credentials[
                                           'nameStartingLower'],
                                       self._credentials[
                                           'correctAddress'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectName']), True)

    def test12_add_school_with_address_upper_case_NEGATIVE(self):
        """ Expected warning about incorrect address """

        self._credetials_to_add_school(self.driver,
                                       self._credentials[
                                           'correctNameForEdit'],
                                       self._credentials[
                                           'addressStartingUpper'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectAddress']), True)

    def test13_ui_to_edit_schools_exists(self):
        """ Test to check whether windows to edit school exists """

        self.driver.find_element_by_xpath(
            self._xpaths['buttonEditSchool']).click()
        self.element_to_test = self.driver.find_element_by_tag_name('h3')

        self.assertEquals(u"Редагувати школу", self.element_to_test.text)

    def test14_edit_school_with_correct_credentials_POSITIVE(self):
        """ The school should be edited with correct credentials """

        src_before = self.driver.page_source
        if self._credentials['correctNameForEdit'] in src_before:
            school_exists = True
        else:
            school_exists = False
        self._credetials_to_edit_school(self.driver,
                                        self._credentials[
                                            'correctNameForEdit'],
                                        self._credentials[
                                            'correctAddressForEdit'],
                                        self._xpaths[
                                            'buttonEditSchool'],
                                        self._xpaths[
                                            'selectionOfDiretor']
                                        )
        self.driver.switch_to_alert().accept()
        self.driver.refresh()
        self.assertEqual(school_exists, False)

    def test15_edit_school_with_roman_name_NEGATIVE(self):
        """Expected warning about incorrect name"""

        self._credetials_to_edit_school(self.driver,
                                        self._credentials['nameRoman'],
                                        self._credentials[
                                            'correctAddress'],
                                        self._xpaths[
                                            'buttonEditSchool'],
                                        self._xpaths[
                                            'selectionOfDiretor'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectName']), True)

    def test16_edit_school_with_roman_address_NEGATIVE(self):
        """Expected warning about incorrect address"""

        self._credetials_to_edit_school(self.driver,
                                        self._credentials[
                                            'correctName'],
                                        self._credentials[
                                            'addressRoman'],
                                        self._xpaths[
                                            'buttonEditSchool'],
                                        self._xpaths[
                                            'selectionOfDiretor'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectAddress']), True)

    def test17_edit_school_with_empty_name_NEGATIVE(self):
        """ Expected warning about incorrect name """

        self._credetials_to_edit_school(self.driver,
                                        "",
                                        self._credentials[
                                            'addressRoman'],
                                        self._xpaths[
                                            'buttonEditSchool'],
                                        self._xpaths[
                                            'selectionOfDiretor'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectName']), True)

    def test18_edit_school_with_empty_address_NEGATIVE(self):
        """ Expected warning about incorrect address """

        self._credetials_to_edit_school(self.driver,
                                        self._credentials[
                                            'correctName'],
                                        "",
                                        self._xpaths[
                                            'buttonEditSchool'],
                                        self._xpaths[
                                            'selectionOfDiretor'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectAddress']), True)

    def test19_edit_school_with_wrong_cyrrilic_name_NEGATIVE(self):
        """ Expected warning about incorrect name """

        self._credetials_to_edit_school(self.driver,
                                        self._credentials[
                                            'cyrrilicNameWrong'],
                                        self._credentials[
                                            'correctAddressForEdit'],
                                        self._xpaths[
                                            'buttonEditSchool'],
                                        self._xpaths[
                                            'selectionOfDiretor'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectName']), True)

    def test20_edit_school_with_wrong_cyrrilic_address_NEGATIVE(self):
        """ Expected warning about incorrect address """

        self._credetials_to_edit_school(self.driver,
                                        self._credentials[
                                            'correctName'],
                                        self._credentials[
                                            'cyrrilicAddressWrong'],
                                        self._xpaths[
                                            'buttonEditSchool'],
                                        self._xpaths[
                                            'selectionOfDiretor'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectAddress']), True)

    def test21_edit_school_with_already_exists_name_NEGATIVE(self):
        """ Expected warning about already existing name for school """

        self._credetials_to_edit_school(self.driver,
                                        self._credentials[
                                            'correctName'],
                                        self._credentials[
                                            'correctAddress'],
                                        self._xpaths[
                                            'buttonEditSchool'],
                                        self._xpaths[
                                            'selectionOfDiretor'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['alreadyExistsName']), True)

    def test22_edit_school_with_name_lower_case_NEGATIVE(self):
        """ Expected warning about incorrect name """

        driver = self.driver
        self._credetials_to_edit_school(driver,
                                        self._credentials[
                                            'nameStartingLower'],
                                        self._credentials[
                                            'correctAddress'],
                                        self._xpaths[
                                            'buttonEditSchool'],
                                        self._xpaths[
                                            'selectionOfDiretor'])
        self.assertEqual(
            self._check_for_element_existence(
                driver, self._warnings['incorrectName']), True)

    def test23_edit_school_with_address_upper_case_NEGATIVE(self):
        """ Expected warning about incorrect address """

        self._credetials_to_edit_school(self.driver,
                                        self._credentials[
                                            'correctName'],
                                        self._credentials[
                                            'addressStartingUpper'],
                                        self._xpaths[
                                            'buttonEditSchool'],
                                        self._xpaths[
                                            'selectionOfDiretor'])
        self.assertEqual(
            self._check_for_element_existence(
                self.driver, self._warnings['incorrectAddress']), True)

    def test24_edit_school_from_main_page_POSITIVE(self):
        """Test to check whether director can be changed from main page"""

        self.driver.find_element_by_xpath('//*[@id="4"]/td[3]').click()
        self.driver.find_element_by_xpath(
            "//option[contains(.,'Петросян Іван Сергієвич')]").click()
        self.driver.find_element_by_xpath(
            "//*[@id='list']/table/thead/tr/th[1]").click()

        self.assertEquals(self.driver.find_element_by_xpath(
            "//option[contains(.,'Петросян Іван Сергієвич')]").is_selected(),
                          True)

    def test25_delete_school_POSITIVE(self):
        """Test to check whether delete school function works"""

        self.driver.find_element_by_xpath(
            self._xpaths['buttonDeleteSchool']).click()
        self.driver.find_element_by_xpath(
            "//*[@id='form']/form/input[3]").click()

        self.assertEqual(self._check_for_element_existence
                         (self.driver,
                          self._credentials['schoolToDelete']),
                         False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
