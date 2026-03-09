# Напишите rsa_operations(message) функцию, которая создает пару RSA-ключей и зашифровывает ими сообщение.

#### Пояснение к задаче
# Для реализации функции используйте библиотеку PyCryptodome.
# Написанная функция должна возвращать оба созданных ключа и зашифрованное сообщение (private_key, public_key, encrypted_message)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_operations(message):
    """
    Генерирует ключи RSA и зашифровывает сообщение.
    Возвращает (private_key, public_key, encrypted_message)
    """
    # 1. Генерируем пару ключей (длина 2048 бит — стандарт безопасности)
    key = RSA.generate(2048)
    private_key = key.export_key() # Закрытый ключ
    public_key = key.publickey().export_key() # Открытый ключ

    # 2. Подготавливаем сообщение (переводим в байты)
    data = message.encode('utf-8')

    # 3. Шифруем с помощью ПУБЛИЧНОГО ключа
    # Используем объект ключа для создания шифратора
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted_message = cipher_rsa.encrypt(data)

    return private_key, public_key, encrypted_message
