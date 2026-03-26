# На основе лог-файла log.txt узнайте, какое действие пользователь Алекс Иванов (имя пользователя в системе alex_ivanov) совершал чаще всего.

#### Пояснения к задаче:
# - Откройте файл log.txt и дополнительный файл blacklist.txt
# - Уберите пустые строки и пробелы 
# - По ключу USER:alex_ivanov выделите все записи, касающиеся пользователя
# - Используя переменную-счетчик, посчитайте каждый вид действий пользователя (ключ действий ACTION)
# - Найдите самое частое и выведите ответ на экран


# Словарь для подсчета действий Алекса Иванова
actions_stat = {}

with open("log.txt", "r", encoding="utf-8") as file:
   for line in file:
       line = line.strip()
       if not line:
           continue
          
       # 1. Фильтруем строки по пользователю alex_ivanov
       if "USER:alex_ivanov" in line:
           # 2. Извлекаем действие (ACTION:...)
           parts = line.split()
           current_action = ""
           for part in parts:
               if part.startswith("ACTION:"):
                   current_action = part.replace("ACTION:", "")
                   break
          
           # 3. Считаем частоту действий
           if current_action:
               actions_stat[current_action] = actions_stat.get(current_action, 0) + 1

# 4. Находим самое частое действие
most_common_action = ""
max_count = 0

for action, count in actions_stat.items():
   if count > max_count:
       max_count = count
       most_common_action = action

if most_common_action:
   print(f"Алекс Иванов чаще всего выполнял действие: {most_common_action} (количество: {max_count})")
