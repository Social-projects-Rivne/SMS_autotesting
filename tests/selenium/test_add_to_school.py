#-*- coding: utf-8 -*-
""" 
Tests for addition teacher or director to school on Selenium WebDriver 
"""

import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from tpt import TestPrepTemplate


class TestAdditionToSchool(unittest.TestCase):

    """ 
    Class with tests for testing the addition teacher or director to school
    """

    baseurl = "http://django-smstest2.rhcloud.com/"
    baseurl_team = "http://smsautotesting-atqc.rhcloud.com/"
    baseurl_local = "http://127.0.0.1:8000/"
    username = "semuschenko"
    password = "pDk7jf"
    xpaths = {
        'inputUsername': "//input[@name='inputUsername']",
        'inputPassword': "//input[@name='inputPassword']",
        'submitButtonLogin': "button"
    }

    def setUp(self):
        """ 
        Fixture that creates all the preparations for tests 
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.baseurl_team)
        self.driver.find_element_by_xpath(self.xpaths['inputUsername']).\
                    send_keys(self.username)

        self.driver.find_element_by_xpath(self.xpaths['inputPassword']).\
                    send_keys(self.password)

        self.driver.find_element_by_tag_name(
            self.xpaths['submitButtonLogin']).click()

    def tearDown(self):
        """ 
        Fixture that deletes all the preparations for tests 
        """
        self.driver.quit()

    def test01_change_director_teacher_same_school(self):
        """ 
        Test 1 Changes role from the director to the teacher of the same
        school 
        """
        driver = self.driver
        driver.find_element_by_link_text(u'Викладачі').click()
        select_teacher1 = Select(driver.find_element_by_xpath(
                                '//*[@id="9"]/td[3]/select'))
        select_teacher1.select_by_value('3')
        select_teacher2_value = driver.find_element_by_xpath(
                                '//*[@id="10"]/td[3]/select').\
                                get_attribute("value")
        self.assertEqual(u'3', select_teacher2_value)
        driver.find_element_by_link_text(u'Навчальні заклади').click()
        select_school = Select(driver.find_element_by_xpath(
                               '//*[@id="3"]/td[3]/select'))
        self.assertEqual(select_school.first_selected_option.\
                         get_attribute('value'), '')

    def test02_change_teacher_director_same_school(self):
        """ 
        Test 2 Changes role from the teacher to the director of the same
        school 
        """
        driver = self.driver
        driver.find_element_by_link_text(u'Викладачі').click()
        select_teacher1 = Select(driver.find_element_by_xpath(
                                '//*[@id="10"]/td[3]/select'))
        select_teacher1.select_by_value('2')
        select_teacher2_value = driver.find_element_by_xpath(
                                '//*[@id="9"]/td[3]/select').\
                                get_attribute("value")
        self.assertEqual(u'3', select_teacher2_value)
        driver.find_element_by_link_text(u'Навчальні заклади').click()
        select_school = Select(driver.find_element_by_xpath(
                               '//*[@id="3"]/td[3]/select'))
        self.assertEqual(select_school.first_selected_option.text,
                         u'Григорук Олег Степанович')

    def test03_change_teacher_director_same_school_with_another_director(self):
        """ 
        Test 3 Changes role from the teacher to the director of the same
        school when there exist another director (teachers_list page) 
        """
        driver = self.driver
        driver.find_element_by_link_text(u'Викладачі').click()
        select_teacher1 = Select(driver.find_element_by_xpath(
                                '//*[@id="9"]/td[3]/select'))
        select_teacher1.select_by_value('2')
        driver.find_element_by_link_text(u'Навчальні заклади').click()
        select_school = Select(driver.find_element_by_xpath(
                              '//*[@id="3"]/td[3]/select'))
        self.assertEqual(select_school.first_selected_option.text,
                         u'Аношко Петро Микитович')

    def test04_change_teacher_director_with_another_director(self):
        """ 
        Test 4 Changes role to the director of the school when there
        exist another director (schools_list page) 
        """
        driver = self.driver
        select_school = Select(driver.find_element_by_xpath(
                              '//*[@id="5"]/td[3]/select'))
        select_school.select_by_value('11')
        driver.find_element_by_link_text(u'Викладачі').click()
        select_teacher1 = Select(driver.find_element_by_xpath(
                                '//*[@id="12"]/td[3]/select'))
        self.assertEqual(select_teacher1.first_selected_option.\
                         get_attribute('value'), u'3')
        select_teacher2 = Select(driver.find_element_by_xpath(
                                '//*[@id="11"]/td[3]/select'))
        self.assertEqual(select_teacher2.first_selected_option.\
                         get_attribute('value'), u'2')

    def test05_add_teacher_school_was_not_connected(self):
        """ 
        Test 5 Add the teacher to school when he wasn't connected to any
        school 
        """
        driver = self.driver
        driver.find_element_by_link_text(u'Викладачі').click()
        select_teacher = Select(driver.find_element_by_xpath(
                               '//*[@id="7"]/td[4]/select'))
        select_teacher.select_by_value('1')
        driver.find_element_by_link_text(u'Навчальні заклади').click()
        select_school = Select(driver.find_element_by_xpath(
                        '//*[@id="1"]/td[3]/select'))
        #print [option.text for option in select_school.options]
        self.assertIn(u'Панасюк Ігор Микитович',
                     [option.text for option in select_school.options])

    def test06_change_school_when_director_in_another(self):
        """ 
        Test 6 Change school when he was the director in another 
        """
        driver = self.driver
        driver.find_element_by_link_text(u'Викладачі').click()
        select_teacher = Select(driver.find_element_by_xpath(
                                '//*[@id="6"]/td[3]/select'))
        self.assertEqual(select_teacher.first_selected_option.\
                        get_attribute('value'), u'2')
        Select(driver.find_element_by_xpath('//*[@id="6"]/td[4]/select')).\
                                            select_by_value('5')
        driver.find_element_by_link_text(u'Навчальні заклади').click()
        select_school = Select(driver.find_element_by_xpath(
                              '//*[@id="5"]/td[3]/select'))
        self.assertIn(u'Охріменко Василь Георгійович',
                     [option.text for option in select_school.options])

    def test07_change_director_to_absent(self):
        """ 
        Test 7 Change role from the director to Відсутній 
        """
        driver = self.driver
        select_school = Select(driver.find_element_by_xpath(
                              '//*[@id="4"]/td[3]/select'))
        select_school.select_by_value('')
        driver.find_element_by_link_text(u'Викладачі').click()
        select_teacher = Select(driver.find_element_by_xpath(
                               '//*[@id="13"]/td[3]/select'))
        self.assertEqual(select_teacher.first_selected_option.\
                         get_attribute('value'), u'3')

    def test08_create_teacher_add_form(self):
        """ 
        Test 8 Create the teacher to school using add form 
        """
        driver = self.driver
        driver.find_element_by_link_text(u'Викладачі').click()
        driver.find_element_by_xpath(
               '//*[@id="list"]/table/thead/tr/th[5]/a').click()
        WebDriverWait(driver, 10).until(lambda driver: driver.\
                      find_element_by_id('inputName'))
        driver.find_element_by_id('inputName').\
                                 send_keys(u'Ковальчук Остап Казимирович')
        driver.find_element_by_id('inputEmail').send_keys(u'koval@orbit.com')
        driver.find_element_by_id('inputLogin').send_keys(u'koval')
        Select(driver.find_element_by_id('selectSchool')).select_by_value('2')
        driver.find_element_by_xpath(
              'html/body/div[3]/div/div/form/div[5]/button').click()
        driver.find_element_by_link_text(u'Навчальні заклади').click()
        select_school = Select(driver.find_element_by_xpath(
                              '//*[@id="2"]/td[3]/select'))
        self.assertIn(u'Ковальчук Остап Казимирович',
                     [option.text for option in select_school.options])

    def test09_change_school_for_teacher_in_another(self):
        """ 
        Test 9 Change school when he was the teacher in another 
        """
        driver = self.driver
        driver.find_element_by_link_text(u'Викладачі').click()
        select_teacher = Select(driver.find_element_by_xpath(
                               '//*[@id="16"]/td[3]/select'))
        self.assertEqual(select_teacher.first_selected_option.\
                        get_attribute('value'), u'3')
        Select(driver.find_element_by_xpath('//*[@id="16"]/td[4]/select')).\
                                            select_by_value('3')
        driver.find_element_by_link_text(u'Навчальні заклади').click()
        select_school = Select(driver.find_element_by_xpath(
                              '//*[@id="3"]/td[3]/select'))
        self.assertIn(u'Левицька Тамара Сергіївна',
                     [option.text for option in select_school.options])


if __name__ == "__main__":
    TestPrepTemplate.prepare_db()
    try:
        unittest.main(verbosity=2)
    finally:
        TestPrepTemplate.prepare_db(action='tearDown')
