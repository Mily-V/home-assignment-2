# -*- coding:utf-8 -*-
import os
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities, Remote
from pages.components import TopMenu, CreateTopicForm
from pages.pages import Page, TopicPage, CreateTopicPage, AuthorizePage, BlogPage
import pages.constants
import pages.locator
import time

__author__ = 'Mily-V'


class TestCreateTopic(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser)
        )
        self.page = Page(self.driver)
        self.page.open()
        AuthorizePage(self.driver).login()
        TopMenu(self.driver).get_username()
        self.create_topic_page = CreateTopicPage(self.driver)
        self.create_topic_page.open()


    def tearDown(self):
        self.page.close()

    def test_bad_topic_without_blog(self):
        self.create_topic_page.create_topic_without_blog(self.create_topic_page)
        self.assertTrue(TopicPage(self.driver).topic.error_create())

    def test_bad_topic_without_title(self):
        self.create_topic_page.create_topic_without_title(self.create_topic_page)
        self.assertTrue(TopicPage(self.driver).topic.error_create())

    def test_bad_topic_without_short_text(self):
        self.create_topic_page.create_topic_without_short_text(self.create_topic_page)
        self.assertTrue(TopicPage(self.driver).topic.error_create())

    def test_bad_topic_without_main_text(self):
        self.create_topic_page.create_topic_without_main_text(self.create_topic_page)
        self.assertTrue(TopicPage(self.driver).topic.error_create())

    def test_bad_topic_with_so_long_title(self):
        self.create_topic_page.create_topic_with_so_long_limit(self.create_topic_page)
        self.assertTrue(TopicPage(self.driver).topic.error_create())

    def test_good_simple_topic_check_text(self):
        self.create_topic_page.create_topic(self.create_topic_page)
        result_title = TopicPage(self.driver).topic.get_title()
        result_text = TopicPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        self.assertEqual(pages.constants.TITLE, result_title)
        self.assertEqual(pages.constants.MAIN_TEXT, result_text)
        TopicPage(self.driver).topic.delete_topic()

    def test_good_simple_topic_check_short_text(self):
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_title = BlogPage(self.driver).topic.get_title()
        result_text = BlogPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        self.assertEqual(pages.constants.TITLE, result_title)
        self.assertEqual(pages.constants.SHORT_TEXT, result_text)
        TopicPage(self.driver).topic.delete_topic()

    def test_bold_text(self):
        self.create_topic_page.create_topic_with_bold_text(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        try:
            is_bold = self.driver.find_element_by_xpath(pages.locator.BOLD_TAG).\
                is_enabled()
        except NoSuchElementException:
            is_bold = False
        self.assertEqual(pages.constants.MAIN_TEXT, result_text)
        self.assertTrue(is_bold)
        TopicPage(self.driver).topic.delete_topic()

    def test_bold_short_text(self):
        self.create_topic_page.create_topic_with_bold_short_text(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        try:
            is_bold = self.driver.find_element_by_xpath(pages.locator.BOLD_TAG).\
                is_enabled()
        except NoSuchElementException:
            is_bold = False
        self.assertEqual(pages.constants.SHORT_TEXT, result_text)
        self.assertTrue(is_bold)
        TopicPage(self.driver).topic.delete_topic()

    def test_italic_text(self):
        self.create_topic_page.create_topic_with_italic_text(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        try:
            is_italic = self.driver.find_element_by_xpath(pages.locator.ITALIC_TAG).\
                is_enabled()
        except NoSuchElementException:
            is_italic = False
        self.assertEqual(pages.constants.MAIN_TEXT, result_text)
        self.assertTrue(is_italic)
        TopicPage(self.driver).topic.delete_topic()

    def test_italic_short_text(self):
        self.create_topic_page.create_topic_with_italic_short_text(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        try:
            is_italic = self.driver.find_element_by_xpath(pages.locator.ITALIC_TAG).\
                is_enabled()
        except NoSuchElementException:
            is_italic = False
        print is_italic
        print result_text
        self.assertEqual(pages.constants.SHORT_TEXT, result_text)
        self.assertTrue(is_italic)
        TopicPage(self.driver).topic.delete_topic()

    def test_quote_text(self):
        CreateTopicForm(self.driver).set_quote_text(pages.locator.QUOTE_MAIN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        waiting_result = '> ' + pages.constants.MAIN_TEXT
        self.assertEqual(waiting_result, result_text)
        TopicPage(self.driver).topic.delete_topic()

    def test_quote_short_text(self):
        CreateTopicForm(self.driver).set_quote_text(pages.locator.QUOTE_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        waiting_result = '> ' + pages.constants.SHORT_TEXT
        self.assertEqual(waiting_result, result_text)
        TopicPage(self.driver).topic.delete_topic()

    # добавить неупорядоченный список в майн текст


    def test_unordered_short_text(self):
        CreateTopicForm(self.driver).set_unordered_list_text(pages.locator.UNORDERED_LIST_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.get_text(pages.locator.UNORDERED_LIST_TAG)
        self.assertEqual(pages.constants.SHORT_TEXT, result_text)
        TopicPage(self.driver).topic.delete_topic()

    def test_ordered_list_text(self):
        CreateTopicForm(self.driver).set_ordered_list_text(pages.locator.ORDERED_LIST_MAIN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.get_text(pages.locator.ORDERED_LIST_TAG)
        self.assertEqual(pages.constants.MAIN_TEXT, result_text)
        TopicPage(self.driver).topic.delete_topic()

    def test_ordered_short_text(self):
        CreateTopicForm(self.driver).set_ordered_list_text(pages.locator.ORDERED_LIST_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.get_text(pages.locator.ORDERED_LIST_TAG)
        self.assertEqual(pages.constants.SHORT_TEXT, result_text)
        TopicPage(self.driver).topic.delete_topic()


    def test_link_text(self):
        CreateTopicForm(self.driver).set_link_in_text(pages.locator.LINK_MAIN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        try:
            result_text = self.driver.find_element_by_xpath(pages.locator.LINK_TAG).\
                get_attribute('href')
        except NoSuchElementException:
            result_text = False
        self.assertIsNot(result_text, False)
        self.assertEqual(result_text, pages.constants.REFERENCE)
        TopicPage(self.driver).topic.delete_topic()

    def test_link_short_text(self):
        CreateTopicForm(self.driver).set_link_in_text(pages.locator.LINK_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        try:
            result_text = self.driver.find_element_by_xpath(pages.locator.LINK_TAG).\
                get_attribute('href')
        except NoSuchElementException:
            result_text = False
        self.assertIsNot(result_text, False)
        self.assertEqual(result_text, pages.constants.REFERENCE)
        TopicPage(self.driver).topic.delete_topic()

    def test_fix_image_text(self):
        CreateTopicForm(self.driver).set_fix_image_in_text(pages.locator.FIX_IMAGE_MAIN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        try:
            result_text = self.driver.find_element_by_xpath(pages.locator.IMAGE_TAG).\
                is_enabled()
        except NoSuchElementException:
            result_text = False
        print result_text
        self.assertTrue(result_text)
        TopicPage(self.driver).topic.delete_topic()

    def test_fix_image_short_text(self):
        CreateTopicForm(self.driver).set_fix_image_in_text(pages.locator.FIX_IMAGE_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        try:
            result_text = self.driver.find_element_by_xpath(pages.locator.IMAGE_TAG).\
                is_enabled()
        except NoSuchElementException:
            result_text = False
        print result_text
        self.assertTrue(result_text)
        TopicPage(self.driver).topic.delete_topic()


    # не получается  :(
    # def test_upload_image_in_text(self):
    #     CreateTopicForm(self.driver).set_upload_image_in_text(pages.locator.UPLOAD_IMAGE_MAIN_TEXT)
    #     self.create_topic_page.create_topic(self.create_topic_page)
    #     try:
    #         result_text = self.driver.find_element_by_xpath(pages.locator.IMAGE_TAG).\
    #             is_enabled()
    #     except NoSuchElementException:
    #         result_text = False
    #     print result_text
    #     # self.assertTrue(result_text)
    #     TopicPage(self.driver).topic.delete_topic()