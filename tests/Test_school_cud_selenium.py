# -*- coding: utf-8 -*-
""" Tests on Selenium WebDriver of school CUD """
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


baseurl = "https://smsauto-dvatqc.rhcloud.com"
username = "semuschenko"
password = "pDk7jf"
nameWarning = u"Некоректно введено назву."
addressWarning = u"Некоректно введено адресу."

xpaths = {
	'inputUsername': "//input[@name='inputUsername']",
	'inputPassword': "//input[@name='inputPassword']",
	'submitButtonLogin':   "button",
	'inputSchoolName': "//*[@id='inputSchoolName']",
	'inputSchoolAddress': "//*[@id='inputNumber']",
	'confirmAddEditButton': "//*[@id='add_button']"
}

credentials = {
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

def insertCredetialsToAddSchool(driver, schoolName, address):
	""" Function to automate proccess of inserting the credentials """
	
	link = driver.find_element_by_link_text(u'+ Додати')
	link.click()
	time.sleep(2)
	driver.find_element_by_xpath(xpaths['inputSchoolName']).send_keys(schoolName)
	driver.find_element_by_xpath(xpaths['inputSchoolAddress']).send_keys(address)
	time.sleep(2)
	driver.find_element_by_xpath(xpaths['confirmAddEditButton']).click() 


class SchoolCUD(unittest.TestCase):

	""" Class with methods, for testing School CUD """

	def setUp(self):
    	""" Fixture that creates all the preparations for tests """
		
		self.driver = webdriver.Firefox()
		
		self.driver.maximize_window()

		self.driver.get(baseurl)
		
		self.driver.find_element_by_xpath(xpaths['inputUsername']).send_keys(username)
		
		self.driver.find_element_by_xpath(xpaths['inputPassword']).send_keys(password)

		self.driver.find_element_by_tag_name(xpaths['submitButtonLogin']).click()

	def tearDown(self):
		""" Fixture that deletes all the preparations for tests """
		
		self.driver.close()

	def test_window_to_add_exists(self):
		""" Test to check whether windows to add school exists """
		driver = self.driver
		
		link = driver.find_element_by_link_text(u'+ Додати')

		link.click()

		time.sleep(2)

		self.element = driver.find_element_by_tag_name('h3')
		
		self.assertEquals(u"Додати школу", self.element.text);

	def test_try_add_school_with_cancel(self):
		""" Fields to enter credentials should be empty after cancel and retry """

		driver = self.driver

		link = driver.find_element_by_link_text(u'+ Додати')

		link.click()

		time.sleep(2)

		driver.find_element_by_xpath(xpaths['inputSchoolName']).send_keys(credentials['correctName'])
		
		driver.find_element_by_xpath(xpaths['inputSchoolAddress']).send_keys(credentials['correctAddress'])

		link2 = driver.find_element_by_link_text('x')

		link2.click()

		link.click()

		time.sleep(2)

		nameValue = driver.find_element_by_xpath(xpaths['inputSchoolName'])

		addressValue = driver.find_element_by_xpath(xpaths['inputSchoolAddress'])
		
		self.assertTrue(("" == nameValue.get_attribute('value')) and \
			("" == addressValue.get_attribute('value')))

	def test_add_school_with_correct_credentials(self):
		""" New school should be added with correct credentials """

		driver = self.driver

		insertCredetialsToAddSchool(driver, credentials['correctName'], credentials['correctAddress'])
	
		src = driver.page_source
		
		if credentials['correctName'] in src:
			school_exists = True
		
		else:
			school_exists = False
		
		self.assertEqual(school_exists, True)

	def test_add_school_with_roman_name(self):
		""" Expected warning about incorrect name """

		driver = self.driver
		insertCredetialsToAddSchool(driver, credentials['nameRoman'], credentials['correctAddress'])
		src = driver.page_source
		
		if nameWarning in src:
	 		warning_exists = True
		
		else:
	 		warning_exists = False

	 	self.assertEqual(warning_exists, True)

	def test_add_school_with_roman_address(self):
		""" Expected warning about incorrect address """

		driver = self.driver

		insertCredetialsToAddSchool(driver, "", credentials['addressRoman'])
	
		src = driver.page_source
		
		if addressWarning in src:
	 		warning_exists = True
		
		else:
	 		warning_exists = False

	 	self.assertEqual(warning_exists, True)

if __name__ == "__main__":
    unittest.main()