#  -*- coding: utf-8 -*-
""""
Test suite for test search tool work
for main teacher of the system
"""

import unittest
import os

import ssh_mod
from testsetup import TestSetup


class TestChangeAvatar(TestSetup):

    """
    Test cases that check possibility
    to change avatar as a user of the system
    """

    def setUp(self):
        """
        Test setup just to add imlicit wait command
        """

        super(TestChangeAvatar, self).setUp()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """
        Base tearDown call
        """

        super(TestChangeAvatar, self).tearDown()
        # pass

    def _change(self, filename, fileext, positive=True):
        """
        General actions for test about changing user avatar
        """

        driver = self.driver
        driver.find_element_by_xpath(
            '//a[@href="/core/profile/"]').click()
        driver.find_element_by_xpath(
            '//a[@href="/core/img_upload/"]').click()

        elem = driver.find_element_by_xpath("//input[@type='file']")
        elem.send_keys(os.getcwd() + "/change_avatar/" +
                       filename + "." + fileext)
        driver.find_element_by_xpath('//button[text()="Зберегти"]').click()
        self.assertTrue(
            ('Exception' or 'IOError' or 'Image too large') not in
            driver.page_source,
            msg="unhandled exception occurred while uploading " +
            filename + "." + fileext
        )
        elem = driver.find_element_by_xpath(
            '//html/body/div[2]/div/div[1]/div/img')
        src = elem.get_attribute('src')
        if positive:
            self.assertTrue(filename in src,
                            msg="selected file doesn't upload: " +
                                filename + "." + fileext)
        else:
            self.assertFalse(filename in src,
                             msg="selected file shouldn't be uploaded: " +
                                 filename + "." + fileext)

    def test_change_non_image_negative(self):
        """
        Negative test on change user avatar with non image file
        """

        self._change('add_image', 'js', positive=False)

    def test_change_large_image_negative(self):
        """
        Negative test on change user avatar with to large image file
        """

        self._change('test_and_code_large', 'jpg', positive=False)

    def test_change_jpg_positive(self):
        """
        Positive test on change user avatar with correct jpg image
        """

        self._change('test_and_code', 'jpg')

    def test_change_def_jpg_positive(self):
        """ Positive test on change default
        user avatar with correct jpg image"""
        self._change('test_and_code', 'jpg')

    def test_change_jpg_positive(self):
        """
        Positive test on change user avatar with correct jpg image
        """

        self._change('test_and_code_jpg', 'jpg')

    def test_change_png_positive(self):
        """
        Positive test on change user avatar with correct png image
        """

        self._change('test_and_code_png', 'png')

    def test_change_bmp_negative(self):
        """
        Nagetive test on change user avatar with bmp image
        """

        self._change('test_and_code_bmp', 'bmp', positive=False)

    def test_change_bmp_negative(self):
        """
        Negative test on change user avatar without image file
        """

        self._change('', '', positive=False)


if __name__ == "__main__":
    unittest.main(verbosity=2)

