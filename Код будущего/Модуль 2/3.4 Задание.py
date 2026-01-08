# Прочитать файл и посчитать, какие CVE встречаются чаще всего

# Требования:
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
from collections import Counter
import re

def analyze_cve(log_file="security.log"):
    cve_pattern = re.compile(r"CVE-\d{4}-\d{4,7}")
    cve_list = []

    try:
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                cve_list.extend(cve_pattern.findall(line))
        if not cve_list:
            print("CVE не найдены")
            return
        counts = Counter(cve_list).most_common(5)

        for cve, count in counts:
            print(f"{cve}:{count}")
    except FileNotFoundError:
        print(f"Файл {log_file} не найден")

if __name__ == "__main__":
    analyze_cve()