# -*- coding: utf-8 -*-
""" Tests on Selenium WebDriver add students to class function"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

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
    _capital_cyrillic = u"1Б"
    _small_cyrillic = u"1б"
    _capital_latin = "1D"
    _small_latin = "1s"
    _relocated = "W2"
    _symbol = "1-S"
    _one_letter = u"Д"
    _many_letter = "1DS"
    _one_digit = 1
    _many_digits = u"123Д"
    _all_many = u"123АБВ"
    _warning = u"Некоректно введено назву."
    _no_teacher = u"Виберіть керівника"
    _with_teacher = u"Балашов Юрій Васильович"
    _with_teacher2 = u"Галицький Максим Генадійович"

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
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_css_selector('div.group__item-holder'))
        hover.perform()
        self.driver.find_element_by_xpath(
            "//a[@href='/director/group_edit/17']").click()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """ Fixture that deletes all the preparations for tests """
        self.driver.close()

    def test01_ui_checks_profile_exist(self):
        """Checks that the class profile is open to edit"""
        self.page_header = self.driver.find_element_by_tag_name('h3')
        self.assertEquals(u'Редагувати клас', self.page_header.text)

    def test02_ui_checks_profile_field_to_edit(self):
        """Checks that the class profile have active fields for edit"""
        input_name = self.driver.find_element_by_xpath(
            "//input[@id='inputName']")
        self.assertIsNotNone(input_name)

    def test03_ui_checks_profile_field_to_edit(self):
        """Checks that the class profile have active fields for edit"""
        input_pos = self.driver.find_element_by_name('teacher')
        self.assertIsNotNone(input_pos)

    def test04_ui_checks_profile_confirm_button(self):
        """Checks that the class profile have confirm button"""
        add_button = self.driver.find_element_by_name('add_button')
        self.assertIsNotNone(add_button)

    def test05_ui_checks_profile_reset_button(self):
        """Checks that the class profile have reset button"""
        reset_button = self.driver.find_element_by_xpath(
            "//a[@href='/director/group_list/']")
        self.assertIsNotNone(reset_button)

    def test06_ui_checks_profile_disable_button(self):
        """Checks that the class profile have disable button"""
        disable_button = self.driver.find_element_by_xpath("//a[@href='#']")
        self.assertIsNotNone(disable_button)

    def test07_edit_class_with_capital_cyrillic_name_POSITIVE(self):
        """Editing class profile with capital cyrillic class name"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(
            self._capital_cyrillic)
        self.driver.find_element_by_tag_name('h3').click()
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._capital_cyrillic), True)

    def test08_add_class_with_blank_name_NEGATIVE(self):
        """Editing class profile with blank class name"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test09_edit_class_name_change_indexes_NEGATIVE(self):
        """Editing class name in case of changing places class indexes"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(self._relocated)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test10_edit_class_name_with_capital_latin_NEGATIVE(self):
        """Editing class name with capital latin letter"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(self._capital_latin)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test11_edit_class_name_with_small_latin_NEGATIVE(self):
        """Editing class name with small latin letter"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(self._small_latin)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test12_edit_class_name_with_small_cyrillic_NEGATIVE(self):
        """Editing class name with small cyrillic letter"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(
            self._small_cyrillic)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test13_edit_class_name_with_symbol_NEGATIVE(self):
        """Editing class name with symbol in it"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(self._symbol)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test14_edit_class_name_only_letter_NEGATIVE(self):
        """Editing class name with only one letter"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(self._one_letter)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test15_edit_class_name_many_letter_NEGATIVE(self):
        """Editing class name with many letters"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(self._many_letter)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test16_edit_class_name_without_letter_NEGATIVE(self):
        """Editing class name without letter"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(self._one_digit)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test17_edit_class_name_many_digits_NEGATIVE(self):
        """Editing class name with many digits"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(self._many_digits)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test18_edit_class_name_many_all_NEGATIVE(self):
        """Editing class name with many digits and letter"""
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(self._all_many)
        self.driver.find_element_by_name('add_button').click()
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._warning), True)

    def test19_edit_class_without_teacher_POSITIVE(self):
        """Editing class profile without teacher name"""
        self.driver.find_element_by_name('teacher').send_keys(self._no_teacher)
        self.driver.find_element_by_tag_name('h3').click()
        self.driver.find_element_by_name('add_button').click()
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_css_selector('div.group__item-holder'))
        hover.perform()
        self.driver.find_element_by_xpath(
            "//a[@href='/director/group_edit/17']").click()
        self.driver.implicitly_wait(10)
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._no_teacher), True)

    def test20_edit_class_with_teacher_POSITIVE(self):
        """Editing class profile with adding teacher name"""
        self.driver.find_element_by_name('teacher').send_keys(
            self._with_teacher)
        self.driver.find_element_by_tag_name('h3').click()
        self.driver.find_element_by_name('add_button').click()
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_css_selector('div.group__item-holder'))
        hover.perform()
        self.driver.find_element_by_xpath(
            "//a[@href='/director/group_edit/17']").click()
        self.driver.implicitly_wait(10)
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._with_teacher), True)

    def test21_edit_class_replace_teacher_POSITIVE(self):
        """Changing class teacher from dropdown list"""
        self.driver.find_element_by_name('teacher').send_keys(
            self._with_teacher2)
        self.driver.find_element_by_tag_name('h3').click()
        self.driver.find_element_by_name('add_button').click()
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_css_selector('div.group__item-holder'))
        hover.perform()
        self.driver.find_element_by_xpath(
            "//a[@href='/director/group_edit/17']").click()
        self.driver.implicitly_wait(10)
        self.assertEqual(self._check_for_element_existence(
            self.driver, self._with_teacher2), True)


if __name__ == "__main__":
    unittest.main(verbosity=1)
