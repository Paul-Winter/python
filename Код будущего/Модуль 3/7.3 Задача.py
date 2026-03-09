import re

def validate_pizza_order(name, email, phone, delivery_time, size, toppings, comment):
    text_pattern = r"^[A-Za-zА-Яа-яЁё\s]+$"
    if not re.match(text_pattern, name):
        return False, "Недопустимые символы в имени"
    if not re.match(text_pattern, comment):
        return False, "Недопустимые символы в комментарии"
    
    email_pattern = r"^[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+$"
    if not re.match(email_pattern, email):
        return False, "Неверный формат почты"
    if not re.match(r"^\d+$", phone):
        return False, "Телефон должен содержать только цифры"
    
    time_pattern = r"^([01]\d|2[0-3]):[0-5]\d$"
    if not re.match(time_pattern, delivery_time):
        return False, "Неверный формат времени (НН:ММ)"
    
    allow_sizes = ["small", "medium", "large"]
    if size not in allow_sizes:
        return False, "Выбран недопустимый размер"
    
    allow_toppings = ["bacon", "cheese", "onion", "mushroom"]
    if not isinstance(toppings, list):
        return False, "Топпинги должны быть переданы списком"
    for topping in toppings:
        if topping not in allow_toppings:
            return False, f"Недопустимый ингредиент {topping}"
    
    return True, "Данные проверены"
