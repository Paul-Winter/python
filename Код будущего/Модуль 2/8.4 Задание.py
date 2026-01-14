from datetime import datetime

log_file = "app.log"
output_file = "filtered.log.txt"

try:
    start = input("Введите начало периода (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
    end = input("Введите конец периода (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")

    start_time = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")

    with open(log_file, "r") as infile:
        with open(output_file, "w") as outfile:
            for line in infile:
                if "ERROR" not in line:
                    continue
                try:
                    log_time_str = line.split()[0] + " " + line.split()[1]
                    log_time = datetime.strptime(log_time_str, "%Y-%m-%d %H:%M:%S")
                    if start_time <= log_time <= end_time:
                        outfile.write(line)
                except (IndexError, ValueError):
                    continue
    print(f"Отфильтрованные логи сохранены в {output_file}")

except FileNotFoundError:
    print(f"Файл {log_file} не найден")
except ValueError:
    print("Неверный формат даты. Используйте ГГГГ-ММ-ДД ЧЧ:ММ:СС")
