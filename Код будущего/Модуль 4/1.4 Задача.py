# Выявите, какие IP-адреса из лог-файла log.txt находятся в черном списке blacklist.txt

#### Пояснения к задаче:
# - Откройте файл log.txt и дополнительный файл blacklist.txt
# - Уберите пустые строки и пробелы 
# - Используйте списки для хранения записей из файлов 
# - Найдите ip адреса и проверьте, находится ли они в blacklist
# 1. Читаем черный список в обычный список (list)

blacklist = []
with open("blacklist.txt", "r", encoding="utf-8") as f:
   for line in f:
       ip = line.strip()
       if ip:
           blacklist.append(ip)

# 2. Список для хранения найденных нарушителей (чтобы не дублировать вывод)
found_attackers = []

with open("log.txt", "r", encoding="utf-8") as file:
   for line in file:
       line = line.strip()
       if not line:
           continue
          
       # Извлекаем IP
       parts = line.split()
       current_ip = ""
       for part in parts:
           if part.startswith("IP:"):
               current_ip = part.replace("IP:", "")
               break
      
       # 3. Проверяем наличие IP в черном списке
       if current_ip in blacklist:
           # Проверяем, не добавляли ли мы этот IP уже ранее, чтобы не повторяться в выводе
           if current_ip not in found_attackers:
               found_attackers.append(current_ip)

# 4. Выводим результат
for bad_ip in found_attackers:
   print(f"ВНИМАНИЕ: Зафиксирована активность с IP из черного списка: {bad_ip}")
