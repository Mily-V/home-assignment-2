# -*- coding:utf-8 -*-

__author__ = 'milya'

# форма авторизации
LOGIN        = '//input[@name="login"]'
PASSWORD     = '//input[@name="password"]'
ENTER_BUTTON = '//span[text()="Войти"]'
LOGIN_BUTTON = '//a[text()="Вход для участников"]'

# главная страница авторизированного пользователя. Верхнее меню
USERNAME     = '//a[@class="username"]'

# просмотр  и редактирование топика
TOPIC_TITLE_VIEW        = '//*[@class="topic-title"]/a'
TEXT_TAG                = '//*[@class="topic-content text"]/p'
BLOG                    = '//*[@class="topic-blog"]'
DELETE_BUTTON           = '//a[@class="actions-delete"]'
DELETE_BUTTON_CONFIRM   = '//input[@value="Удалить"]'
BOLD_TAG                = '(//*[@class="topic-content text"])[1]/p/strong'
ITALIC_TAG              = '(//*[@class="topic-content text"])[1]/p/em'
UNORDERED_LIST_TAG      = '(//*[@class="topic-content text"])[1]/p/ul'
ORDERED_LIST_TAG        = '(//*[@class="topic-content text"])[1]/p/ol'
IMAGE_TAG               = '(//*[@class="topic-content text"])[1]/p/img'
LINK_TAG                = '/(//*[@class="topic-content text"])[1]/p/a'

# форма создания топика
BLOGSELECT      = '//a[@class="chzn-single"]'
OPTION          = '//li[text()="{}"]'
TITLE           = '//input[@name="title"]'
SHORT_TEXT      = '(//*[@class="CodeMirror-scroll"])[1]'
MAIN_TEXT       = '(//*[@class="CodeMirror-scroll"])[2]'
CREATE_BUTTON   = '//button[contains(text(),"Создать")]'

# всякие кнопочки на форме создания топика
BOLD_MAIN_TEXT      = '(//*[@class="markdown-editor-icon-bold"])[2]'
BOLD_SHORT_TEXT     = '(//*[@class="markdown-editor-icon-bold"])[1]'
ITALIC_MAIN_TEXT    = '(//*[@class="markdown-editor-icon-italic"])[2]'
ITALIC_SHORT_TEXT   = '(//*[@class="markdown-editor-icon-italic"])[1]'
QUOTE_MAIN_TEXT     = '(//*[@class="markdown-editor-icon-quote"])[2]'
QUOTE_SHORT_TEXT    = '(//*[@class="markdown-editor-icon-quote"])[1]'
LINK_MAIN_TEXT      = '(//*[@class="markdown-editor-icon-link"])[3]'
LINK_SHORT_TEXT     = '(//*[@class="markdown-editor-icon-link"])[1]'
UNORDERED_LIST_MAIN_TEXT    = '(//*[@class="markdown-editor-icon-unordered-list"])[2]'
UNORDERED_LIST_SHORT_TEXT   = '(//*[@class="markdown-editor-icon-unordered-list"])[1]'
ORDERED_LIST_MAIN_TEXT      = '(//*[@class="markdown-editor-icon-ordered-list"])[2]'
ORDERED_LIST_SHORT_TEXT     = '(//*[@class="markdown-editor-icon-ordered-list"])[1]'
FIX_IMAGE_MAIN_TEXT     = '(//*[@class="markdown-editor-icon-image"])[3]'
FIX_IMAGE_SHORT_TEXT    = '(//*[@class="markdown-editor-icon-image"])[1]'
UPLOAD_IMAGE_MAIN_TEXT  = '(//*[@class="markdown-editor-icon-image"])[4]'
UPLOAD_IMAGE_SHORT_TEXT = '(//*[@class="markdown-editor-icon-image"])[2]'
FORM_UPLOAD_LOCAL_IMAGE = '(//*[@name="filedata"])[2]'