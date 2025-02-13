from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from test_data import *
from locators import *
from conftest import *


gen_email = generate_email()
gen_password = generate_password()


class TestRegistration:

    # Проверяем, что значение поля Имя не пустое
    def test_registration_name_not_empty(self, registration):
        registration.find_element(*REG_NAME).send_keys(test_name)
        value_name = WebDriverWait(registration, 3).until(ec.presence_of_element_located(REG_NAME))
        assert value_name.get_attribute('value') != ""

    # Проверяем формат введенных данных в поле Email
    def test_registration_email_format(self, registration):
        registration.find_element(*EMAIL).send_keys(gen_email)
        email_input = WebDriverWait(registration, 3).until(ec.presence_of_element_located(EMAIL))
        value_email = email_input.get_attribute('value')
        # Вызываем функцию проверки валидного формата email (проверяем корректный формат логин@домен)
        assert valid_email(value_email)

    # Проверяем, отображение ошибки при вводе некорректного пароля (менее 6 символов)
    def test_registration_invalid_password(self, registration):
        registration.find_element(*REG_NAME).send_keys(test_name)
        registration.find_element(*EMAIL).send_keys(gen_email)
        registration.find_element(*PASSWORD).send_keys('12345')
        # Ожидаем ввод данных и кликаем на 'Зарегистрировать'
        WebDriverWait(registration, 3).until(ec.element_to_be_clickable(REGISTER)).click()
        # Ожидаем появление ошибки
        error = WebDriverWait(registration, 3).until(ec.visibility_of_element_located(ERROR_PASSWORD))
        assert error.text == 'Некорректный пароль'

    # Проверяем, что Регистрация отрабатывает успешно с корректными данными
    def test_registration_successful(self, registration):
        registration.find_element(*REG_NAME).send_keys(test_name)
        registration.find_element(*EMAIL).send_keys(gen_email)
        registration.find_element(*PASSWORD).send_keys(gen_password)
        # Ожидаем ввод данных и кликаем на 'Зарегистрировать'
        WebDriverWait(registration, 3).until(ec.element_to_be_clickable(REGISTER)).click()
        WebDriverWait(registration, 10).until(ec.url_to_be(PAGE_LOGIN))
        assert registration.current_url == PAGE_LOGIN
