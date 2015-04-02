# -*- coding:utf-8 -*-
import os
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities, Remote
from pages.components import TopMenu, CreateTopicForm
from pages.pages import Page, TopicPage, CreateTopicPage, AuthorizePage, BlogPage
import pages.constants
import pages.locator

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
        try:
            TopicPage(self.driver).topic.delete_topic()
        except NoSuchElementException:
            pass
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


    def test_good_simple_topic_check_short_text(self):
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_title = BlogPage(self.driver).topic.get_title()
        result_text = BlogPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        self.assertEqual(pages.constants.TITLE, result_title)
        self.assertEqual(pages.constants.SHORT_TEXT, result_text)


    def test_bold_text(self):
        self.create_topic_page.create_topic_with_bold_text(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        is_bold = TopicPage(self.driver).topic.is_bold()
        self.assertEqual(pages.constants.MAIN_TEXT, result_text)
        self.assertTrue(is_bold)


    def test_bold_short_text(self):
        self.create_topic_page.create_topic_with_bold_short_text(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        is_bold = BlogPage(self.driver).topic.is_bold()
        self.assertEqual(pages.constants.SHORT_TEXT, result_text)
        self.assertTrue(is_bold)


    def test_italic_text(self):
        self.create_topic_page.create_topic_with_italic_text(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        is_italic = TopicPage(self.driver).topic.is_italic()
        self.assertEqual(pages.constants.MAIN_TEXT, result_text)
        self.assertTrue(is_italic)


    def test_italic_short_text(self):
        self.create_topic_page.create_topic_with_italic_short_text(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        is_italic = BlogPage(self.driver).topic.is_italic()
        self.assertEqual(pages.constants.SHORT_TEXT, result_text)
        self.assertTrue(is_italic)


    def test_quote_text(self):
        CreateTopicForm(self.driver).set_quote_text(pages.locator.QUOTE_MAIN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        waiting_result = '> ' + pages.constants.MAIN_TEXT
        self.assertEqual(waiting_result, result_text)


    def test_quote_short_text(self):
        CreateTopicForm(self.driver).set_quote_text(pages.locator.QUOTE_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.get_text(pages.locator.TEXT_TAG)
        waiting_result = '> ' + pages.constants.SHORT_TEXT
        self.assertEqual(waiting_result, result_text)


    def test_unordered_text(self):
        CreateTopicForm(self.driver).set_unordered_list_text(pages.locator.UNORDERED_LIST_MAIN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.is_unordered_list_text()
        self.assertTrue(result_text)



    def test_unordered_short_text(self):
        CreateTopicForm(self.driver).set_unordered_list_text(pages.locator.UNORDERED_LIST_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.is_unordered_list_text()
        self.assertTrue(result_text)


    def test_ordered_list_text(self):
        CreateTopicForm(self.driver).set_ordered_list_text(pages.locator.ORDERED_LIST_MAIN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.is_ordered_list_text()
        self.assertTrue(result_text)


    def test_ordered_short_text(self):
        CreateTopicForm(self.driver).set_ordered_list_text(pages.locator.ORDERED_LIST_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.is_ordered_list_text()
        self.assertTrue(result_text)


    def test_link_text(self):
        CreateTopicForm(self.driver).set_link_in_text(pages.locator.LINK_MAIN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.get_link()
        self.assertTrue(result_text)
        self.assertEqual(result_text, pages.constants.REFERENCE)


    def test_link_short_text(self):
        CreateTopicForm(self.driver).set_link_in_text(pages.locator.LINK_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.get_link()
        self.assertTrue(result_text)
        self.assertEqual(result_text, pages.constants.REFERENCE)


    def test_fix_image_text(self):
        CreateTopicForm(self.driver).set_fix_image_in_text(pages.locator.FIX_IMAGE_MAIN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.is_image_in_text()
        self.assertTrue(result_text)


    def test_fix_image_short_text(self):
        CreateTopicForm(self.driver).set_fix_image_in_text(pages.locator.FIX_IMAGE_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.is_image_in_text()
        self.assertTrue(result_text)


    def test_upload_image_in_text(self):
        CreateTopicForm(self.driver).set_upload_image_in_text(pages.locator.UPLOAD_IMAGE_MAIN_TEXT,
                                                              pages.locator.FORM_UPLOAD_IMAGE_IN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.is_image_in_text()
        self.assertTrue(result_text)


    def test_upload_image_in_short_text(self):
        CreateTopicForm(self.driver).set_upload_image_in_text(pages.locator.UPLOAD_IMAGE_SHORT_TEXT,
                                                              pages.locator.FORM_UPLOAD_IMAGE_IN_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.is_image_in_text()
        self.assertTrue(result_text)


    def test_add_user_in_text(self):
        CreateTopicForm(self.driver).set_add_user_in_text(pages.locator.ADD_USER_IN_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        result_text = TopicPage(self.driver).topic.get_link()
        self.assertEqual(result_text, pages.constants.USER)


    def test_add_user_in_short_text(self):
        CreateTopicForm(self.driver).set_add_user_in_text(pages.locator.ADD_USER_IN_SHORT_TEXT)
        self.create_topic_page.create_topic(self.create_topic_page)
        BlogPage(self.driver).topic.open_blog()
        result_text = BlogPage(self.driver).topic.get_link()
        self.assertEqual(result_text, pages.constants.USER)


    def test_add_poll(self):
        CreateTopicForm(self.driver).set_add_poll()
        self.create_topic_page.create_topic(self.create_topic_page)
        res_answ1, res_answ2 = TopicPage(self.driver).topic.get_poll_answers()
        self.assertEqual(res_answ1, pages.constants.ANSWER1)
        self.assertEqual(res_answ2, pages.constants.ANSWER2)


    def test_forbid_comment(self):
        CreateTopicForm(self.driver).set_forbid_comment()
        self.create_topic_page.create_topic(self.create_topic_page)
        result = TopicPage(self.driver).topic.is_forbid_comment()
        self.assertFalse(result)
