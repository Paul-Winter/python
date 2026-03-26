# На основе данных лог-файла log.txt выявите дни, в которые количество скачиваний увеличилось более чем в два раза по сравнению со вчерашним днем

#### Пояснения к задаче:
# - Откройте файл log
# - Найдите все скачивания (ACTION:DOWNLOAD) и выясните даты этих скачиваний
# - Создайте список дат и отсортируйте его
# - Для каждой даты сравните количество скачиваний с количеством в предыдущий день
# - Выведите на экран случаи, когда количество скачивания выросло более чем в 2 раза

# 1. Собираем статистику скачиваний по датам
daily_downloads = {}

with open("log.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
          
        # Ищем только скачивания
        if "ACTION:DOWNLOAD" in line:
            # Извлекаем дату (она находится в начале строки [YYYY-MM-DD])
            date = line[1:11]
            daily_downloads[date] = daily_downloads.get(date, 0) + 1

# 2. Получаем отсортированный список дат
sorted_dates = sorted(daily_downloads.keys())

# 3. Сравниваем количество с предыдущим днем
for i in range(1, len(sorted_dates)):
    current_day = sorted_dates[i]
    previous_day = sorted_dates[i-1]
  
    current_count = daily_downloads[current_day]
    previous_count = daily_downloads[previous_day]
  
    # Рост БОЛЕЕ чем в два раза (строгое неравенство)
    if current_count > (previous_count * 2):
        print(f"Всплеск активности! {current_day}: {current_count} (предыдущий день: {previous_count})")
