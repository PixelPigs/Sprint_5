from conftest import *


class TestConstructor:

    # Проверяем переход в Соусы
    def test_from_constructor_click_sauces(self, authorization):
        authorization.find_element(*BUTTON_CONSTRUCTOR).click()
        authorization.find_element(*SAUCES_BUTTON).click()
        elm_sauces = authorization.find_element(*HEADER_SAUCES)
        assert elm_sauces.text == 'Соусы'

    # Проверяем переход в Начинки
    def test_from_constructor_click_fillings(self, authorization):
        authorization.find_element(*BUTTON_CONSTRUCTOR).click()
        authorization.find_element(*FILLINGS_BUTTON).click()
        elm_fillings = authorization.find_element(*HEADER_FILLINGS)
        assert elm_fillings.text == 'Начинки'

    # Проверяем переход в Начинки
    def test_from_constructor_click_bun(self, authorization):
        authorization.find_element(*BUTTON_CONSTRUCTOR).click()
        authorization.find_element(*FILLINGS_BUTTON).click()
        authorization.find_element(*BUN_BUTTON).click()
        elm_fillings = authorization.find_element(*HEADER_BUN)
        assert elm_fillings.text == 'Булки'
