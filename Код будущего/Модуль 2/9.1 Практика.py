import pandas as pd
import glob
from datetime import datetime
import os

# загрузка и объединение CSV-файлов
all_files = glob.glob("data/*.csv")
df_list = [pd.read_csv(f) for f in all_files]
data = pd.concat(df_list)

# преобразуем строку в datetime
# отфильтровываем строки по дате
data['timestamp'] = pd.to_datetime(data['timestamp'])
target_day = '2025-06-13'
filtered = data[data['timestamp']].dt.date == datetime.strptime(target_day, "%Y-%m-%d").date()

# агрегация по уровню угроз
# считаем количество по каждой категории (CRITICAL, HIGH и т.д.)
# выделяем все уникальные системы
counts = filtered['severity'].value_counts().to_dict()
total = len(filtered)
systems = set(filtered['system'])

# формирование отчёта из шаблона
with open("report_template.txt", "r", encoding="utf-8") as f:
    template = f.read()

report = template.format(date = target_day,
    systems="\n".join(systems),
    critical=counts.get("CRITICAL", 0),
    high=counts.get("HIGH", 0),
    medium=counts.get("MEDIUM", 0),
    low = counts.get("LOW", 0),
    total = total
    )

# сохранение отчёта
os.makedirs("reports", exist_ok=True)
with open(f"reports/report_{target_day}.txt", "w", encoding="utf-8") as f:
    f.write(report)
