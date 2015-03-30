# -*- coding:utf-8 -*-
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.components import AuthForm, TopMenu
from pages.pages import PageObject, TopicPage

__author__ = 'Mily-V'


class TestCreateTopic(unittest.TestCase):

    BLOG = 'Флудилка'
    TITLE = u'ЗаГоЛоВоК'
    SHORT_TEXT = u'Короткий текст, отображается в блогах!'
    MAIN_TEXT = u'Отображается внутри топика'

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

    def test_create_good_simple_topic(self):
        self.page.login()
        TopMenu(self.driver).get_username()
        self.page.create_topic(self.BLOG, self.TITLE, self.SHORT_TEXT, self.MAIN_TEXT)
        result_title = TopicPage(self.driver).topic.get_title()
        result_text = TopicPage(self.driver).topic.get_text()
        self.assertEqual(self.TITLE, result_title)
        self.assertEqual(self.MAIN_TEXT, result_text)

