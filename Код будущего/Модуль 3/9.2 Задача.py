# Напишите функции для кодирования [encode_to_base64(text)] и декодирования [decode_from_base64(b64_text)] строки в Base64. 

#### Пояснение к задаче
#  - Используйте стандартную библиотеку base64
#  - Так как библиотека base64 работает не со строками напрямую, а с байтами, необходимо использовать
# методы .encode() и .decode() для подготовки текста

import base64

def encode_to_base64(text):
    """Кодирует строку в формат Base64"""
    # 1. Переводим строку в байты (utf-8)
    text_bytes = text.encode('utf-8')

    # 2. Кодируем байты в base64-байты
    base64_bytes = base64.b64encode(text_bytes)

    # 3. Возвращаем результат как обычную строку
    return base64_bytes.decode('utf-8')

def decode_from_base64(b64_text):
    """Декодирует строку из формата Base64"""
    # 1. Переводим b64-строку в байты
    b64_bytes = b64_text.encode('utf-8')

    # 2. Декодируем из base64 в обычные байты
    original_bytes = base64.b64decode(b64_bytes)
    
    # 3. Возвращаем как строку
    return original_bytes.decode('utf-8')
