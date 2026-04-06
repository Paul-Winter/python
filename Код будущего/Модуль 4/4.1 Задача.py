# Напишите скрипт, который извлекает из файла  1malware.exe  текстовые строки и находит подозрительные паттерны: URL-адреса, IP-адреса из внутренних диапазонов и команды запуска cmd.exe или powershell.

#### Пояснения к задаче:
# Импортируйте модуль re для работы с регулярными выражениями.
# Используйте функцию dop.extract_strings(filename), чтобы получить все текстовые строки из исполняемого файла.
# Эта функция возвращает список строк.
# Объедините полученные строки в один текст, разделяя их символом перевода строки \n, чтобы упростить поиск.
# С помощью re.findall() найдите:
# URL-адреса, начинающиеся с http:// или https://
# IP-адреса из диапазонов 192.168. и 10.0..
# Команды cmd.exe или powershell. 
# Выведите найденные списки на экран (URL, IP, команды).

import re
import dop

def analyze_malware(filename):
    # 1. Извлекаем строки из файла
    strings_list = dop.extract_strings(filename)
  
    # 2. Объединяем в один текст для удобного поиска через re
    full_text = "\n".join(strings_list)
  
    # 3. Поиск паттернов
    # URL: http или https
    urls = re.findall(r'https?://[^\s<>"]+', full_text)
  
    # Внутренние IP: 192.168.x.x или 10.0.x.x
    # Используем упрощенный паттерн по условию задачи
    ips = re.findall(r'(?:192\.168\.|10\.0\.)\d{1,3}\.\d{1,3}', full_text)
  
    # Команды запуска
    commands = re.findall(r'(?:cmd\.exe|powershell(?:\.exe)?)', full_text, re.IGNORECASE)
  
    # 4. Вывод результатов
    print("Подозрительные URL:")
    print(urls)
  
    print("\nПодозрительные IP:")
    print(ips)
  
    print("\nКоманды запуска:")
    print(commands)

if __name__ == "__main__":
    analyze_malware("1malware.exe")
