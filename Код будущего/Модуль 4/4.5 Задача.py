# В файле 5obfuscated_script.py находится Python-скрипт, который использует XOR-шифрование для сокрытия данных.
# Найдите в нём все присваивания переменной xor_key (шестнадцатеричные ключи) и все выражения с оператором XOR (^).

#### Пояснения к задаче
# 1. В текстовом файле 5obfuscated_script.py с помощью регулярных выражений найдите все строки, где переменной xor_key присваивается шестнадцатеричное значение.
# 2. Используя регулярные выражения найдите все выражения, содержащие оператор XOR (например, data[i] ^ key). Обратите внимание, что в паттерне нужно экранировать символ ^.
# Можно искать любые два операнда, разделённые пробелами и символом ^.
# 3. Выведите найденные ключи XOR и строки с XOR-операциями, чтобы увидеть, какие данные используются для расшифровки в обфусцированном скрипте.

import re
import os

def analyze_xor_obfuscation(filename):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Поиск присваивания xor_key (например: xor_key = 0xAF)
        # Ищем слово xor_key, пробелы, равно и hex-значение (0x + цифры/буквы A-F)
        key_pattern = r'xor_key\s*=\s*0x[0-9a-fA-F]+'
        keys_found = re.findall(key_pattern, content)

        # 2. Поиск операций XOR (например: a ^ b)
        # Ищем конструкцию: [что-то] ^ [что-то]
        # \^ — экранируем спецсимвол
        xor_op_pattern = r'\w+\[\w+\]\s*\^\s*\w+|\w+\s*\^\s*\w+'
        ops_found = re.findall(xor_op_pattern, content)

        # 3. Вывод результатов
        print("Найденные ключи XOR:")
        for key in keys_found:
            print(key)

        print("\nНайденные операции XOR:")
        for op in ops_found:
            print(op)

    except Exception as e:
        print(f"Ошибка при анализе: {e}")

if __name__ == "__main__":
    analyze_xor_obfuscation("5obfuscated_script.py")
