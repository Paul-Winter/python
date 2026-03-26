# Визуализируйте количество событий по времени (на каждый час) из лог-файла log.txt, построив гистограмму с помощью текстовых символов. 

#### Пояснения к задаче:
# - Используйте словарь для подсчета событий
# - Извлеките время событий
# - Создайте список и для каждого события добавьте час и количество событий в этот час
# - Сделайте сортировку по ключу 
# - Создайте текст с анализом активности по часам
# - Постройте гистограмму, представленную горизонтальными полосками, состоящими из символов *

# 1. Создаем пустой словарь для накопления статистики
hourly_stats = {}

with open("log.txt", "r", encoding="utf-8") as file:
   for line in file:
       line = line.strip()
       # Пропускаем пустые строки или слишком короткие записи
       if not line or len(line) < 15:
           continue
          
       try:
           # Время в логе находится в формате [YYYY-MM-DD HH:MM:SS]
           # Извлекаем часы (символы с 12 по 14 индекс)
           hour = line[12:14]
          
           if hour.isdigit():
               # Используем метод get: если часа еще нет в словаре, берем 0 и прибавляем 1
               hourly_stats[hour] = hourly_stats.get(hour, 0) + 1
       except:
           continue

# 2. Сортируем ключи (часы), чтобы гистограмма шла по порядку от 00 до 23
sorted_hours = sorted(hourly_stats.keys())

# 3. Проходим по отсортированным часам и рисуем график
for hour in sorted_hours:
   count = hourly_stats[hour]
   # Визуализируем количество событий с помощью символа '*'
   bar = "*" * count
   print(f"{hour}:00 | {bar} ({count})")


with open('4/4.1/log.txt', 'r', encoding='utf-8') as file:
    lines=file.readlines()
    hour_activity={}

    for line in lines:
        time_str=line[12:20]
        hour=int(time_str.split(':')[0])
        hour_activity[hour]=hour_activity.get(hour,0)+1
    activity_list=[]
    for hour,count in hour_activity.items():
        activity_list.append([hour,count])

    activity_list = sorted(activity_list, key=lambda x: x[0])

    print('Активность по часам:')
    for hour, count in activity_list:
        bar='█'*count
        print(f"{hour:02d}" + bar)
