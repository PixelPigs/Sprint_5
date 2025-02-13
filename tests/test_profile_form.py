from conftest import *


class TestProfile:

    # Проверяем переход в Личный кабинет
    def test_go_to_personal_account(self, authorization):
        WebDriverWait(authorization, 3).until(ec.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT))
        authorization.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
        # Ждем что урл будет содержать "profile"
        WebDriverWait(authorization, 5).until(expected_conditions.url_contains("profile"))
        assert authorization.current_url == PAGE_PROFILE

    # Проверяем переход из Личного кабинета в конструктор
    def test_go_to_constructor_from_account(self, authorization):
        WebDriverWait(authorization, 3).until(ec.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT))
        authorization.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(authorization, 5).until(ec.url_contains("profile"))
        WebDriverWait(authorization, 3).until(ec.element_to_be_clickable(BUTTON_CONSTRUCTOR))
        authorization.find_element(*BUTTON_CONSTRUCTOR).click()
        WebDriverWait(authorization, 3).until(ec.visibility_of_element_located(BURGER_TITLE))
        assert authorization.current_url == MAIN_PAGE

    # Проверяем из Личного кабинета по клику на Конструктор и на логотип
    def test_click_logo_from_account(self, authorization):
        WebDriverWait(authorization, 3).until(ec.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT))
        authorization.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(authorization, 5).until(ec.url_contains("profile"))
        WebDriverWait(authorization, 3).until(ec.element_to_be_clickable(LOGO))
        authorization.find_element(*LOGO).click()
        assert authorization.current_url == MAIN_PAGE

    # Проверяем Выход из Личного кабинета
    def test_click_exit_from_personal_account(self, authorization):
        authorization.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(authorization, 5).until(ec.url_contains("profile"))
        WebDriverWait(authorization, 3).until(ec.element_to_be_clickable(BUTTON_EXIT))
        authorization.find_element(*BUTTON_EXIT).click()
        WebDriverWait(authorization, 3).until(ec.presence_of_element_located(HEADER_LOGIN))
        assert authorization.current_url == PAGE_LOGIN
