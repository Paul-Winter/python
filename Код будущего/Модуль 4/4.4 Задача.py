# Функции IsDebuggerPresent и NtQueryInformationProcess часто используются вредоносным ПО для проверки, выполняется ли программа под отладчиком.
# Найдите вызовы этих функций в файле 4malware.exe 

#### Пояснения к задаче:
# Откройте файл 4malware.exe в бинарном режиме и прочитайте всё содержимое.
# Декодируйте бинарные данные в строку с помощью кодировки Latin-1 (а не UTF-8), игнорируя все возможные ошибки декодирования.
# Latin-1 отображает каждый байт в символ, что позволяет прочитать любые байты как текст, включая названия функций.
# В отличие от предыдущих задач, здесь мы не ищем текстовые строки в UTF-8, а используем Latin-1, чтобы гарантированно найти имена функций, которые могут быть разбросаны по бинарному файлу.
# Выведите полученную строку для визуального просмотра.
# Создайте список функций ["IsDebuggerPresent", "NtQueryInformationProcess"].
# Для каждой функции проверьте, содержится ли она в полученной строке (оператор in).
# Если функция найдена, выведите сообщение об её обнаружении.

import os

def check_anti_debug(filename):
    anti_debug_functions = ["IsDebuggerPresent", "NtQueryInformationProcess"]
  
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден в текущей директории.")
        return

    try:
        # Читаем как "сырые" байты
        with open(filename, "rb") as f:
            data = f.read()
          
        # Декодируем каждый байт в символ Latin-1 (0-255)
        # Это позволяет искать текст внутри бинарного потока
        content = data.decode('latin-1', errors='ignore')

        print(f"Анализ файла: {filename}")
        for func in anti_debug_functions:
            if func in content:
                print(f"ВНИМАНИЕ: Найдена функция {func}")
            else:
                print(f"Функция {func} не обнаружена")
              
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

if __name__ == "__main__":
    check_anti_debug("4malware.exe")
