# Напишите функцию обработки формы ввода логина и пароля login_prepare(username, password) так,
# чтобы осуществлялась защита от SQL-инъекций и XSS-атак,
# а также после 3 попыток ввода неправильных данных обработка блокировалась на 10 секунд.

#### Пояснение к задаче
# Используйте опыт предыдущего урока, собрав вместе полученные знания.
# Защита от XSS осуществляется как валидацию значений.
# Допустимые символы для логина и пароля: буквы (a-z, A-Z), цифры (0-9), точки (.), дефисы (-), подчеркивания (_)
# защита от SQL-инъекций осуществляется методом “экранирования”
# Кроме этой функции, код больше ничего содержать не должен
# Пример объявления такой функции: generate_secure_query(username, password)
# Возвращайте в username, password обработанные безопасные логин и пароль,
# а также в значении функции "ложь" (return False),
# если нарушены условия (содержалась атака, не прошел валидацию, превышено число попыток)
# и истина (return True) если все в порядке. 

import re
import time

def login_prepare(username, password):
    # Инициализируем переменные для хранения состояния (только при первом запуске)
    if not hasattr(login_prepare, "attempts"):
        login_prepare.attempts = 0
        login_prepare.block_until = 0

    # 1. Проверка блокировки по времени
    current_time = time.time()
    if current_time < login_prepare.block_until:
        return False, username, password

    # 2. Валидация (Защита от XSS)
    # Разрешены: a-z, A-Z, 0-9, ., -, _
    pattern = r"^[a-zA-Z0-9._-]+$"

    if not re.match(pattern, username) or not re.match(pattern, password):
        login_prepare.attempts += 1
        # Если это 3-я ошибка — блокируем на 10 секунд
        if login_prepare.attempts >= 3:
            login_prepare.block_until = current_time + 10
            login_prepare.attempts = 0 # Сбрасываем счетчик для следующего цикла
        return False, username, password

    # 3. Экранирование (Защита от SQL-инъекций)
    # Удваиваем одинарные кавычки для SQL
    safe_username = username.replace("'", "''")
    safe_password = password.replace("'", "''")

    # Если всё успешно
    return True, safe_username, safe_password
