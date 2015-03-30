# -*- coding:utf-8 -*-
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.components import AuthForm, TopMenu
from pages.pages import PageObject, AuthorizePage

__author__ = 'Mily-V'


class Test(unittest.TestCase):

    NAME_USER = u'Господин Манилов'

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser)
        )
        self.page = PageObject(self.driver)
        self.page.open()

    def tearDown(self):
        self.page.close()

    def test_authentication(self):
        self.page.login()
        real_user_in_result = TopMenu(self.driver).get_username()
        self.assertEqual(real_user_in_result, self.NAME_USER)


