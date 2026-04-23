# Напишите программу, которая рекурсивно сканирует директорию и выводит список файлов,
# изменённых за последние 24 часа, с их метаданными (дата создания, изменения, размер).

#### Пояснение к задаче
# 1. Импортируй необходимые модули:
#    - `os` для работы с файловой системой
#    - `datetime` из `datetime` для работы с датой и временем
# 2. Задай путь для сканирования: `'4/4.9/3.test_dir'` и сохрани его в переменную `scan_path`.
# 3. Получи текущее время с помощью `datetime.now()` и сохрани в переменную `current_time`.
# 4. Вычисли время 24 часа назад с помощью `timedelta(hours=24)` и сохрани в переменную `time_24h_ago`.
# 5. Используй функцию `os.walk(scan_path)` для рекурсивного обхода директории:
#    - Функция возвращает кортежи `(root, dirs, files)` для каждого каталога
#    - `root` — текущий путь к каталогу
#    - `dirs` — список подкаталогов в текущем каталоге
#    - `files` — список файлов в текущем каталоге
# 6. С помощью вложенного цикла `for` перебери все файлы в текущем каталоге.
# 7. Сформируй полный путь к файлу с помощью `os.path.join(root, file)`.
# 8. Получи метаданные файла с помощью `os.stat(file_path)` и сохрани в переменную `file_stat`.
# 9. Извлеки время последнего изменения файла: `file_stat.st_mtime` и преобразуй его в объект `datetime` с помощью `datetime.fromtimestamp()`.
# 10. Проверь, было ли изменение файла в течение последних 24 часов: если `mod_time >= time_24h_ago`.
# 11. Если условие выполнено:
#     - Извлеки время создания файла с помощью `file_stat.st_ctime` и преобразуй в `datetime`
#     - Извлеки размер файла с помощью `file_stat.st_size`
#     - Выведи информацию в формате: `f'{file_path} | Создан: {create_time} | Размер: {size} | Изменен: {mod_time}'`


import os
from datetime import datetime, timedelta

scan_path = '4/4.9/3.test_dir'
current_time = datetime.now()
time_24h_ago = current_time-timedelta(hours=24)
for root,dirs,files in os.walk(scan_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_stat = os.stat(file_path)
        mod_time = datetime.fromtimestamp(file_stat.st_mtime)
        if mod_time >= time_24h_ago:
            create_time = datetime.fromtimestamp(file_stat.st_ctime)
            size=file_stat.st_size
            print(f'{file_path} | Создан: {create_time} | Размер: {size} | Изменен: {mod_time}')
