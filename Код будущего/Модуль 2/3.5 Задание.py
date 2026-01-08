# Отсортировать уязвимости по убыванию CVSS

# Требования:
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# 7.
# 8.
import re

def sort_by_cvss(src="security.log", dst="sorted.log"):
    pattern = re.compile(r"(CVE-\d{4}-\d{4,7}).*?CVSS: (\d+\.\d+)")

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
            return
        
        vulns.sort(key=lambda x: x[1], reverse=True)

        with open(dst, "w", encoding="utf-8") as out:
            for cve, cvss in vulns:
                out.write(f"{cve} {cvss}\n")
        print("Готово")
    except FileNotFoundError:
        print(f"Файл {src} не найден")

if __name__ == "__main__":
    sort_by_cvss()