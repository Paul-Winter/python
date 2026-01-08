# Создать новый файл с названием critical.log и перенести в него только
# те строки из security.log, где встречается слово Critical

# Требования:
# 1.
# 2.
# 3.
# 4.
# 5.

def extract_critical(src="security.log", dst="critical.log"):
    try:
        with open(src, "r", encoding="utf-8") as f:
            with open(dst, "w", encoding="utf-8") as out:
                for line in f:
                    if "Critical" in line:
                        out.write(line)
        print("Готово")
    except FileNotFoundError:
        print(f"Файл {src} не найден")

if __name__ == "__main__":
    extract_critical()