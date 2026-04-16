# Создайте скрипт, который анализирует файл веб-лога и находит User-Agent,
# встречающиеся чаще заданного порога.

#### Пояснение к задаче
# 1. Импортируйте необходимые библиотеки
# 2. Задайте пороговое значение (например, `5`) для количества вхождений User-Agent,
#    при превышении которого, он считается подозрительным
# 3. Воспользуйтесь файлом лога `access.log` для решения этой задачи
# 4. Создайте пустой список для хранения User-Agent
# 6. Для каждой строки выполните следующие действия:
#    - Проверьте наличие символа `'"'` в строке
#    - Разделите строку по символу `'"'`
#    - Извлеки предпоследний элемент (это User-Agent)
#    - Если User-Agent существует и не является пустой строкой, добавьте его в список
# 7. Создайте объект `Counter` из списка User-Agent для подсчета частоты встречаемости
# 8. Переберите элементы счетчика. Если количество вхождений превышает заданный порог,
#    выведите сообщение в формате: `"{User-Agent}: встречается {количество} раз"`
# 9. Если ни один User-Agent не превысил порог, выведи сообщение:
#    `"Аномального поведения не найдено"`.

from collections import Counter

def analyze_logs(filename):
    # 2. Пороговое значение
    threshold = 5
    user_agents = []

    try:
        # 3. Открываем файл
        with open(filename, 'r', encoding='utf-8') as file:
            # 4. Читаем строки
            for line in file:
                # 6. Извлекаем User-Agent
                if '"' in line:
                    parts = line.split('"')
                    # User-Agent обычно находится в предпоследней части (между кавычками)
                    if len(parts) >= 2:
                        ua = parts[-2].strip()
                        if ua:
                            user_agents.append(ua)

        # 7. Подсчет частоты
        ua_counts = Counter(user_agents)
      
        found_anomaly = False
        # 8. Проверка порога
        for ua, count in ua_counts.items():
            if count > threshold:
                print(f"{ua}: встречается {count} раз")
                found_anomaly = True
      
        # 9. Если ничего не нашли
        if not found_anomaly:
            print("Аномального поведения не найдено")

    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    analyze_logs("access.log")
