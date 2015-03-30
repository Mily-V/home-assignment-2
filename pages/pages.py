# -*- coding:utf-8 -*-

import urlparse
from components import AuthForm, TopMenu, CreateForm, Topic

__author__ = 'Mily-V'

class PageObject(object):

    BASE_URL = 'http://ftest.stud.tech-mail.ru'
    PATH     = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def login(self):
        auth_page = AuthorizePage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login("ftest15@tech-mail.ru")
        auth_form.set_password("Pa$$w0rD-15")
        auth_form.submit()

    def create_topic(self, blog, title, short_test, main_text):
        create_topic_page = CreateTopicPage(self.driver)
        create_topic_page.open()
        create_form = create_topic_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(blog)
        create_form.set_title(title)
        create_form.set_short_text(short_test)
        create_form.set_main_text(main_text)
        create_form.submit()




class AuthorizePage(PageObject):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)


class CreateTopicPage(PageObject):
    PATH = '/blog/topic/create/'

    @property
    def form(self):
        return CreateForm(self.driver)


class TopicPage(PageObject):
    @property
    def topic(self):
        return Topic(self.driver)
