# фильтрация логов по уровню:
# - прочитать лог log.txt
# - сохранить только строки с уровнями ERROR и WARNING в errors.txt

import os
os.chdir("C:\\Users\\Student\\python\\Код будущего\\test")

def filter_logs(input_file="log.txt", output_file="errors.txt"):
    try:
        with open(input_file, 'r', encoding="utf-8") as infile:
            with open(output_file, 'w', encoding="utf-8") as outfile:
                for line in infile:
                    if "ERROR" in line or "WARNING" in line:
                        outfile.write(line)
        print(f"Логи отфильтрованы. Результат в {output_file}")
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")

# вызов функции
filter_logs()