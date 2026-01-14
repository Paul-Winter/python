import os
import pandas as pd
from datetime import datetime

try:
    # 1.Загрузка
    if not os.path.exists("data"):
        print("Создана папка data. Поместите туда файлы данных")
    
    data_files = [f for f in os.listdir("data") if f.endswith(".csv")]
    if not data_files:
        print("В папке data нет CSV-файлов")
    
    df = pd.concat([pd.read_csv(f"data/{f}") for f in data_files])

    # 2.Фильтрация по дате
    start_date = input("Введите начальную дату (ГГГГ-ММ-ДД): ")
    end_date = input("Введите конечную дату (ГГГГ-ММ-ДД): ")

    df["Дата"] = pd.to_datetime(df["Дата"])
    mask = (df["Дата"] >= start_date) & (df["Дата"] <= end_date)
    filtered_df = df.loc[mask]

    # 3.Агрегирование
    report = filtered_df.groupby('Категория').agg({
        "Сумма": "sum",
        "Количество": "count"
    }).reset_index()

    # 4.Сохранение отчёта
    report.to_csv("report.csv", index=False)
    print("Отчёт успешно сгенерирован (report.csv)")

except Exception as e:
    print(f"Ошибка: {e}")
