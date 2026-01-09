# Найти все уязвимости с CVSS > 8
# Преобразовать данные (например, IP, CVE, CVSS) в CSV-таблицу
# Сохранить как report.csv
#
# 1. Прочитать CSV-файл vulnerabilities.csv.
# 2. Ожидается, что в файле есть колонки: IP, CVE, CVSS.
# 3. Для каждой строки проверить значение CVSS.
# 4. Отобрать только те строки, у которых CVSS больше 8.
# 5. Сохранить отобранные данные в новый CSV-файл report.csv
#    с теми же колонками: IP, CVE, CVSS.
# 6. В начале файла записать заголовки колонок.
# 7. После успешного сохранения вывести сообщение:
#    Отчёт сохранён в report.csv.
# 8. Если файл vulnerabilities.csv отсутствует, вывести сообщение:
#    Файл vulnerabilities.csv не найден.

import csv

input_file = "vulnerabilities.csv"
output_file = "report.csv"

try:
    with open(input_file, "r") as infile, open(output_file, "w", newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['IP', 'CVE', 'CVSS']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            try:
                cvss = float(row['CVSS'])
                if cvss > 8:
                    writer.writerow(row)
            except (ValueError, KeyError):
                continue
    print(f"Отчёт сохранён в {output_file}")
except FileNotFoundError:
    print(f"Файл {input_file} не найден")
