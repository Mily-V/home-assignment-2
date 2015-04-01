# -*- coding:utf-8 -*-

import urlparse
from components import AuthForm, TopMenu, CreateTopicForm, TopicRead
import constants
import locator


__author__ = 'Mily-V'

class Page(object):

    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(constants.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()


class AuthorizePage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    def login(self):
        auth_page = AuthorizePage(self.driver)
        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(constants.LOGIN)
        auth_form.set_password(constants.PASSWORD)
        auth_form.submit()

class TopicPage(Page):

    @property
    def topic(self):
        return TopicRead(self.driver)

class BlogPage(Page):

    PATH = '/feed/live/broadcast/'

    @property
    def topic(self):
        return TopicRead(self.driver)

class CreateTopicPage(Page):
    PATH = '/blog/topic/create/'

    @property
    def form(self):
        return CreateTopicForm(self.driver)


    def create_topic(self, create_topic_page):
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(constants.BLOG)
        create_form.set_title(constants.TITLE)
        create_form.set_short_text(constants.SHORT_TEXT)
        create_form.set_main_text(constants.MAIN_TEXT)
        create_form.submit()
        return create_form

    def create_topic_without_blog(self, create_topic_page):
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.set_title(constants.TITLE)
        create_form.set_short_text(constants.SHORT_TEXT)
        create_form.set_main_text(constants.MAIN_TEXT)
        create_form.submit()
        return create_form

    def create_topic_without_title(self, create_topic_page):
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(constants.BLOG)
        create_form.set_short_text(constants.SHORT_TEXT)
        create_form.set_main_text(constants.MAIN_TEXT)
        create_form.submit()
        return create_form

    def create_topic_without_short_text(self, create_topic_page):
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(constants.BLOG)
        create_form.set_title(constants.TITLE)
        create_form.set_main_text(constants.MAIN_TEXT)
        create_form.submit()
        return create_form

    def create_topic_without_main_text(self, create_topic_page):
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(constants.BLOG)
        create_form.set_title(constants.TITLE)
        create_form.set_short_text(constants.SHORT_TEXT)
        create_form.submit()
        return create_form

    def create_topic_with_so_long_limit(self, create_topic_page):
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(constants.BLOG)
        create_form.set_title(constants.LONG_TITLE)
        create_form.set_short_text(constants.SHORT_TEXT)
        create_form.set_main_text(constants.MAIN_TEXT)
        create_form.submit()
        return create_form

    def create_topic_with_bold_text(self, create_topic_page):
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(constants.BLOG)
        create_form.set_title(constants.TITLE)
        create_form.set_short_text(constants.SHORT_TEXT)
        create_form.set_main_text(constants.MAIN_TEXT)
        create_form.select_text(locator.MAIN_TEXT)
        CreateTopicForm(self.driver).set_bold_text(locator.BOLD_MAIN_TEXT)
        create_form.submit()
        return create_form

    def create_topic_with_bold_short_text(self, create_topic_page):
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(constants.BLOG)
        create_form.set_title(constants.TITLE)
        create_form.set_short_text(constants.SHORT_TEXT)
        create_form.set_main_text(constants.MAIN_TEXT)
        create_form.select_text(locator.SHORT_TEXT)
        CreateTopicForm(self.driver).set_bold_text(locator.BOLD_SHORT_TEXT)
        create_form.submit()
        return create_form

    def create_topic_with_italic_text(self, create_topic_page):
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(constants.BLOG)
        create_form.set_title(constants.TITLE)
        create_form.set_short_text(constants.SHORT_TEXT)
        create_form.set_main_text(constants.MAIN_TEXT)
        create_form.select_text(locator.MAIN_TEXT)
        CreateTopicForm(self.driver).set_italic_text(locator.ITALIC_MAIN_TEXT)
        create_form.submit()
        return create_form

    def create_topic_with_italic_short_text(self, create_topic_page):
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(constants.BLOG)
        create_form.set_title(constants.TITLE)
        create_form.set_short_text(constants.SHORT_TEXT)
        create_form.set_main_text(constants.MAIN_TEXT)
        create_form.select_text(locator.SHORT_TEXT)
        CreateTopicForm(self.driver).set_italic_text(locator.ITALIC_SHORT_TEXT)
        create_form.submit()
        return create_form
