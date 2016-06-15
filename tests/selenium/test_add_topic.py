# -*- coding: utf-8 -*-
""" 
Tests for lesson addition on Selenium WebDriver 
"""


import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from tpt import TestPrepTemplate


class TestPreparations(unittest.TestCase):

    """ 
    Superclass with preparations for tests and initial data 
    """

    baseurl = "http://django-smstest2.rhcloud.com/"
    baseurl_team = "http://smsautotesting-atqc.rhcloud.com/"
    baseurl_local = "http://127.0.0.1:8000/"
    username = "yulia"
    password = "Lhkj4Gh"

    xpaths = {
        'inputUsername': "//input[@name='inputUsername']",
        'inputPassword': "//input[@name='inputPassword']",
        'submitButtonLogin': "button"
    }

    def setUp(self):
        """ 
        Fixture that creates an initial data and records for tests 
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
        Fixture that deletes all preparation for tests 
        """
        self.driver.quit()


class LessonAddition(TestPreparations):

    """ 
    Class with methods for testing lesson addition
    """

    lesson_number = 2
    topic_max = u"проа"*51
    topic_min = u"a"
    topic_spaces = u"     "
    topic_numbers = u"1234567"
    topic_latin = u"Hello world!"
    topic_capital_letters = u"ОУН-УПА"
    topic_small_letters = u"small letter topic"
    topic_special_symbols = u"= | * ( ) - : ; # % ^ ? ! [ ]"
    topic_letters_numbers = u"Національно-визвольна війна українського народу \
                            1647-1654 рр."
    topic_outer_spaces = u"   Hello world!   "
    topic_key_sensitive = u"War AnD PeACe - tHe twO wOrDS are KnoWN To eveRyoNe"
    topic_html = u"<button class='btn btn-success' name='add_button' \
                 type='submit'>Прийняти</button>"
    topic_javascript = u"<script>alert('Hello, world!')</alert>, <script>" + \
                       u"document.getElementByID('…').disabled=true</script>"
    topic_sql = u"DROP TABLE teachers; SELECT * FROM teachers;"
    topic_symbols_code = u"\\x27\\xu201C\\xu2663\\xu263A\\xu2642\\xu201D\\x20" \
                         + u"\\xu201C\\xu201D\\xu2018\\x7E\\x21\\x23\\x24\\x25"

    hometask1 = u"параграф 34 переказувати"
    hometask2 = u"ReaD AnD trAnSlaTe tHe TeXT"
    hometask3 = u"<a class='modal-dialog link' \
                href='/teacher/class_journal_add_lesson/13'>+ Add</a>"
    hometask4 = u"<script>alert(“Hello, world!”)</alert>, <script>document.\
                getElementByID(“…”).disabled=true</script"
    hometask5 = u"\\x20\\x20\\x20\\x20\\x20\\x20\\x20\\x20\\x20\\x20\\x20\\x20"

    def setUp(self):
        """ 
        Fixture that creates a initial data and records for tests 
        """
        super(LessonAddition, self).setUp()

    def fill_in_lesson_add_form(self, class_link, lesson_link, topic, hometask):
        """ 
        Function for filling in the textfields on the lesson add form 
        """
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='1']/a[" + str(class_link) \
                                    + "]").click()
        self.assertTrue(u"Класс:", driver.find_element_by_xpath(
                        "//h5[contains(.,'Класс:')]"))
        driver.find_element_by_xpath(
               "html/body/div[2]/div/div[2]/div/div/table[2]/thead/tr/th[" + \
               str(lesson_link) + "]/a").click()
        self.assertTrue(u"Додати урок", driver.find_element_by_xpath(
                        "//h3[contains(.,'Додати урок')]"))
        input_topic = driver.find_element_by_id("inputTopic")
        input_topic.clear()
        input_topic.send_keys(topic)
        input_hometask = driver.find_element_by_id("inputHomework")
        input_hometask.clear()
        input_hometask.send_keys(hometask)
        driver.find_element_by_name('add_button').click()

    def check_correct_lesson_addition(self, class_name, lesson_link, topic, hometask):
        """ 
        Function for checking values of the textfields after the lesson was added
        """
        driver = self.driver
        #self.assertTrue(u"Класс: " + str(class_name).decode('utf-8'), 
        #               driver.find_element_by_xpath(
        #               "//h5[contains(.,'Класс: " + str(class_name).decode('utf-8') + " ')]"))
        driver.find_element_by_xpath(
               "html/body/div[2]/div/div[2]/div/div/table[2]/thead/tr/th[" + \
               str(lesson_link) + "]/a").click()
        self.assertTrue(u"Редагувати урок", driver.find_element_by_xpath(
                        "//h3[contains(.,'Редагувати урок')]"))
        self.assertTrue(topic, driver.find_element_by_id('inputTopic').text)
        self.assertTrue(hometask, driver.find_element_by_id('inputHomework').\
                        text)

    def fill_in_date(self, class_link, class_name, lesson_link, date_value):
        """ 
        Function for fill in date values on the lesson add form 
        """
        driver = self.driver
        driver.find_element_by_xpath(
               "html/body/div[2]/div/div[2]/div/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='2']/a[" + str(class_link) + "]").\
                                     click()
        self.assertTrue(u"Класс: ", driver.find_element_by_xpath(
                        "//h5[contains(.,'Класс: ')]"))
        driver.find_element_by_xpath(
               "html/body/div[2]/div/div[2]/div/div/table[2]/thead/tr/th[" + \
                str(lesson_link) + "]/a").click()
        self.assertTrue(u"Додати урок", driver.find_element_by_xpath(
                        "//h3[contains(.,'Додати урок')]"))
        input_data = driver.find_element_by_id("date")
        input_data.clear()
        input_data.send_keys(date_value)
        input_topic = driver.find_element_by_id("inputTopic")
        input_topic.clear()
        input_topic.send_keys(u"Eurovision Song Contest 2016")
        input_hometask = driver.find_element_by_id("inputHomework")
        input_hometask.clear()
        input_hometask.send_keys(u"Watch Online")
        driver.find_element_by_name('add_button').click()

    def check_correct_date_addition(self, class_name, lesson_link, date_value):
        """ 
        Function for checking of date existance after lesson addition 
        """
        driver = self.driver
        self.assertTrue(u"Класс: ", driver.find_element_by_xpath(
                        "//h5[contains(.,'Класс: ')]"))
        self.assertTrue(str(date_value), driver.find_element_by_xpath(
                        "html/body/div[2]/div/div[2]/div/div/table[2]/thead/tr/th[" \
                        + str(lesson_link) + "]/a").text)

    def test01_profile_is_opened(self):
        """ 
        Test 1 Checks that teachers profile is opened 
        """
        driver = self.driver
        self.assertIn("/teacher/subject_group_list", driver.current_url)

    def test02_information_of_logged_user(self):
        """ 
        Test 2 Checks that teachers profile contains information about 
        logged user 
        """
        driver = self.driver
        self.assertTrue("Викладач", driver.find_element_by_xpath(
                        "//h5[contains(.,'Викладач')]"))
        self.assertTrue("Бондаренко Юлія Олександрівна", driver.\
                       find_element_by_xpath(
                        "//p[contains(.,'Бондаренко Юлія Олександрівна')]"))

    def test03_profile_contains_subjects_and_classes(self):
        """ 
        Test 3 Checks that teachers profile contains subjects and classes 
        """
        driver = self.driver
        self.assertTrue("Українська мова", driver.find_element_by_xpath(
                        "//a[contains(.,'Українська мова')]")) 
        self.assertTrue("Українська література", driver.find_element_by_xpath(
                        "//a[contains(.,'Українська література')]")) 
        self.assertTrue("8А клас", driver.find_element_by_xpath(
                        "//a[contains(.,'8А клас')]")) 
        self.assertTrue("8Б клас", driver.find_element_by_xpath(
                        "//a[contains(.,'8Б клас')]")) 
        self.assertTrue("8В клас", driver.find_element_by_xpath(
                        "//a[contains(.,'8В клас')]")) 

    def test04_class_contains_students(self):
        """ 
        Test 4 Checks that class contains students 
        """
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='1']/a[1]").click()
        self.assertTrue("Савчук Олена Петрівна", driver.find_element_by_xpath(
                        "//td[contains(.,'Савчук Олена Петрівна')]"))
        self.assertTrue("Щеба Андрій Назарович", driver.find_element_by_xpath(
                        "//td[contains(.,'Щеба Андрій Назарович')]")) 

    def test05_frame_for_addition_opened(self):
        """ 
        Test 5 Checks that frame for lesson addition is opened 
        """
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='1']/a[1]").click()
        self.assertTrue("Класс: 8А", driver.find_element_by_xpath(
                        "//h5[contains(.,'Класс: 8А')]"))
        driver.find_element_by_xpath(
               "html/body/div[2]/div/div[2]/div/div/table[2]/thead/tr/th[9]/a"
                ).click()
        self.assertTrue("Додати урок", driver.find_element_by_xpath(
                        "//h3[contains(.,'Додати урок')]"))

    def test06_lesson_addition_link_exists(self):
        """ 
        Test 6 Checks if the link for lesson addition exists 
        """
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='1']/a[1]").click()
        self.assertTrue("+ Add", driver.find_element_by_xpath(
                        "//a[contains(.,'+ Add')]"))

    def test07_frame_contains_buttons_fields(self):
        """ 
        Test 7 Checks if the frame contains buttons and fields 
        """
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='1']/a[1]").click()
        self.assertTrue("Класс: 8А", driver.find_element_by_xpath(
                        "//h5[contains(.,'Класс: 8А')]"))
        #window_before = driver.window_handles[0]
        #print window_before
        
        driver.find_element_by_xpath(
               "html/body/div[2]/div/div[2]/div/div/table[2]/thead/tr/th[9]/a"
                ).click()
        #alert = driver.switch_to_alert()
        #elements_ids = driver.find_elements_by_name('*')
        #print elements_ids
        #for elem in elements_ids:
        #    print elem
        self.assertTrue('date', driver.find_elements_by_id('date'))
        self.assertTrue('selectDir', driver.find_elements_by_id('selectDir'))
        self.assertTrue('inputTopic', driver.find_elements_by_id('inputTopic'))
        self.assertTrue('inputHomework', driver.find_elements_by_id('inputHomework'))
        self.assertTrue('add_button', driver.find_element_by_name('add_button'))

    def test08_lesson_addition_empty_fields(self):
        """ 
        Test 8 Checks lesson addition with empty fields 
        """
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='1']/a[1]").click()
        self.assertTrue("Класс: 8А", driver.find_element_by_xpath(
                        "//h5[contains(.,'Класс: 8А')]"))
        driver.find_element_by_xpath(
               "html/body/div[2]/div/div[2]/div/div/table[2]/thead/tr/th[9]/a"
                ).click()
        self.assertTrue("Додати урок", driver.find_element_by_xpath(
                        "//h3[contains(.,'Додати урок')]"))
        driver.find_element_by_id('inputTopic').clear()
        driver.find_element_by_id('inputHomework').clear()
        driver.find_element_by_id('date').clear()
        driver.find_element_by_name('add_button').click()
        self.assertTrue("Додати урок", driver.find_element_by_xpath(
                        "//h3[contains(.,'Додати урок')]"))

    def test09_lesson_addition_max_plus_one_symbols(self):
        """ 
        Test 9 Checks lesson addition with max+1 symbols length 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number, self.topic_max, 
                                     self.topic_max)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number, 
                                           self.topic_max, self.topic_max)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test10_lesson_addition_min_symbol(self):
        """ 
        Test 10 Checks lesson addition with min symbols length 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+1, self.topic_min, 
                                     self.topic_min)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+1, 
                                           self.topic_min, self.topic_min)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test11_lesson_addition_only_with_spaces(self):
        """ 
        Test 11 Checks lesson addition only with spaces 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+2, self.topic_spaces, 
                                     self.topic_spaces)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+2, 
                                           self.topic_spaces, self.topic_spaces)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test12_lesson_addition_only_with_numbers(self):
        """ 
        Test 12 Checks lesson addition with only numbers 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+3, self.topic_numbers, 
                                     self.topic_numbers)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+3, 
                                           self.topic_numbers, self.topic_numbers)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test13_lesson_addition_with_latin_letters(self):
        """ 
        Test 13 Checks lesson addition with latin letters 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+4, self.topic_latin, 
                                     self.topic_latin)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+4, 
                                           self.topic_latin, self.topic_latin)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test14_lesson_addition_only_with_capital_letters(self):
        """ 
        Test 14 Checks lesson addition with capital letters 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+5, 
                                    self.topic_capital_letters, 
                                    self.topic_capital_letters)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+5, 
                                           self.topic_capital_letters, 
                                           self.topic_capital_letters)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test15_lesson_addition_only_with_small_letters(self):
        """ 
        Test 15 Checks lesson addition with small letters 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+6, 
                                    self.topic_small_letters, 
                                    self.topic_small_letters)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+6, 
                                           self.topic_small_letters, 
                                           self.topic_small_letters)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test16_lesson_addition_only_with_special_symbols(self):
        """ 
        Test 16 Checks lesson addition with special symbols 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+7, 
                                    self.topic_special_symbols, 
                                    self.topic_special_symbols)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+7, 
                                           self.topic_special_symbols, 
                                           self.topic_special_symbols)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test17_lesson_addition_only_with_letters_numbers(self):
        """ 
        Test 17 Checks lesson addition with letters and numbers 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+8, 
                                    self.topic_letters_numbers, self.hometask1)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+8, 
                                           self.topic_letters_numbers, 
                                           self.hometask1)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test18_lesson_addition_only_with_outer_spaces(self):
        """ 
        Test 18 Checks lesson addition with outer spaces 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+9, 
                                    self.topic_outer_spaces, 
                                    self.topic_outer_spaces)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+9, 
                                           self.topic_outer_spaces, 
                                           self.topic_outer_spaces)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test19_lesson_addition_only_with_key_sensitive(self):
        """ 
        Test 19 Checks lesson addition with key sensitive letters 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+10, 
                                    self.topic_key_sensitive, self.hometask2)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+10, 
                                           self.topic_key_sensitive, 
                                           self.hometask2)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test20_lesson_addition_only_with_html_scripts(self):
        """ 
        Test 20 Checks lesson addition with HTML scripts 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+11, 
                                    self.topic_html, self.hometask3)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+11, 
                                           self.topic_html, self.hometask3)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test21_lesson_addition_only_with_javascript(self):
        """ 
        Test 21 Checks lesson addition with javascripts 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+12, 
                                    self.topic_javascript, 
                                    self.hometask4)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+12, 
                                           self.topic_javascript, 
                                           self.hometask4)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test22_lesson_addition_only_with_sql_script(self):
        """ 
        Test 22 Checks lesson addition with sql script 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+13, 
                                    self.topic_sql, self.topic_sql)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+13, 
                                           self.topic_sql, self.topic_sql)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test23_lesson_addition_only_with_symbols_code(self):
        """ 
        Test 23 Checks lesson addition with symbols code 
        """
        driver = self.driver
        self.fill_in_lesson_add_form(2, self.lesson_number+14, 
                                    self.topic_symbols_code, 
                                    self.hometask5)
        self.check_correct_lesson_addition(u"8Б", self.lesson_number+14, 
                                           self.topic_symbols_code, 
                                           self.hometask5)
        #self.assertTrue("Додати урок", driver.find_element_by_xpath(
        #                "//h3[contains(.,'Додати урок')]"))

    def test24_lesson_addition_yesterdays_date(self):
        """ 
        Test 24 Checks lesson addition with yesterday's date if there 
        was no lessons of the subject today 
        """
        self.fill_in_date(1, u"9Б", self.lesson_number, "2016-05-12")
        self.check_correct_date_addition(u"9Б", self.lesson_number, "12.05")

    def test25_lesson_addition_tomorrows_date(self):
        """ 
        Test 25 Checks lesson addition with tomorrow's date 
        """
        self.fill_in_date(1, u"9Б", self.lesson_number+1, "2016-05-14")
        self.check_correct_date_addition(u"9Б", self.lesson_number+1, "14.05")

    def test26_lesson_addition_yesterdays_date_today(self):
        """ 
        Test 26 Checks lesson addition with yesterday's date if today's 
        lesson was added 
        """
        self.fill_in_date(1, u"9Б", self.lesson_number+2, "2016-05-13")
        self.check_correct_date_addition(u"9Б", self.lesson_number+1, "13.05")

    def test27_lesson_addition_with_previous_year(self):
        """ 
        Test 27 Checks lesson addition with previous year 
        """
        self.fill_in_date(1, u"9Б", self.lesson_number+3, "2015-05-13")
        self.check_correct_date_addition(u"9Б", 2, "13.05")

    def test28_lesson_addition_yyyyddmm(self):
        """ 
        Test 28 Checks lesson addition with inversed position of day and month 
        """
        self.fill_in_date(1, u"9Б", self.lesson_number+4, "2016-22-05")
        self.check_correct_date_addition(u"9Б", self.lesson_number+4, "22.05")

    def test29_lesson_addition_ddmmyyyy(self):
        """ 
        Test 29 Checks lesson addition with date format dd-mm-yyyy 
        """
        self.fill_in_date(1, u"9Б", self.lesson_number+5, "22-05-2016")
        self.check_correct_date_addition(u"9Б", self.lesson_number+5, "22.05")

    def test30_lesson_addition_with_slash_in_date(self):
        """ 
        Test 30 Checks lesson addition with slash instead of dash in date 
        """
        self.fill_in_date(1, u"9Б", self.lesson_number+6, "2016/05/25")
        self.check_correct_date_addition(u"9Б", self.lesson_number+5, "25.05")

    def test31_lesson_addition_with_dot_in_date(self):
        """ 
        Test 31 Checks lesson addition with dot instead of dash in date 
        """
        self.fill_in_date(1, u"9Б", self.lesson_number+7, "2016.05.25")
        self.check_correct_date_addition(u"9Б", self.lesson_number+6, "25.05")

    def test32_lesson_addition_float_date(self):
        """ 
        Test 32 Checks lesson addition with float numbers in date 
        """
        self.fill_in_date(1, u"9Б", self.lesson_number+8, "20.160515")
        self.check_correct_date_addition(u"9Б", self.lesson_number+8, "20.160515")

    def test33_lesson_addition_1859_year_date(self):
        """ 
        Test 33 Checks lesson addition with 1859 year in date 
        """
        self.fill_in_date(1, u"9Б", self.lesson_number+9, "1859-05-22")
        self.check_correct_date_addition(u"9Б", 3, "22.05") 

    def lesson_type_addition(self, class_link, inp_data, lesson_link, type_value):
        """ 
        Function for lesson addition with different types 
        """
        driver = self.driver
        driver.find_element_by_xpath(
               "html/body/div[2]/div/div[2]/div/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='2']/a[" + str(class_link) + "]").\
                                     click()
        self.assertTrue(u"Класс: ", driver.find_element_by_xpath(
                        "//h5[contains(.,'Класс: ')]"))
        driver.find_element_by_xpath(
               "html/body/div[2]/div/div[2]/div/div/table[2]/thead/tr/th[" + \
                str(lesson_link) + "]/a").click()
        self.assertTrue(u"Додати урок", driver.find_element_by_xpath(
                        "//h3[contains(.,'Додати урок')]"))
        input_data = driver.find_element_by_id("date")
        input_data.clear()
        input_data.send_keys(inp_data)
        input_topic = driver.find_element_by_id("inputTopic")
        input_topic.clear()
        input_topic.send_keys(u"Eurovision Song Contest 2016")
        input_hometask = driver.find_element_by_id("inputHomework")
        input_hometask.clear()
        input_hometask.send_keys(u"Watch Online")
        Select(driver.find_element_by_id("selectDir")).select_by_value(str(type_value))
        driver.find_element_by_name('add_button').click()

    def check_lesson_type(self, lesson_link, selected_type):
        """ 
        Function for checking the correct lesson type 
        """
        driver = self.driver
        self.assertTrue(u"Класс: ", driver.find_element_by_xpath(
                        "//h5[contains(.,'Класс: ')]"))
        driver.find_element_by_xpath(
               "html/body/div[2]/div/div[2]/div/div/table[2]/thead/tr/th[" + \
                str(lesson_link) + "]/a").click()
        self.assertTrue(u"Редагувати урок", driver.find_element_by_xpath(
                        "//h3[contains(.,'Редагувати урок')]"))
        select_type = Select(driver.find_element_by_id("selectDir"))
        self.assertTrue(select_type.first_selected_option.text, selected_type)

    def test34_lesson_addition_type_Lab(self):
        """ 
        Test 34 Checks lesson addition with lesson type as Lab 
        """
        self.lesson_type_addition(1, u"2016-05-26", self.lesson_number+10, 2) 
        self.check_lesson_type(self.lesson_number+8, 
                               u"Самостійна/Лабораторна робота")

    def test35_lesson_addition_type_Control(self):
        """ 
        Test 35 Checks lesson addition with lesson type as Control Work 
        """
        self.lesson_type_addition(1, u"2016-05-27", self.lesson_number+11, 3)
        self.check_lesson_type(self.lesson_number+9, u"Контрольна робота")

    def test36_lesson_addition_type_Usual(self):
        """ 
        Test 36 Checks lesson addition with lesson type as Usual Lesson 
        (default setting) 
        """
        self.lesson_type_addition(1, u"2016-05-28", self.lesson_number+12, 1)
        self.check_lesson_type(self.lesson_number+10, u"Звичайний")
        
    def tearDown(self):
        """ 
        Fixture that deletes all preparation for tests and restores
        original data
        """
        super(LessonAddition, self).tearDown()

if __name__ == "__main__":
    TestPrepTemplate.prepare_db()
    try:
        unittest.main(verbosity=2)
    finally:
        print(TestPrepTemplate.prepare_db(action='tearDown'))
