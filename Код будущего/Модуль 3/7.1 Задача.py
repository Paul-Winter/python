# Функция login принимает:
# login_val - логин пользователя
# password_val - пароль пользователя
# is_correct - флаг (1 - верно, 0 - неверно)
# current_attempts - текущее число уже сделанных попыток

def login(login_val, password_val, is_correct, current_attempts):
    # Если попыток уже 3 или больше, ввод запрещен
    if current_attempts >= 3:
        return current_attempts, "Запрещено"
    if is_correct == 1:
    # Если вход верный, счетчик сбрасывается (или остается 0)
        return 0, "Разрешено"
    else:
    # Если вход неверный, увеличиваем счетчик
        new_attempts = current_attempts + 1
        status = "Разрешено" if new_attempts < 3 else "Запрещено"
        return new_attempts, status
