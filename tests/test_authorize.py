# -*- coding:utf-8 -*-
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.components import TopMenu
from pages.pages import Page, AuthorizePage
import pages.constants

__author__ = 'Mily-V'


class TestAuth(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser)
        )
        self.page = Page(self.driver)
        self.page.open()

    def tearDown(self):
        self.page.close()

    def test_good_authorize(self):
        AuthorizePage(self.driver).login()
        real_user_in_result = TopMenu(self.driver).get_username()
        self.assertEqual(real_user_in_result, pages.constants.NAME_USER)


