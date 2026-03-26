# Проанализируйте лог-файл и найдите ситуации, в которых был введен неверный пароль 10 раз

#### Пояснения к задаче:
# - Считайте файл log.txt
# - Попытки входа фиксируются как ACTION:LOGIN
# - Ошибка во вводе пароля приводит к статусу STATUS:FAILED для этого действия
# - Считайте каждую строку и уберите лишние пробелы и пустые строки
# - Создайте счетчики входов, используя словарь 
# - Найдите все входы с неверным паролем и, используя метод get, посчитайте количество
# Словарь для накопления попыток. Ключ — IP, значение — счетчик.

attempts_counter = {}

# Открываем лог с явным указанием кодировки
with open("log.txt", "r", encoding="utf-8") as file:
   for line in file:
       line = line.strip()
       if not line:
           continue
      
       # СТРОГАЯ ПРОВЕРКА: только попытки ВХОДА и только со статусом ОШИБКА
       if "ACTION:LOGIN" in line and "STATUS:FAILED" in line:
           try:
               # Извлекаем IP-адрес из строки
               # Ищем элемент, который начинается на IP:
               parts = line.split()
               ip = ""
               for part in parts:
                   if part.startswith("IP:"):
                       ip = part.replace("IP:", "")
                       break
              
               # Если IP найден, увеличиваем его счетчик в словаре
               if ip:
                   attempts_counter[ip] = attempts_counter.get(ip, 0) + 1
           except Exception:
               continue

# Проверяем накопленные данные
for ip, count in attempts_counter.items():
   if count >= 10:
       print(f"ВНИМАНИЕ: Обнаружена атака методом перебора! IP: {ip}. Неудачных попыток входа: {count}")
