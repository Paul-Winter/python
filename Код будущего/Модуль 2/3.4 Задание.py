# Прочитать файл и посчитать, какие CVE встречаются чаще всего

# Требования:
# 1. Открыть файл security.log (он уже будет создан системой).
# 2. Найти в каждой строке все упоминания CVE по такому виду:
#    CVE-XXXX-YYYY, где
#  - XXXX - это 4 цифры года,
#  - YYYY - это номер от 4 до 7 цифр.
# 3. Собрать все найденные CVE.
# 4. Если не найдено ни одного - вывести:
#    CVE не найдены.
# 5. Если они есть - нужно вывести ТОП-5 самых частых, по одной строке:
#    CVE:количество
#    Например:
#    CVE-2021-1111:3
# 6. Если файл security.log отсутствует вывести:
#    Файл security.log не найден.
from collections import Counter
import re

log_file="security.log"
cve_pattern = re.compile(r"CVE-\d{4}-\d{4,7}")
cve_list = []
try:
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            cve_list.extend(cve_pattern.findall(line))
    if not cve_list:
        print("CVE не найдены")
    counts = Counter(cve_list).most_common(5)
    for cve, count in counts:
        print(f"{cve}:{count}")
except FileNotFoundError:
    print(f"Файл {log_file} не найден")
