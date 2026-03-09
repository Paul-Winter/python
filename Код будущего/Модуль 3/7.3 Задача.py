# Напишите  функцию validate_pizza_order, получающую данные формы https://httpbin.org/forms/post и осуществляющую защиту от атаки типа XSS.

#### Пояснение к задаче
# Защита от XSS осуществляется как валидацию значений
# Проверка должна включать:
#  - имя и комментарий должны состоять только из букв
#  - телефон должен состоять только из цифр
#  - время должно быть в формате HH:MM и иметь реальный диапазон значений
# не забудьте проверить корректность полей, в котором пользователь осуществляет выбор вариантов (checkbox и radio buttons) – вдруг злоумышленник сумел их подменить
# Используйте регулярные выражения, они могут сильно упростить проверки таких вещей, как email, время или телефон
# Формат объявления такой функции: validate_pizza_order(name, email, phone, delivery_time, size, toppings, comment)
# Возвращайте значение "ложь", если данные не прошли валидацию (return False) и истина (return True), если прошли

import re

def validate_pizza_order(name, email, phone, delivery_time, size, toppings, comment):
    """
    Комплексная проверка безопасности формы заказа пиццы.
    """
    # 1. Текстовые поля (Защита от XSS: только буквы и пробелы)
    text_pattern = r"^[A-Za-zА-Яа-яЁё\s]+$"
    if not re.match(text_pattern, name):
        return False, "Недопустимые символы в имени"
    if not re.match(text_pattern, comment):
        return False, "Недопустимые символы в комментарии"
    
    # 2. Контактные данные (Строгая валидация формата)
    email_pattern = r"^[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+$"
    if not re.match(email_pattern, email):
        return False, "Неверный формат почты"
    if not re.match(r"^\d+$", phone):
        return False, "Телефон должен содержать только цифры"
    
    # 3. Время доставки (Защита формата HH:MM)
    # Часы 00-23, минуты 00-59
    time_pattern = r"^([01]\d|2[0-3]):[0-5]\d$"
    if not re.match(time_pattern, delivery_time):
        return False, "Неверный формат времени (НН:ММ)"
    
    # 4. Размер пиццы (Белый список для Radio buttons)
    allow_sizes = ["small", "medium", "large"]
    if size not in allow_sizes:
        return False, "Выбран недопустимый размер"
    
    # 5. Топпинги (Белый список для Checkboxes)
    allow_toppings = ["bacon", "cheese", "onion", "mushroom"]
    if not isinstance(toppings, list):
        return False, "Топпинги должны быть переданы списком"
    for topping in toppings:
        if topping not in allow_toppings:
            return False, f"Недопустимый ингредиент {topping}"
    
    return True, "Данные проверены"
