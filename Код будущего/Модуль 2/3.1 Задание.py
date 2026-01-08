# Напишите программу в файле, которая подсчитывает количество уязвимостей
# для каждого IP-адреса под данным из файла vulns.log

# Требования к программе:
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# 7.
# 8.
# 9.

def count_vulns(log_file="vulns.log"):
    counts = {}

    try:
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if not parts:
                    continue
                ip = parts[0]
                counts[ip] = counts.get(ip, 0) + 1
        
        for ip, total in counts.items():
            print(f"{ip}: {total}")
    except FileNotFoundError:
        print(f"Файл {log_file} не найден")

if __name__ == "__main__":
    count_vulns()