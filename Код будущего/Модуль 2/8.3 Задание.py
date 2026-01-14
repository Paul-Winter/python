import pandas as pd
from datetime import datetime, timedelta

def get_recent_logs(input_file="logs.csv", minutes=5):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return pd.DataFrame() # возвращаем пустой DataFrame
    
    if "timestamp" not in df.columns:
        print("Файл должен содержать колонку 'timestamp'")
        return pd.DataFrame()
    
    try:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
    except Exception:
        print("Не удалось преобразовать 'timestamp' в форматы даты/времени")
        return pd.DataFrame()
    
    now = datetime.now()
    cutoff = now - timedelta(minutes=minutes)
    recent_df = df[df["timestamp"] >= cutoff]
    print(f"Найдено {len(recent_df)} событий за последние {minutes} минут")
    return recent_df
