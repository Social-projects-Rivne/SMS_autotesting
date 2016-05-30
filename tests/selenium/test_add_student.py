# -*- coding: utf-8 -*-
""" Tests on Selenium WebDriver add students to class function"""


import unittest
from selenium import webdriver

xpaths = {
    'inputUsername': "//input[@name='inputUsername']",
    'inputPassword': "//input[@name='inputPassword']",
    'submitButtonLogin': "button"
}


class add_students(unittest.TestCase):
    """Class with methods, for testing add student to class"""

    _baseurl = "http://ss-alexeyvasiluk.rhcloud.com/"
    _login_director = "zoshch"
    _password_director = "df5sFdf"
    _cyrillic3 = u"Василюк Олексій Олексійович"
    _cyrillic2 = u"Василюк Дмитро"
    _cyrillic1 = u"Василюк"
    _smallCyrillic = u"василюк олексій олексійович"
    _latin3 = "Vasiluk Alexey Alexeevich"
    _dot = u"Василюк О.О."
    _symbol = u"Карпенко-Карий Іван Іванович"
    _warning = u"Некоректно введено ім'я."

    def _check_for_element_existence(self, driver, element):
        """Method for elements compare"""
        src = driver.page_source
        if element in src:
            element_exist = True
        else:
            element_exist = False
        return element_exist

    def setUp(self):
        """ Fixture that creates all the preparations for tests """
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self._baseurl)
        self.driver.find_element_by_xpath(xpaths['inputUsername']).send_keys(
            self._login_director)
        self.driver.find_element_by_xpath(xpaths['inputPassword']).send_keys(
            self._password_director)
        self.driver.find_element_by_tag_name(xpaths['submitButtonLogin']). \
            click()
        self.driver.find_element_by_xpath(
            "//a[@href='/director/student_list/17']").click()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """ Fixture that deletes all the preparations for tests """
        self.driver.close()

    def test01_ui_checks_profile_exist(self):
        """Checks that the class profile is exist"""
        self.page_header = self.driver.find_element_by_tag_name('h4')
        self.assertEquals(u'Керування учнями 1А класу', self.page_header.text)

    def test02_ui_checks_profile_open_to_edit(self):
        """Checks that the class profile is open to edit"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        self.page_header = self.driver.find_element_by_tag_name('h3')
        self.assertEquals(u'Додати учня', self.page_header.text)

    def test03_ui_checks_profile_field_to_edit(self):
        """Checks that the class profile have active fields for edit"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        input_field = self.driver.find_element_by_xpath(
            "//input[@id='inputName']")
        self.assertIsNotNone(input_field)

    def test04_ui_checks_profile_confirm_button(self):
        """Checks that the class profile have confirm button"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        add_button = self.driver.find_element_by_name('add_button')
        self.assertIsNotNone(add_button)

    def test05_ui_checks_profile_reset_button(self):
        """Checks that the class profile have reset button"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        reset_button = self.driver.find_element_by_xpath(
            "//a[@href='/director/student_list/17']")
        self.assertIsNotNone(reset_button)

    def test06_ui_checks_profile_disable_button(self):
        """Checks that the class profile have disable button"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        disable_button = self.driver.find_element_by_xpath("//a[@href='#']")
        self.assertIsNotNone(disable_button)

    def test07_add_student_with_classic_cyrillic_name_POSITIVE(self):
        """New student should be added with classic cyrillic name"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        self.driver.find_element_by_name('name').send_keys(self._cyrillic3)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._cyrillic3), True)

    def test08_add_student_name_without_second_name_NEGATIVE(self):
        """Add students to class with cyrillic name without second name"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        self.driver.find_element_by_name('name').send_keys(self._cyrillic2)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test09_add_student_name_withonly_surname_NEGATIVE(self):
        """Add students to class with cyrillic name with surname only"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        self.driver.find_element_by_name('name').send_keys(self._cyrillic1)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test10_add_student_name_with_small_letter_name_NEGATIVE(self):
        """Add students to class with cyrillic name(first small letter)"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        self.driver.find_element_by_name('name').send_keys(self._smallCyrillic)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test11_add_student_name_with_latin_name_NEGATIVE(self):
        """Add students to class with classic latin name"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        self.driver.find_element_by_name('name').send_keys(self._latin3)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test12_add_student_name_with_short_name_NEGATIVE(self):
        """Add students to class with classic cyrillic name(short name)"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        self.driver.find_element_by_name('name').send_keys(self._dot)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test13_add_student_name_with_line_name_NEGATIVE(self):
        """Add students to class with line in cyrillic name"""
        self.driver.find_element_by_link_text(u'+ Додати').click()
        self.driver.find_element_by_name('name').send_keys(self._symbol)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)


if __name__ == "__main__":
    unittest.main(verbosity=1)
