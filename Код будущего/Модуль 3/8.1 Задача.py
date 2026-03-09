import re

def validate_russian_email(email):
    pattern = r"^[A-Za-z0-9._-]+@([A-Za-z0-9А-Яа-яЁё._-]+\.(ru|su|рф))$"
    if re.match(pattern, email, re.IGNORECASE):
        return True, "Email корректен и относится к зоне RU/SU/РФ"
    else:
        return False, "Неверный формат или доменная зона не входит в пространство РФ"
