# -*- coding: utf-8 -*-
""""
Test suite for test search tool work
for main teacher of the system
"""

import time
import unittest

from selenium.webdriver.common.keys import Keys
from testsetup import TestSetup
from tpt import TestPrepTemplate


class TestSearchTool(TestSetup):

    """ Class for testing search tool
    """

    def setUp(self):
        super(TestSearchTool, self).setUp()

        # timeout in seconds
        self._timeout = 2.0

        self._xpaths = {
            'btn-search': '//button[text()="Пошук"]',
            'link-schools': '//a[@href="/mainteacher/schools_list/"]',
            'link-teachers': '//a[@href="/mainteacher/teachers_list/"]',
            'search-table-row': '//tbody/tr[@id]'
        }

    def tearDown(self):
        super(TestSearchTool, self).tearDown()

    def _search(self, search_text='',
                link='', expected_count=0,
                fail_msg='test FAIL'):
        """ General actions for all tests about search tool testing"""
        driver = self.driver
        driver.find_element_by_xpath(link).click()
        elem = driver.find_element_by_name('search_text')
        elem.send_keys(search_text.decode('utf-8'))
        driver.find_element_by_xpath(self._xpaths['btn-search']).click()

        start_time = time.time()
        expected_result = False
        while not expected_result:
            expected_result = [False, True][len(driver.find_elements_by_xpath(
                self._xpaths['search-table-row'])) == expected_count]
            if time.time()-start_time > self._timeout:
                break
        else:
            return

        self.fail(fail_msg)

    def _search_by_enter(self, search_text='',
                link='', expected_count=0,
                fail_msg='test FAIL'):

        driver = self.driver
        driver.find_element_by_xpath(link).click()
        elem = driver.find_element_by_name('search_text')
        elem.send_keys(search_text.decode('utf-8'))
        elem.send_keys(Keys.ENTER)

        start_time = time.time()
        expected_result = False
        while not expected_result:
            expected_result = [False, True][len(driver.find_elements_by_xpath(
                self._xpaths['search-table-row'])) == expected_count]
            if time.time() - start_time > self._timeout:
                break
        else:
            return

        self.fail(fail_msg)

    # Tests for search among schools
    def test_search_schools_text_empty(self):
        """ TestCase for search among schools by empty text"""
        self._search(link=self._xpaths['link-schools'],
                     search_text='',
                     expected_count=3,
                     fail_msg="Test search by empty text FAILED")

    def test_search_schools_text_cyrilic(self):
        """ TestCase for search among schools by cyrilic text"""
        self._search(link=self._xpaths['link-schools'],
                     search_text='Колегіум',
                     expected_count=1,
                     fail_msg="Test search by cyrilic text FAILED")

    def test_search_schools_text_latin(self):
        """ TestCase for search among schools by latin text"""
        self._search(link=self._xpaths['link-schools'],
                     search_text='Colledge',
                     expected_count=1,
                     fail_msg="Test search by latin text FAILED")

    def test_search_schools_numbers(self):
        """ TestCase for search among schools by numbers"""
        self._search(link=self._xpaths['link-schools'],
                     search_text='111222333',
                     expected_count=1,
                     fail_msg="Test search by numbers FAILED")

    def test_search_schools_text_untrimmed(self):
        """ TestCase for search among schools by untrimmed text"""
        self._search(link=self._xpaths['link-schools'],
                     search_text='  Колегіум  ',
                     expected_count=1,
                     fail_msg="Test search by text with spaces FAILED")

    def test_search_schools_text_wrong_case(self):
        """ TestCase for search among schools by text with wrong capacity"""
        self._search(link=self._xpaths['link-schools'],
                     search_text='колегіум',
                     expected_count=1,
                     fail_msg="Test search by text with wrong case FAILED")

    def test_search_schools_by_key_enter(self):
        """ TestCase for search among schools by cyrilic text by key Enter"""
        self._search_by_enter(link=self._xpaths['link-schools'],
                              search_text='Колегіум',
                              expected_count=1,
                              fail_msg="Test search by key enter FAILED")

    # Tests for search among teachers
    def test_search_teachers_text_empty(self):
        """ TestCase for search among teachers by empty text"""
        self._search(link=self._xpaths['link-teachers'],
                     search_text='',
                     expected_count=3,
                     fail_msg="Test search by empty text FAILED")

    def test_search_teachers_text_cyrilic(self):
        """ TestCase for search among teachers by cyrilic text"""
        self._search(link=self._xpaths['link-teachers'],
                     search_text='Тест',
                     expected_count=1,
                     fail_msg="Test search by cyrilic text FAILED")

    def test_search_teachers_text_latin(self):
        """ TestCase for search among teachers by latin text"""
        self._search(link=self._xpaths['link-teachers'],
                     search_text='Test',
                     expected_count=1,
                     fail_msg="Test search by latin text FAILED")

    def test_search_teachers_numbers(self):
        """ TestCase for search among teachers by numbers"""
        self._search(link=self._xpaths['link-teachers'],
                     search_text='111222333',
                     expected_count=1,
                     fail_msg="Test search by numbers FAILED")

    def test_search_teachers_text_untrimmed(self):
        """ TestCase for search among teachers by untrimmed text"""
        self._search(link=self._xpaths['link-teachers'],
                     search_text='  Тест  ',
                     expected_count=1,
                     fail_msg="Test search by text with spaces FAILED")

    def test_search_teachers_text_wrong_case(self):
        """ TestCase for search among teachers by text with wrong capacity"""
        self._search(link=self._xpaths['link-teachers'],
                     search_text='тест',
                     expected_count=1,
                     fail_msg="Test search by text with wrong case FAILED")

    def test_search_teachers_by_key_enter(self):
        """ TestCase for search among teachers by cyrilic text by key Enter"""
        self._search_by_enter(link=self._xpaths['link-teachers'],
                              search_text='Тест',
                              expected_count=1,
                              fail_msg="Test search by key enter FAILED")


if __name__ == "__main__":
    # try:
    #     TestPrepTemplate.prepare_db(sql_filename='psv_test.sql')
    # except:
    #     TestPrepTemplate.prepare_db(action='teardown')
    #     exit()

    TestPrepTemplate.prepare_db(sql_filename='psv_test.sql')
    try:
        unittest.main(verbosity=2)
    finally:
        TestPrepTemplate.prepare_db(action='teardown')

