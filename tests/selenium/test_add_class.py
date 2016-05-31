# -*- coding: utf-8 -*-
""" Tests for class addition on Selenium WebDriver """


import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from tpt import TestPrepTemplate


class TestPreparations(unittest.TestCase):
    """ Superclass with preparations for tests and initial data """

    _baseurl = "http://django-smstest2.rhcloud.com/"
    _baseurl_team = "http://smsautotesting-atqc.rhcloud.com/"
    _baseurl_local = "http://127.0.0.1:8000/"
    _username = "zoshch"
    _password = "df5sFdf"

    _xpaths = {
        'inputUsername': "//input[@name='inputUsername']",
        'inputPassword': "//input[@name='inputPassword']",
        'submitButtonLogin': "button"
    }

    def setUp(self):
        """ Fixture that creates a initial data and records for tests,
        initial test steps
        """

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self._baseurl_team)
        self.driver.find_element_by_xpath(self._xpaths['inputUsername']).\
                    send_keys(self._username)

        self.driver.find_element_by_xpath(self._xpaths['inputPassword']).\
                    send_keys(self._password)

        self.driver.find_element_by_tag_name(
            self._xpaths['submitButtonLogin']).click()


    def tearDown(self):
        """ Fixture that deletes all preparation for tests """

        self.driver.quit()


