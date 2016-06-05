# -*- coding: utf-8 -*-
""" Tests for login Process (testing with Selenium) """

import unittest
from selenium import webdriver


class SmokeTests(unittest.TestCase):
    """ Smoke tests for login process - check UI elements presence """

    base_url = "http://sms-rv016atqc.rhcloud.com"

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.accept_next_alert = True

    def test_ui_presence(self):
        """ 01. Check, that login page contains fields and buttons """

        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_name("inputUsername")
        driver.find_element_by_name("inputPassword")
        driver.find_element_by_xpath("//button[contains(.,'Увійти')]")

    def tearDown(self):
        """ Fixture that deletes all preparation for tests """

        self.driver.quit()


class PositiveTests(unittest.TestCase):
    """ Positive tests for login process with correct data,
    expected result - login is successful
    """

    # _list_login_correct = ["semuschenko",
    #                        "zoshch",
    #                        "maximus",
    #                        "sEmUsChEnKo",
    #                        "semuschenko"]
    # _list_password_correct = ["pDk7jf",
    #                           "df5sFdf",
    #                           "LKuJf3y",
    #                           "pDk7jf",
    #                           "pDk7jf"]
    # _list_url_part = ["/mainteacher/",
    #                   "/director/",
    #                   "/teacher/",
    #                   "/mainteacher/",
    #                   "/mainteacher/"]
    # _list_position = ["Головний вчитель",
    #                   "Завуч",
    #                   "Викладач",
    #                   "Головний вчитель",
    #                   "Головний вчитель"]
    # _list_name = ["Семищенко Христофор Онуфрійович",
    #               "Зощенко Іван Вікторович",
    #               "Галицький Максим Генадійович",
    #               "Семищенко Христофор Онуфрійович",
    #               "Семищенко Христофор Онуфрійович"]
    #
    # _test_data = zip(_list_login_correct,
    #                  _list_password_correct,
    #                  _list_url_part,
    #                  _list_position,
    #                  _list_name)
    #
    # test_data_count = len(_test_data)

    base_url = "http://sms-rv016atqc.rhcloud.com"


    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        # input_error_msg = "Quantity of input parameters must be equal"
        # self.assertEqual(len(self._list_login_correct),
        #                  len(self._list_password_correct),
        #                  input_error_msg)
        # self.assertEqual(len(self._list_password_correct),
        #                  len(self._list_url_part),
        #                  input_error_msg)
        # self.assertEqual(len(self._list_url_part),
        #                  len(self._list_position),
        #                  input_error_msg)
        # self.assertEqual(len(self._list_position),
        #                  len(self._list_name),
        #                  input_error_msg)

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.accept_next_alert = True

    # def _set_test_data(self):
    #     """ Creating initial data for each test """
    #
    #     self.login = self._list_login_correct[self.current_test]
    #     self.password = self._list_password_correct[self.current_test]
    #     self.url_part = self._list_url_part[self.current_test]
    #     self.position = self._list_position[self.current_test]
    #     self.name = self._list_name[self.current_test]


    def _test_steps(self):
        """ Common tests steps """

        # self._set_test_data()

        print("\nPositive test for : ")
        print([self.login, self.password,
               self.url_part, self.position, self.name])

        driver = self.driver
        driver.get(self.base_url)

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password.decode('utf-8'))
        driver.find_element_by_xpath("//button[@type='submit']").click()

        self.assertIn(self.url_part, driver.current_url)
        self.assertIn(self.position.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//h5[@class='inline']").text)
        self.assertIn(self.name.decode('utf-8'),
                      driver.find_element_by_xpath(
                          "//p[@class='profile__name']").text)

    def test01_main_teacher_login(self):
        """
        01. Login Should Succeed for main teacher when the correct Username
        and Password are entered
        """

        self.login = "semuschenko"
        self.password = "pDk7jf"
        self.url_part = "/mainteacher/"
        self.position = "Головний вчитель"
        self.name = "Семищенко Христофор Онуфрійович"

        self._test_steps()

    def test02_school_director_login(self):
        """
        02. Login Should Succeed for school director when the correct
        Username and Password are entered
        """

        self.login = "zoshch"
        self.password = "df5sFdf"
        self.url_part = "/director/"
        self.position = "Завуч"
        self.name = "Зощенко Іван Вікторович"

        self._test_steps()

    def test03_common_teacher_login(self):
        """
        03. Login Should Succeed for teacher when the correct Username and
        Password are entered
        """

        self.login = "maximus"
        self.password = "LKuJf3y"
        self.url_part = "/teacher/"
        self.position = "Викладач"
        self.name = "Галицький Максим Генадійович"

        self._test_steps()

    def test04_main_teacher_login_case(self):
        """
        04. Login Should Succeed for main teacher when the correct Username
        (different case) and Password are entered
        """

        self.login = "sEmUsChEnKo"
        self.password = "pDk7jf"
        self.url_part = "/mainteacher/"
        self.position = "Головний вчитель"
        self.name = "Семищенко Христофор Онуфрійович"

        self._test_steps()

    def test05_login_restore(self):
        """
        05. Test whether login/close/reopen browser shows an login page
        with empty fields
        """

        self.login = "sEmUsChEnKo"
        self.password = "pDk7jf"
        self.url_part = "/mainteacher/"
        self.position = "Головний вчитель"
        self.name = "Семищенко Христофор Онуфрійович"

        self._test_steps()

        self.driver.quit()

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://sms-rv016atqc.rhcloud.com"
        self.accept_next_alert = True
        driver = self.driver
        driver.get(self.base_url + "/")
        self.assertEqual(driver.find_element_by_name("inputUsername").text, "")
        self.assertEqual(driver.find_element_by_name("inputPassword").text, "")

    def tearDown(self):
        """ Fixture that deletes all preparation for tests """

        self.driver.quit()


class NegativeTests(unittest.TestCase):
    """ Negative tests for login process with incorrect data,
    expected result - login is unsuccessful
    """
    #
    # _list_login_incorrect = \
    #     ["semuschenko",
    #      "pDk7jf",
    #      "",
    #      "loginloginlogin",
    #      "",
    #      "loginloginlogin",
    #      "semuschenko",
    #      "loginloginlogin",
    #      "<script>alert(123)</script>",
    #      "(' or 'a' = 'a'; DROP TABLE teachers; SELECT * FROM teachers;)",
    #      "' or 'a' = 'a'; DROP TABLE teachers; SELECT * FROM teachers;",
    #      "(<script>alert(\"Hello, world!\")</alert>, <script>document.getElementByID(\"…\").disabled=true</script>)",
    #      "<script>alert(\"Hello, world!\")</alert>, <script>document.getElementByID(\"…\").disabled=true</script>",
    #      "(<form action=\"http://sms-rv016atqc.rhcloud.com/\"><input type=\"submit\"></form>)",
    #      "<form action=\"http://sms-rv016atqc.rhcloud.com/\"><input type=\"submit\"></form>",
    #      "\x23\x27\xE2\x80\x9C\xE2\x99\xA3\xE2\x98\xBA\xE2\x99\x82\xE2\x80\x9D\x20\x2C\x20\xE2\x80\x9C\xE2\x80\x9D\xE2\x80\x98\x7E\x21\x40\x23\x24\x25\x5E\x26\x2A\x28\x29\x3F\x3E\x2C\x2E\x2F\x5C\x3C\x5D\x5B\x20\x2F\x2A\x3C\x21\xE2\x80\x93\xE2\x80\x9C\xE2\x80\x9D\x2C\x20\xE2\x80\x9C\x24\x7B\x63\x6F\x64\x65\x7D\xE2\x80\x9D\x3B\xE2\x80\x93\x3E\x27",
    #      "\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20",
    #      "\x20\x20\x20\x20semuschenko",
    #      "semuschenko\x20\x20\x20\x20",
    #      "логін",
    #      "<semuschenko>"]
    #
    # _list_password_incorrect = \
    #     ["PdK7Jf",
    #      "semuschenko",
    #      "",
    #      "",
    #      "passwordpasswordpassword",
    #      "passwordpasswordpassword",
    #      "passwordpasswordpassword",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "pDk7jf",
    #      "пароль123!?%&",
    #      "pDk7jf"]

    login_part = "/mainteacher/"

    warning_message = "Невірно вказаний пароль або логін"
    page_title = "Авторизація | SMS"

    base_url = "http://sms-rv016atqc.rhcloud.com"

    # _test_data = zip(_list_login_incorrect,
    #                  _list_password_incorrect)
    #
    # test_data_count = len(_test_data)

    def setUp(self):
        """ Fixture that creates a initial data and records for tests """

        # input_error_msg = "Quantity of input parameters must be equal"
        # self.assertEqual(len(self._list_login_incorrect),
        #                  len(self._list_password_incorrect), input_error_msg)

        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.accept_next_alert = True

    # def _set_test_data(self):
    #     """ Creating initial data for each test """
    #
    #     self.login = self._list_login_incorrect[self.current_test]
    #     self.password = self._list_password_incorrect[self.current_test]
    #     print("\nNegative test for : ")
    #     print(list(param for param in self._test_data[self.current_test]))

    def _test_steps(self):
        """ Common tests steps """

        # self._set_test_data()

        print("\nNegative test for : ")
        print([self.login, self.password])

        driver = self.driver
        driver.get(self.base_url + "/")

        input_username = driver.find_element_by_name("inputUsername")
        input_username.clear()
        input_username.send_keys(self.login.decode('utf-8'))
        input_password = driver.find_element_by_name("inputPassword")
        input_password.clear()
        input_password.send_keys(self.password.decode('utf-8'))
        driver.find_element_by_xpath("//button[@type='submit']").click()

        self.assertNotIn(self.login_part,
                         driver.current_url,
                         "Login is successful, while expecting otherwise")

        if self.login != "" and self.password != "":
            self.assertIn(self.warning_message.decode('utf-8'),
                          driver.find_element_by_xpath(
                              "//span[@class='help-block']").text)
        else:
            self.assertIn(self.page_title.decode('utf-8'), driver.title)

    def test01_password_mixed_case(self):
        """
        01. Warning Message Should appear for user when the correct
        Username and Password (different case) are entered
        """

        self.login = "semuschenko"
        self.password = "PdK7Jf"
        self._test_steps()

    def test02_username_password_rearranged(self):
        """
        02. Warning Message Should appear for user when the
        Password->Username and Username->Password
        """

        self.login = "pDk7jf"
        self.password = "semuschenko"

        self._test_steps()

    def test03_username_password_empty(self):
        """
        03. Warning Message Should appear for user when the Username
        and Password left empty
        """

        self.login = ""
        self.password = ""

        self._test_steps()

    def test04_password_empty(self):
        """
        04. Warning Message Should appear for user when the
        Password left empty
        """

        self.login = "loginloginlogin"
        self.password = ""

        self._test_steps()

    def test05_username_empty(self):
        """
        05. Warning Message Should appear for user when the
        Username left empty
        """

        self.login = ""
        self.password = "passwordpasswordpassword"

        self._test_steps()

    def test06_username_password_incorrect(self):
        """
        06. Warning Message Should appear for user when the incorrect
        Username and Password are Entered
        """

        self.login = "loginloginlogin"
        self.password = "passwordpasswordpassword"

        self._test_steps()

    def test07_password_incorrect(self):
        """
        07. Warning Message Should appear for user when the correct
        Username and incorrect Password are Entered
        """

        self.login = "semuschenko"
        self.password = "passwordpasswordpassword"

        self._test_steps()

    def test08_username_incorrect(self):
        """
        08. Warning Message Should appear for user when the incorrect
        Username and correct Password are Entered
        """
        self.login = "loginloginlogin"
        self.password = "pDk7jf"

        self._test_steps()

    def test09_username_injection(self):
        """
        09. Warning Message Should appear for user when the
        injection1 -> Username and correct Password are Entered
        """

        self.login = "<script>alert(123)</script>"
        self.password = "pDk7jf"

        self._test_steps()

    def test10_username_injection(self):
        """
        10. Warning Message Should appear for user when the
        injection2 -> Username and correct Password are Entered
        """

        self.login = "(' or 'a' = 'a'; DROP TABLE teachers; " \
                     "SELECT * FROM teachers;)"
        self.password = "pDk7jf"

        self._test_steps()

    def test11_username_injection(self):
        """
        11. Warning Message Should appear for user when the
        injection3 -> Username and correct Password are Entered
        """

        self.login = "' or 'a' = 'a'; DROP TABLE teachers; " \
                     "SELECT * FROM teachers;"
        self.password = "pDk7jf"

        self._test_steps()

    def test12_username_injection(self):
        """
        12. Warning Message Should appear for user when the
        injection4 -> Username and correct Password are Entered
        """

        self.login = "(<script>alert(\"Hello, world!\")</alert>, " \
                     "<script>document.getElementByID(\"…\")." \
                     "disabled=true</script>)"
        self.password = "pDk7jf"

        self._test_steps()

    def test13_username_injection(self):
        """
        13. Warning Message Should appear for user when the
        injection5 -> Username and correct Password are Entered
        """

        self.login = "<script>alert(\"Hello, world!\")</alert>, " \
                     "<script>document.getElementByID(\"…\")." \
                     "disabled=true</script>"
        self.password = "pDk7jf"

        self._test_steps()

    def test14_username_injection(self):
        """
        14. Warning Message Should appear for user when the
        injection6 -> Username and correct Password are Entered
        """

        self.login = "(<form action=\"http://sms-rv016atqc.rhcloud.com/\">" \
                     "<input type=\"submit\"></form>)"
        self.password = "pDk7jf"

        self._test_steps()

    def test15_username_injection(self):
        """
        15. Warning Message Should appear for user when the
        injection7 -> Username and correct Password are Entered
        """

        self.login = "<form action=\"http://sms-rv016atqc.rhcloud.com/\">" \
                     "<input type=\"submit\"></form>"
        self.password = "pDk7jf"

        self._test_steps()

    def test16_username_incorrect_password_correct(self):
        """
        16. Warning Message Should appear for user when the wrong
        Username and correct Password are Entered
        """

        #'“♣☺♂” , “”‘~!@#$%^&*()?>,./\<][ /*<!–“”, “${code}”;–>'
        self.login = "\x23\x27\xE2\x80\x9C\xE2\x99\xA3\xE2\x98\xBA\xE2" \
                     "\x99\x82\xE2\x80\x9D\x20\x2C\x20\xE2\x80\x9C\xE2" \
                     "\x80\x9D\xE2\x80\x98\x7E\x21\x40\x23\x24\x25\x5E" \
                     "\x26\x2A\x28\x29\x3F\x3E\x2C\x2E\x2F\x5C\x3C\x5D" \
                     "\x5B\x20\x2F\x2A\x3C\x21\xE2\x80\x93\xE2\x80\x9C" \
                     "\xE2\x80\x9D\x2C\x20\xE2\x80\x9C\x24\x7B\x63\x6F" \
                     "\x64\x65\x7D\xE2\x80\x9D\x3B\xE2\x80\x93\x3E\x27"
        self.password = "pDk7jf"

        self._test_steps()

    def test17_username_from_spaces(self):
        """
        17. Warning Message Should appear for user when the wrong Username
        only with spaces and correct Password are Entered
        """

        self.login = "\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20"
        self.password = "pDk7jf"

        self._test_steps()

    def test18_username_with_spaces_on_start(self):
        """
        18. Warning Message Should appear for user when the correct
        Username with spaces at beginning and correct Password are Entered
        """

        self.login = "\x20\x20\x20\x20semuschenko"
        self.password = "pDk7jf"

        self._test_steps()

    def test19_username_with_spaces_on_end(self):
        """
        19. Warning Message Should appear for user when the correct
        Username with spaces on the end and correct Password are Entered
        """

        self.login = "semuschenko\x20\x20\x20\x20"
        self.password = "pDk7jf"

        self._test_steps()

    def test20_username_password_cyrillic(self):
        """
        20. Warning Message Should appear for user when the Username and
        Password (both cyrillic) are Entered
        """

        self.login = "логін"
        self.password = "пароль123!?%&"

        self._test_steps()

    def test21_username_incorrect_password_correct(self):
        """
        21. Warning Message Should appear for user when the incorrect
        Username with <> and correct Password are Entered
        """

        self.login = "<semuschenko>"
        self.password = "pDk7jf"

        self._test_steps()

    def tearDown(self):
        """ Fixture that deletes all preparation for tests """

        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
