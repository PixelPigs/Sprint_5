import random
import string
import re


# Генерируем корректный email (логин, номер когорты и три цифры)
def generate_email(domain="ya.ru"):
    length_login = random.randint(5, 13)
    login = ''.join(random.choices(string.ascii_lowercase, k=length_login))
    cohort_number = random.randint(1, 10)
    random_number = random.randint(100, 1000)
    return f"{login}{cohort_number}{random_number}@{domain}"


# Генерируем корректный пароль (минимально символов 6)
def generate_password():
    length_password = random.randint(6, 21)
    password = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=length_password))
    return password


# Функция проверки формата email
def valid_email(email):
    return bool(re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email))


# Тестовые данные для формы регистрации/авторизации
test_name = 'Ольга'
test_email = 'boichenkoolga8112@ya.ru'
test_password = "123456"
