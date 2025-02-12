import pytest
from selenium import webdriver
from locators import *
from test_data import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as ec


# Фикстура открыть страницу регистрации, выполнить действия и закрыть браузер
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(page_registration)
    yield driver
    driver.quit()


#  Фикстура открыть страницу Входа, выполнить действия и закрыть браузер
@pytest.fixture
def login():
    driver = webdriver.Chrome()
    driver.get(page_login)
    yield driver
    driver.quit()


# Фикстура для авторизации из разных форм (переход на страницу входа из разных форм и авторизация)
@pytest.fixture()
def login_to_account():
    driver = webdriver.Chrome()
    driver.get(main_page)
    yield driver
    driver.find_element(*LOGIN_EMAIL).send_keys(test_email)
    driver.find_element(*LOGIN_PASSWORD).send_keys(test_password)
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LOGIN_BUTTON))
    driver.find_element(*LOGIN_BUTTON).click()
    driver.quit()


# Для авторизации на сайте
@pytest.fixture()
def authorization():
    driver = webdriver.Chrome()
    driver.get(page_login)
    driver.find_element(*LOGIN_EMAIL).send_keys(test_email)
    driver.find_element(*LOGIN_PASSWORD).send_keys(test_password)
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable(LOGIN_BUTTON))
    driver.find_element(*LOGIN_BUTTON).click()
    yield driver
    driver.quit()
