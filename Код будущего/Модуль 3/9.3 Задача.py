# Напишите функцию hash_password(password) для хэширования пароля с добавлением случайной соли с использованием
# библиотеки hashlib и метода os.urandom для генерации соли,
# а также функцию check_password(stored_hash, stored_salt, provided_password) для проверки соответствия пароля и его хэша.

#### Пояснение к задаче
# Напомним, что солью называется случайная строка (набор байтов),
# которая добавляется к паролю перед хэшированием для того, чтобы сделать хэш более защищённым.
#  - Так как библиотека base64 работает не со строками напрямую, а с байтами,
# необходимо использовать методы .encode() и .decode() для подготовки текста
#  - Функция hash_password(password) должна вернуть хеш и соль в hex-формате для удобства хранения
#  - Функция check_password(stored_hash, stored_salt, provided_password) должна логическое значение Истина (True)
# если проверка прошла успешно, либо Ложь (False), если нет.

import hashlib
import os

def hash_password(password):
    """Генерирует соль и хеширует пароль."""
    # Генерируем соль (16 байт)
    salt = os.urandom(16)

    # Хешируем: сначала соль, потом пароль
    hash_obj = hashlib.sha256()
    hash_obj.update(salt)
    hash_obj.update(password.encode('utf-8'))

    # Возвращаем хеш и соль в hex-формате для удобства хранения
    return hash_obj.hexdigest(), salt.hex()

def check_password(stored_hash, stored_salt, provided_password):
    """Проверяет, соответствует ли введенный пароль сохраненному хешу."""
    # 1. Превращаем hex-соль обратно в байты
    salt_bytes = bytes.fromhex(stored_salt)

    # 2. Хешируем введенный пароль с ТЕМ ЖЕ самым значением соли
    hash_obj = hashlib.sha256()
    hash_obj.update(salt_bytes)
    hash_obj.update(provided_password.encode('utf-8'))

    # 3. Сравниваем полученный хеш с тем, что хранится в базе
    return hash_obj.hexdigest() == stored_hash
