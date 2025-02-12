import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import time
from test_data import *
from locators import *
from conftest import *


class TestLogin:

    # Проверяем что, авторизация на странице Входа перенаправляет на Главную страницу
    def test_login_correct_email_and_password_show_main_page(self, login):
        login.find_element(*LOGIN_EMAIL).send_keys(test_email)
        login.find_element(*LOGIN_PASSWORD).send_keys(test_password)
        WebDriverWait(login, 3).until(ec.element_to_be_clickable(LOGIN_BUTTON))
        login.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(login, 3).until(ec.visibility_of_element_located(BUTTON_ORDER))
        assert login.current_url == main_page

    # Проверяем Вход по кнопке «Войти в аккаунт» (с Главной страницы), отображается страница Входа
    def test_login_on_main_page(self, login_to_account):
        login_to_account.find_element(*LOGIN_ACCOUNT).click()
        WebDriverWait(login_to_account, 3).until(ec.visibility_of_element_located(LOGIN_EMAIL))
        assert login_to_account.current_url == page_login

    # Проверяем вход по кнопке "Личный кабинет"
    def test_login_on_personal_account(self, login_to_account):
        login_to_account.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(login_to_account, 3).until(ec.visibility_of_element_located(LOGIN_EMAIL))
        assert login_to_account.current_url == page_login

    # # Проверяем вход через форму регистрации
    def test_login_from_register_form(self, login_to_account):
        login_to_account.find_element(*LOGIN_ACCOUNT).click()
        login_to_account.find_element(*BUTTON_ENTER_FROM_REG).click()
        WebDriverWait(login_to_account, 3).until(ec.visibility_of_element_located(LOGIN_EMAIL))
        assert login_to_account.current_url == page_login

    # # Проверяем вход через форму Восстановления пароля
    def test_login_from_password_recovery(self, login_to_account):
        login_to_account.find_element(*LOGIN_ACCOUNT).click()
        login_to_account.find_element(*BUTTON_PASSWORD_RECOVERY).click()
        login_to_account.find_element(*BUTTON_LOGIN_FROM_RECOVERY).click()
        WebDriverWait(login_to_account, 3).until(ec.visibility_of_element_located(LOGIN_EMAIL))
        assert login_to_account.current_url == page_login
