# Часто повторяющиеся уязвимости
# Отсортировать уязвимости по убыванию CVSS

# Требования:
# 1. Прочитать файл security.log.
# 2. В каждой строке найти уязвимость формата CVE-XXXX-YYYY
#    и её оценку CVSS в виде числа с точкой.
# 3. Собрать все найденные пары CVE и CVSS.
# 4. Если ни одной такой записи не найдено, вывести сообщение:
#    Нет уязвимостей.
# 5. Если записи есть, отсортировать их по убыванию значения CVSS (от большего к меньшему).
# 6. Записать отсортированные данные в файл sorted.log, по одной строке
#    в формате: CVE CVSS.
# 7. После успешной записи вывести сообщение: Готово.
# 8. Если файл security.log отсутствует, вывести сообщение:
#    Файл security.log не найден.
import re

src="security.log"
dst="sorted.log"

pattern = re.compile(r"(CVE-\d{4}-\d{4,7}).*?CVSS:(\d+\.\d+)")
vulns = []
try:
    with open(src, "r", encoding="utf-8") as f:
        for line in f:
            m = pattern.search(line)
            if m:
                cve = m.group(1)
                cvss = float(m.group(2))
                vulns.append((cve, cvss))
    if not vulns:
        print("Нет уязвимостей")    
    vulns.sort(key=lambda x: x[1], reverse=True)

    with open(dst, "w", encoding="utf-8") as out:
        for cve, cvss in vulns:
            out.write(f"{cve} {cvss}\n")
    print("Готово")
except FileNotFoundError:
    print(f"Файл {src} не найден")
