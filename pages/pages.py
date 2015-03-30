# -*- coding:utf-8 -*-

import urlparse
from components import AuthForm, TopMenu

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


class AuthorizePage(PageObject):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)