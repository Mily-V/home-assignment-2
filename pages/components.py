# -*- coding:utf-8 -*-

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import constants
import locator
import time

__author__ = 'Mily-V'

class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):

    def open_form(self):
        self.driver.find_element_by_xpath(locator.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(locator.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(locator.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(locator.ENTER_BUTTON).click()


class TopMenu(Component):

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(locator.USERNAME).text
        )



class TopicRead(Component):

    def error_create(self):
        return self.driver.find_element_by_class_name('system-message-error').is_displayed()

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(locator.TOPIC_TITLE_VIEW).text
        )

    def get_text(self, locator):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(locator).text
        )

    def open_blog(self):
        self.driver.find_element_by_xpath(locator.BLOG).click()

    def delete_topic(self):
        self.driver.find_element_by_xpath(locator.DELETE_BUTTON).click()
        self.driver.find_element_by_xpath(locator.DELETE_BUTTON_CONFIRM).click()

class CreateTopicForm(Component):

    def blog_select_open(self):
        self.driver.find_element_by_xpath(locator.BLOGSELECT).click()

    def blog_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(locator.OPTION.format(option_text)).click()

    def set_title(self, title):
        self.driver.find_element_by_xpath(locator.TITLE).send_keys(title)

    def set_short_text(self, short_text):
        short_text_field = self.driver.find_element_by_xpath(locator.SHORT_TEXT)
        action = ActionChains(self.driver)
        action.click(short_text_field)
        action.send_keys(short_text)
        action.perform()

    def set_main_text(self, main_text):
        main_text_field = self.driver.find_element_by_xpath(locator.MAIN_TEXT)
        action = ActionChains(self.driver)
        action.click(main_text_field)
        action.send_keys(main_text)
        action.perform()

    def submit(self):
        self.driver.find_element_by_xpath(locator.CREATE_BUTTON).click()


    def select_text(self, location):
        ActionChains(self.driver).\
            click(self.driver.find_element_by_xpath(location)).\
            key_down(Keys.CONTROL).\
            send_keys("a").\
            key_up(Keys.CONTROL).\
            perform()

    def set_bold_text(self, location):
        self.driver.find_element_by_xpath(location).click()

    def set_italic_text(self, location):
        self.driver.find_element_by_xpath(location).click()

    def set_quote_text(self, location):
        self.driver.find_element_by_xpath(location).click()

    def set_unordered_list_text(self, location):
        self.driver.find_element_by_xpath(location).click()

    def set_ordered_list_text(self, location):
        self.driver.find_element_by_xpath(location).click()

    def set_link_in_text(self, location):
        self.driver.find_element_by_xpath(location).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(constants.REFERENCE)
        alert.accept()

    def set_fix_image_in_text(self, location):
        self.driver.find_element_by_xpath(location).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(constants.FIX_IMAGE)
        alert.accept()

    # не получается
    def set_upload_image_in_text(self, location):
        self.driver.find_element_by_xpath(location).click()
        self.driver.find_element_by_xpath(locator.FORM_UPLOAD_LOCAL_IMAGE).\
            send_keys(constants.LOAD_IMAGE)
        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, locator.FORM_UPLOAD_LOCAL_IMAGE)))
        time.sleep(3)

