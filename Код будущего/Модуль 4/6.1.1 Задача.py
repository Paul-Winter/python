# Создайте скрипт, который отправляет длинную строку в уязвимое приложение для проверки возможности возникновения переполнения буфера.

#### Пояснение к задаче
# 1. Импортируйте необходимый модуль для запуска внешних приложений и взаимодействия с ними.
# 2. Сформируйте длинную строку, состоящую из 5000 символов (например, можно 5000 раз повторить символ `'A'`).
# 3. Путь к исполняемому файлу уязвимого приложения этот каталог выполнения вашего скрипта (./vulnerable_app.exe).
# 4. Используй `subprocess.run()` и установи необходимые параметры
# 5. Обработай исключение `subprocess.TimeoutExpired`

import subprocess

long_s = 'A'*5000
app_path="C\\Program Files\\SomeApp\\vulnerable_app.exe"
try:
    result = subprocess.run(
        [app_path, long_s],
        capture_output=True,
        text=True,
        timeout=5
    )
    print(f'Код возврата: {result.returncode}')
    print(f'Вывод в консоль: {result.stdout[:200]}')
except subprocess.TimeoutExpired:
    print('Программа зависла, возможно переполнение буфера')

try:
    process=subprocess.Popen(
        app_path,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout,stderr = process.communicate(input=long_s,timeout=5)
    print(f'Код возврата: {process.returncode}')
    if stdout:
        print(f'Вывод в консоль: {stdout[:200]}')
    if stderr:
        print(f'Вывод в консоль: {stdout[:200]}')
except subprocess.TimeoutExpired:
    print('Программа зависла, возможно переполнение буфера')
    process.kill()
