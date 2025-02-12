from selenium.webdriver.common.by import By

# Форма Регистрации
page_registration = 'https://stellarburgers.nomoreparties.site/register'
REG_NAME = By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']"
EMAIL = By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']"
PASSWORD = By.NAME, "Пароль"
REGISTER = By.XPATH, ".//button[text()='Зарегистрироваться']"
ERROR_PASSWORD = By.XPATH, ".//p[contains(@class, 'input__error')]"
BUTTON_ENTER_FROM_REG = By.XPATH, ".//button[text()='Войти']"

# Форма Входа
page_login = 'https://stellarburgers.nomoreparties.site/login'
LOGIN_EMAIL = By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']"
LOGIN_ACCOUNT = By.XPATH, ".//button[text()='Войти в аккаунт']"
LOGIN_PASSWORD = By.XPATH, ".//input[@type='password' and @name='Пароль']"
LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']"
HEADER_LOGIN = By.XPATH, "//h2[text()='Вход']"

# Восстановление пароля
page_password_recovery = 'https://stellarburgers.nomoreparties.site/forgot-password'
BUTTON_PASSWORD_RECOVERY = By.CLASS_NAME, "Auth_link__1fOlj"
BUTTON_LOGIN_FROM_RECOVERY = By.XPATH, ".//p/a[text()='Войти']"

# Страница Личный кабинет
page_profile = 'https://stellarburgers.nomoreparties.site/account/profile'
BUTTON_PERSONAL_ACCOUNT = By.PARTIAL_LINK_TEXT, "Личный Кабинет"

# Главная страница StellarBurgers
main_page = 'https://stellarburgers.nomoreparties.site/'
BUTTON_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"

# Переход в конструктор
BUTTON_CONSTRUCTOR = By.PARTIAL_LINK_TEXT, "Конструктор"
BURGER_TITLE = By.XPATH, ".//section[1]/h1[text()='Соберите бургер']"

# Форма конструктора
SAUCES_BUTTON = By.XPATH, ".//span[text()='Соусы']/parent::*"
HEADER_SAUCES = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"
FILLINGS_BUTTON = By.XPATH, ".//span[text()='Начинки']/parent::*"
HEADER_FILLINGS = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"
BUN_BUTTON = (By.XPATH, ".//span[text()='Булки']/parent::*")
HEADER_BUN = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"


# Логотип StellarBurger
LOGO = By.TAG_NAME, "svg"

# Кнопка Выход (в Личном кабинете)
BUTTON_EXIT = By.XPATH, ".//button[text()='Выход']"



