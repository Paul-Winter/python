# Напишите функцию обработки формы задания логина и пароля login_set(username, password) так,
# чтобы проверялись параметры соответствия  логина и пароля заданным правилам сложности.

#### Пояснение к задаче
# Логин должен состоять из от 7 до 12 допустимых символов: буквы (a-z, A-Z), цифры (0-9), точка (.), дефис (-), подчеркивание (_)
# Пароль должен состоять из от 8 до 64 допустимых символов: букв (a-z, A-Z), цифры (0-9), знаки (.@#&-_) и отвечать следующим правилам:
#  - включать не менее 1 цифры
#  - включать не менее 1 знака (.@#&-_)
#  - включать не менее 1 заглавно буквы
# Возвращайте значение функции "ложь" (return False), если логин или пароль не соответствуют этим правилам и "истина" (return True), если все в порядке

import re

def login_set(username, password):
    # 1. Проверка логина (длина 7-12, допустимые символы)
    user_pattern = r"^[a-zA-Z0-9._-]{7,12}$"
    if not re.match(user_pattern, username):
        return False

    # 2. Проверка длины пароля (8-64) и допустимых символов
    # Допустимые знаки: . @ # & - _
    if not (8 <= len(password) <= 64):
        return False

    # Регулярное выражение для проверки состава символов пароля
    pass_pattern = r"^[a-zA-Z0-9.@#&-_]+$"
    if not re.match(pass_pattern, password):
        return False

    # 3. Проверка правил сложности пароля
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in ".@#&-_" for char in password)

    if not (has_digit and has_upper and has_special):
        return False

    # Если все условия пройдены
    return True