class ClassAddition(TestPreparations):

    """ Class with methods for testing class addition"""

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        super(ClassAddition, self).setUp()

    def negative_test(self, form_id, form_number):
        driver = self.driver
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[" + str(form_id) +\
                 "]/a").click()
        driver.find_element_by_xpath("//*[@id=" + str(form_id) + "]/a").click()
        self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
        class_name = driver.find_element_by_id("inputName")
        class_name.clear()
        class_name.send_keys(form_number)
        driver.find_element_by_id("add_button").click()
        self.assertTrue("Некоректно введено назву", driver.\
                       find_element_by_xpath(
                        "//span[contains(.,'Некоректно введено назву')]"))

    def test01_profile_is_opened(self):
        """ Test 1 Checks that profile is opened """
        driver = self.driver
        self.assertIn("/director/group_list/", driver.current_url)

    def test02_information_of_logged_user(self):
        """ Test 2 Checks that profile contains information of logged user """
        driver = self.driver
        self.assertTrue("Завуч", driver.find_element_by_xpath(
                        "//h5[contains(.,'Завуч')]"))
        self.assertTrue("Зощенко Іван Вікторович", driver.\
                       find_element_by_xpath(
                        "//p[contains(.,'Зощенко Іван Вікторович')]"))

    def test03_classes_navigation_tabs(self):
        """ Test 3 Checks that profile has class navigation tabs for each
        class """
        driver = self.driver
        for index in range(1, 12):
            self.assertTrue(str(index) + "класи", driver.find_element_by_xpath(
                            "html/body/div[2]/div/div[2]/div/div/ul/li[" + \
                            str(index) + "]/a").text)

    def test04_links_for_class_addition(self):
        """ Test 4 Checks that profile contains links for adding any class """
        driver = self.driver
        for index in range(1, 12):
            self.assertTrue("+", driver.\
                            find_element_by_xpath(
                            "//*[@id=" + str(index) + "]/a"))

    def test05_class_addition_frame_is_opened(self):
        """ Test 5 Checks that clicking on the link to add class opens the
        frame for class addition"""
        driver = self.driver
        for index in range(1, 12):
            driver.find_element_by_link_text(str(index) + " класи").click()
            driver.find_element_by_xpath("//*[@id=" + str(index) + "]/a").\
                                         click()
            self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
            driver.find_element_by_link_text("Відмінити").click()

    def test06_classes_grades_are_visible(self):
        """ Test 6 Checks if all the classes grades are visible """
        driver = self.driver
        for index in range(1, 12):
            self.assertTrue(str(index) + " класи", driver.\
                            find_element_by_xpath(
                            "html/body/div[2]/div/div[2]/div/div/ul/li[" + \
                            str(index) + "]/a").text)

    def test07_class_valid_name_is_added(self):
        """ Test 7 Checks if class with valid name is added """
        driver = self.driver
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[7]/a").click()
        driver.find_element_by_xpath("//*[@id='7']/a").click()
        self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
        class_name = driver.find_element_by_id("inputName")
        class_name.clear()
        class_name.send_keys(u"7А")
        driver.find_element_by_id("add_button").click()
        driver.find_element_by_xpath(
            "html/body/div[2]/div/div[2]/div/div/ul/li[7]/a").click()
        self.assertTrue("7А клас", driver.find_element_by_link_text(
                        "7А клас"))

    def test08_empty_class_name(self):
        """ Test 8 Checks class addition with empty name """
        driver = self.driver
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[6]/a").click()
        driver.find_element_by_xpath("//*[@id='6']/a").click()
        self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
        class_name = driver.find_element_by_id("inputName")
        class_name.clear()
        driver.find_element_by_id("add_button").click()
        self.assertTrue("Некоректно введено назву", driver.\
                       find_element_by_xpath(
                        "//span[contains(.,'Некоректно введено назву')]"))

    def test09_class_with_latin_letter(self):
        """ Test 9 Checks class addition with latin letter """
        self.negative_test(6, u"6A")

    def test10_class_with_small_letter(self):
        """ Test 10 Checks class addition with small letter """
        self.negative_test(6, u"6а")

    def test11_class_with_small_latin_letter(self):
        """ Test 11 Checks class addition with small latin letter """
        self.negative_test(6, u"6a")

    def test12_class_with_several_capital_letters(self):
        """ Test 12 Checks class addition with several capital letters """
        self.negative_test(6, u"6АБВ")

    def test13_class_with_several_small_letters(self):
        """ Test 13 Checks class addition with several small letters """
        self.negative_test(6, u"6абв")

    def test14_class_without_letters(self):
        """ Test 14 Checks class addition without letters """
        self.negative_test(6, u"6")

    def test15_class_with_numbers_letter(self):
        """ Test 15 Checks class addition with several numbers and letter """
        self.negative_test(6, u"631А")

    def test16_class_without_numbers(self):
        """ Test 16 Checks class addition without numbers """
        self.negative_test(6, u"А")

    def test17_class_with_space(self):
        """ Test 17 Checks class addition with space """
        self.negative_test(6, u"6 А")

    def test18_class_with_down_underline(self):
        """ Test 18 Checks class addition with down underline """
        self.negative_test(6, u"6_А")

    def test19_class_with_outer_spaces(self):
        """ Test 19 Checks class addition with correct name but with outer
        spaces """
        self.negative_test(6, u" 6А ")

    def test20_class_with_special_symbols(self):
        """ Test 20 Checks class addition with special symbols """
        special_symbols = ["=", "/", "\\", "|", "*", "(", ")", "-", ":", ";",\
                           "#", "%", "^", "?", "!", "[", "]"]
        driver = self.driver
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[6]/a").click()
        driver.find_element_by_xpath("//*[@id='6']/a").click()
        self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
        class_name = driver.find_element_by_id("inputName")
        for elem in special_symbols:
            class_name.clear()
            class_name.send_keys(u"6" + elem + u"А")
            driver.find_element_by_id("add_button").click()
            self.assertTrue("Некоректно введено назву", driver.\
                           find_element_by_xpath(
                           "//span[contains(.,'Некоректно введено назву')]"))


    def test21_class_with_latin_numbers(self):
        """ Test 21 Checks class addition with latin numbers """
        self.negative_test(11, u"IIА")

    def test22_class_with_inversed_letter_number(self):
        """ Test 22 Checks class addition with inversed letter and number """
        self.negative_test(2, u"А2")

    def test23_class_with_existed_name(self):
        """ Test 23 Checks class addition with already existed name """
        driver = self.driver
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[8]/a").click()
        driver.find_element_by_xpath("//*[@id='8']/a").click()
        self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
        class_name = driver.find_element_by_id("inputName")
        class_name.clear()
        class_name.send_keys(u"8А")
        driver.find_element_by_id("add_button").click()

        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[8]/a").click()
        driver.find_element_by_xpath("//*[@id='8']/a").click()
        self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
        class_name = driver.find_element_by_id("inputName")
        class_name.clear()
        class_name.send_keys(u"8А")
        driver.find_element_by_id("add_button").click()
        self.assertTrue("Клас з такою назвою вже існує.", driver.\
                        find_element_by_xpath(
                        "//span[contains(.,'Клас з такою назвою вже існує')]"))


    def test24_class_addition_on_another_tab(self):
        """ Test 24 Checks class addition when 9th class is added using the
        11 class tab """
        driver = self.driver
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[11]/a").click()
        driver.find_element_by_xpath("//*[@id='11']/a").click()
        self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
        class_name = driver.find_element_by_id("inputName")
        class_name.clear()
        class_name.send_keys(u"9А")
        driver.find_element_by_id("add_button").click()
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[9]/a").click()
        self.assertTrue(u"9А клас", driver.\
                       find_element_by_xpath("//a[contains(.,'9А клас')]"))
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[11]/a").click()
        #self.assertFalse(u"9А клас", driver.\
                       #find_element_by_xpath("//a[contains(.,'9А клас')]"))

    def test25_class_with_correct_name_supervisor(self):
        """ Test 25 Checks class addition with correct name and supervisor
        teacher """
        driver = self.driver
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[5]/a").click()
        driver.find_element_by_xpath("//*[@id='5']/a").click()
        self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
        class_name = driver.find_element_by_id("inputName")
        class_name.clear()
        class_name.send_keys(u"5Ґ")
        Select(driver.find_element_by_id("selectTeacher")).select_by_value('2')
        driver.find_element_by_id("add_button").click()
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[5]/a").click()
        self.assertTrue("5Ґ клас", driver.\
                       find_element_by_xpath("//div[contains(.,'5Ґ клас')]"))
        driver.find_element_by_xpath("//*[@id='5']/a").click()
        select = Select(driver.find_element_by_id("selectTeacher"))
        self.assertNotIn(u'Галицький Максим Геннадійович',
                        [option.text for option in select.options])


    def test26_class_with_correct_name_different_supervisors(self):
        """ Test 26 Checks class addition with same class name and different
        supervisors """
        driver = self.driver
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[4]/a").click()
        driver.find_element_by_xpath("//*[@id='4']/a").click()
        self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
        class_name = driver.find_element_by_id("inputName")
        class_name.clear()
        class_name.send_keys(u"4Р")
        #Select(driver.find_element_by_id("selectTeacher")).select_by_value('2')
        driver.find_element_by_id("add_button").click()
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[4]/a").click()
        self.assertTrue("5Ґ клас", driver.\
                       find_element_by_xpath("//div[contains(.,'4Р клас')]"))
        driver.find_element_by_xpath("//*[@id='4']/a").click()
        class_name = driver.find_element_by_id("inputName")
        class_name.clear()
        class_name.send_keys(u"4Р")
        self.assertTrue(u'Клас з такою назвою вже існує', driver.\
                       find_element_by_xpath(
                        "//span[contains(.,'Клас з такою назвою вже існує')]"))

    def test27_frame_contains_fields_buttons(self):
        """ Test 27 Checks if the frame to add class contains fields and
        buttons """
        driver = self.driver
        driver.find_element_by_xpath(
                "html/body/div[2]/div/div[2]/div/div/ul/li[7]/a").click()
        driver.find_element_by_xpath("//*[@id='7']/a").click()
        self.assertTrue("Додати клас", driver.find_element_by_xpath(
                            "//h3[contains(.,'Додати клас')]"))
        driver.find_element_by_id("inputName")
        driver.find_element_by_id("selectTeacher")
        self.assertTrue("Прийняти", driver.find_element_by_id("add_button").\
                        text)
        self.assertTrue("Відмінити", driver.find_element_by_xpath(
                            "html/body/div[3]/div/div/form/div[3]/a").text)


    def tearDown(self):
        """ Fixture that deletes all preparation for tests and restores
        original data
        """
        super(ClassAddition, self).tearDown()

if __name__ == "__main__":
    TestPrepTemplate.prepare_db()
    try:
        unittest.main(verbosity=2)
    finally:
        print(TestPrepTemplate.prepare_db(action='tearDown'))



