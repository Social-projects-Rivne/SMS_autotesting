# -*- coding: utf-8 -*-
"""
Tests on Selenium WebDriver of an ability to add subject and class for teacher
"""

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class AddSubjectClassForTeacherTests(unittest.TestCase):
    """
    Class with methods for testing an ability
    to add subject and class for teacher
    """

    base_url = "https://smsauto-dvatqc.rhcloud.com"
    username = "zoshch"
    password = "df5sFdf"
    xpaths = {
        'inputUsername': "//input[@name='inputUsername']",
        'inputPassword': "//input[@name='inputPassword']",
        'submitButtonLogin': "button",
    }
    warnings = {
        "alreadyExistsSubject": u"Даний викладач вже веде вибраний предмет.",
        "thisIsRequiredField": u"Це обов'язкове поле.",
        "alreadyStudyingSubjectForClass": u"Викладач вже веде даний предмет в цьому класі."
    }

    def check_for_element_existence(self, driver, element):
        """ Function to check whether element exists on the web-page """

        self.page_content = driver.page_source
        if element in self.page_content:
            element_exists = True
        else:
            element_exists = False
        return element_exists

    def setUp(self):
        """ Fixture that creates all the preparations for tests """

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.accept_next_alert = True
        self.driver.get(self.base_url)
        self.driver.find_element_by_xpath(
            self.xpaths['inputUsername']).send_keys(
            self.username)

        self.driver.find_element_by_xpath(
            self.xpaths['inputPassword']).send_keys(
            self.password)

        self.driver.find_element_by_tag_name(
            self.xpaths['submitButtonLogin']).click()

    def tearDown(self):
        """ Fixture that deletes all the preparations for tests """

        self.driver.close()

    # def test01_ui_to_add_subject_exist(self):
    #     """
    #     Check whether pop-up windows shows onclick the button “Add subject”
    #     """
    #
    #     self.driver.find_element_by_link_text(u"Керування предметами").click()
    #     self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/table/tbody/tr[2]/td/a").click()
    #     self.assertEqual(
    #         self.check_for_element_existence(
    #             self.driver,
    #             self.driver.find_element_by_tag_name("h3").text), True)
    #
    # def test02_add_subject_for_teacher_positive(self):
    #     """  Check whether subject can be added for teacher """
    #
    #     self.driver.find_element_by_link_text(u"Керування предметами").click()
    #     self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/table/tbody/tr[2]/td/a").click()
    #     select = Select(self.driver.find_element_by_xpath(
    #         "//*[@id='manage_teachers_select']"))
    #     select.select_by_value('9')
    #     self.driver.find_element_by_xpath("//*[@id='add_button']").click()
    #     self.assertEqual(self.check_for_element_existence(self.driver,
    #                                                       u"Зарубіжна література"),
    #                      True)

    # def test03_add_already_exist_subject_for_teacher_negative(self):
    #     """
    #     Check whether warning message exists
    #     while add already exist subject for teacher
    #     """
    #     self.driver.find_element_by_link_text(u"Керування предметами").click()
    #     self.driver.find_element_by_xpath(
    #         "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr[3]/td/a"). \
    #         click()
    #     select = Select(self.driver.find_element_by_xpath(
    #         "//*[@id='manage_teachers_select']"))
    #     select.select_by_value('9')
    #     self.driver.find_element_by_xpath("//*[@id='add_button']").click()
    #     self.assertEqual(
    #         self.check_for_element_existence(self.driver,
    #                                          self.warnings[
    #                                              "alreadyExistsSubject"]),
    #         True)

    # def test04_insert_empty_value_for_subject_negative(self):
    #     """ Check whether warning message exist while subject not chosen """
    #
    #     self.driver.find_element_by_link_text(u"Керування предметами").click()
    #     self.driver.find_element_by_xpath(
    #         "/html/body/div[2]/div/div[2]/div/div/table/tbody/tr[8]/td/a"). \
    #         click()
    #     self.driver.find_element_by_xpath("//*[@id='add_button']").click()
    #     self.assertEqual(self.check_for_element_existence(self.driver,
    #                                                       self.warnings[
    #                                                           "thisIsRequiredField"]),
    #                      True)
    #
    # def test05_ui_to_add_class(self):
    #     """
    #     Check whether pop-up windows shows onclick the button “Add class”
    #     """
    #
    #     self.driver.find_element_by_link_text(u"Керування предметами").click()
    #     self.driver.find_element_by_xpath("//*[@id='2']/td[2]/a").click()
    #
    #     self.assertIsNotNone(self.driver.find_element_by_tag_name("select"))
    #
    # def test06_add_class_for_teacher_positive(self):
    #     """ Check whether school class can be added for teacher """
    #
    #     self.driver.find_element_by_link_text(u"Керування предметами").click()
    #     self.driver.find_element_by_xpath("//*[@id='8']/td[4]/a").click()
    #     select = Select(self.driver.find_element_by_xpath(
    #         "//*[@id='manage_teachers_select']"))
    #     select.select_by_value('17')
    #     self.driver.find_element_by_xpath("//*[@id='add_button']").click()
    #     self.assertEqual(self.check_for_element_existence(self.driver, u"1А"),
    #                      True)
    # def test07_add_second_class_for_teacher_positive(self):
    #     """
    #     Check whether second school class can be added for the same teacher
    #     """
    #
    #     self.driver.find_element_by_link_text(u"Керування предметами").click()
    #     self.driver.find_element_by_xpath("//*[@id='8']/td[4]/a").click()
    #     select = Select(self.driver.find_element_by_xpath(
    #         "//*[@id='manage_teachers_select']"))
    #     select.select_by_value('18')
    #     self.driver.find_element_by_xpath("//*[@id='add_button']").click()
    #     self.assertEqual(self.check_for_element_existence(self.driver, u"1Б"),
    #                      True)
    def test08_add_already_exists_class_for_subject_negative(self):
        """ Check whether warning message exists
        while add already exists class for subject
        """

        self.driver.find_element_by_link_text(u"Керування предметами").click()
        self.driver.find_element_by_xpath("//*[@id='8']/td[4]/a").click()
        select = Select(self.driver.find_element_by_xpath(
            "//*[@id='manage_teachers_select']"))
        select.select_by_value('17')
        self.driver.find_element_by_tag_name('h3').click()
        self.assertEqual(self.check_for_element_existence(self.driver,
                                                          self.warnings[
                                                              "alreadyStudyingSubjectForClass"]),
                         True)
    def test09_delete_subject_positive(self):
        """ Check whether subject can be deleted """

        


if __name__ == "__main__":
    unittest.main(verbosity=2)
