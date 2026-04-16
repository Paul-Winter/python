# Создайте скрипт, который обнаруживает аномалии командах bash и находит команды,
# выполняемые чаще среднего значения.

#### Пояснение к задаче
# 1. Для подсчета используйте уже знакомый класс `Counter` из модуля `collections`
# 2. Историю команд прочитайте из файла bash_history.txt в список `command`,
#    выполняя следующие действия:
#    - В каждой прочитанной строке удалите пробелы
#    - Если строка останется не пустой, то добавьте её в список команд 
# 3. Создайте объект `Counter` из списка команд для подсчета частоты встречаемости каждой команды.
# 4. Вычислите общее количество команд (`len(command)`).
# 5. Вычислите количество уникальных команд (`len(cmd_counter)`).
# 6. Рассчитайте среднее значение встречаемости команд:
#    `общее количество / количество уникальных команд`.
# 7. Выведите среднее значение в формате: `"Среднее {average}"`.
# 8. Переберите элементы счетчика. Если количество вхождений команды превышает среднее значение,
#    выведите сообщение в формате: `"Комманда {cmd} встречается чаще среднего, а именно {count} раз"`.

from collections import Counter

def analyze_bash_history(filename):
    commands = []
  
    try:
        # 2. Чтение истории команд
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Удаляем пробелы по краям
                cmd = line.strip()
                if cmd:
                    commands.append(cmd)
      
        if not commands:
            print("История команд пуста.")
            return

        # 3. Подсчет частоты
        cmd_counter = Counter(commands)
      
        # 4. Общее количество команд
        total_count = len(commands)
      
        # 5. Количество уникальных команд
        unique_count = len(cmd_counter)
      
        # 6. Среднее значение
        average = total_count / unique_count
      
        # 7. Вывод среднего
        print(f"Среднее {average}")
      
        # 8. Поиск аномалий
        for cmd, count in cmd_counter.items():
            if count > average:
                print(f"Комманда {cmd} встречается чаще среднего, а именно {count} раз")
              
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")

if __name__ == "__main__":
    analyze_bash_history("bash_history.txt")
