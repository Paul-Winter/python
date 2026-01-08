# Напишите программу, которя выводит топ-3 IP-адреса с наибольшим количеством
# уязвимостей на основе файла vulns.log

# Требования:
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# 7.
# 8.
# 9.
# 10.

from collections import Counter

def top3_ips(log_file="vulns.log"):
    try:
        ips = []
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if parts:
                    ips.append(parts[0])
        counter = Counter(ips)
        for ip, count in counter.most_common(3):
            print(f"{ip}: {count}")
    except FileNotFoundError:
        print(f"Файл {log_file} не найден")

if __name__ == "__main__":
    top3_ips()