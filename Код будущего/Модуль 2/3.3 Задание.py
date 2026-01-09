# Создать новый файл с названием critical.log и перенести в него только
# те строки из security.log, где встречается слово Critical

# Требования:
# 1. Открыть файл security.log (он уже существует - его создаёт система).
# 2. Прочитать его построчно.
# 3. Каждый раз, когда в строке есть слово Critical,
#    записывать эту строку в новый файл critical.log.
# 4. Когда всё будет готово, вывести на экран сообщение: Готово.
# 5. Если файла security.log почему-то нет, нужно вывести сообщение:
#    Файл security.log не найден.

src="security.log"
dst="critical.log"
try:
    with open(src, "r", encoding="utf-8") as f:
        with open(dst, "w", encoding="utf-8") as out:
            for line in f:
                if "Critical" in line:
                    out.write(line)
    print("Готово")
except FileNotFoundError:
    print(f"Файл {src} не найден")
