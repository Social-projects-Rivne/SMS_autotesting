# -*- coding: utf-8 -*-
"""  _  """


import unittest
from selenium import webdriver


class TestPreparations(unittest.TestCase):
    """ Superclass with preparations for tests and initial data """

    _url = "http://sms-rv016atqc.rhcloud.com"
    _login = "yulia"
    _password = "Lhkj4Gh"

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


    def tearDown(self):
        """ Fixture that deletes all preparation for tests """

        self.driver.quit()


class ViewClassesAsATeacher(TestPreparations):
    """ Class with methods for testing """

    _subjects = ["Українська мова",
                 "Українська література"]

    _classes_literature = ["9Б клас",
                           "9A клас"]

    _classes_language = ["8А клас",
                         "8Б клас",
                         "8В клас",
                         "8В клас",
                         "9A клас"]

    _students8A = ["Кулаковський Іван Орестович",
                   "Обліпиха Володимир Володимирович",
                   "Панасюк Ігор Олександрович",
                   "Петрук Тамара Миколаївна",
                   "Порох Євген Леонідович",
                   "Савчук Олена Петрівна",
                   "Сорока Ірина Ігорівна",
                   "Степанюк Володимир Григорович",
                   "Щеба Андрій Назарович"]

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        super(ViewClassesAsATeacher, self).setUp()

    def test01_smoke_test(self):
        """ 01. Check, that the page to view classes opened """

        driver = self.driver
        self.assertIn("teacher/subject_group_list", driver.current_url)

    def test02_page_contains_subjects(self):
        """ 02. Check, that the tabs for subjects exists and shown """

        driver = self.driver

        for subj in self._subjects:
            self.assertTrue(len(driver.find_elements_by_link_text(
                subj.decode("utf-8"))) == 1)

    def test03_subject_page_contains_classes(self):
        """ 03. Check, that the appropriate classes is present
        on the subjects pages
        """

        driver = self.driver

        driver.find_element_by_xpath(
            "//a[contains(.,'Українська література')]").click()

        for cls in self._classes_literature:
            self.assertTrue(len(driver.find_elements_by_link_text(
                cls.decode("utf-8"))) == 1)

        driver.find_element_by_xpath(
            "//a[contains(.,'Українська мова')]").click()

        for cls in self._classes_language:
            self.assertTrue(len(driver.find_elements_by_link_text(
                cls.decode("utf-8"))) == 1)

    def test04_class_page_opened(self):
        """ 04. Check, that the page for class opened """

        driver = self.driver

        driver.find_element_by_link_text(
            "8А клас".decode("utf-8")).click()

        self.assertIn("class_journal", driver.current_url)
        self.assertIn("Класс: 8А Предмет:".decode("utf-8"),
                      driver.find_element_by_xpath(
                          "//h5[contains(.,'Класс: 8А Предмет:')]".decode(
                              "utf-8")).text)
        self.assertIn("Українська мова".decode("utf-8"),
                      driver.find_element_by_xpath(
                          "//select[@onchange='location = "
                          "this.options[this.selectedIndex].value;']").text)

    def test05_class_page_contains_students(self):
        """ 05. Check, that the list of students contains full
        and exact list for students in the class
        """

        driver = self.driver

        driver.find_element_by_link_text("8А клас".decode("utf-8")).click()

        for student in self._students8A:
            self.assertTrue(len(
                driver.find_elements_by_xpath(
                    "//td[contains(.,'{}')]".format(student))) > 0)

    def tearDown(self):
        """ Fixture that deletes all preparation for tests and restores
        original data
        """

        super(ViewClassesAsATeacher, self).tearDown()

if __name__ == "__main__":
    unittest.main(verbosity=2)


