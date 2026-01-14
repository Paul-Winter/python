from datetime import datetime

def date_difference(date1: str, date2: str) -> int:
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2-d1).days)
    except ValueError:
        print("Неправильный формат даты. Используйте 'YYYY-MM-DD'.")
        return None