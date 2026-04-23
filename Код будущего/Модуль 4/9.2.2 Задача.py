# Напишите скрипт, который анализирует auth.log и ищет выполнение подозрительных команд. Выведите список таких команд с указанием пользователя и времени выполнения.

#### Пояснение к задаче
# 1. Логи для анализа находятся в файле `'auth.log'`.
# 2. К подозрительным командам мы будем относить следующий список: `['wget', 'curl', 'nmap', 'nc']`.
# 3. Для поиска записей в логе используйте регулярное выражение `r'(\w+\s+\d+\s+\d+:\d+:\d+).*?(\w+)\s*:.*?COMMAND=(.*?)(?:\s|$)'`
#    - Первая группа — время выполнения (месяц, день, время)
#    - Вторая группа — имя пользователя
#    - Третья группа — выполненная команда
# 4. Аналогично прошлой задаче, используйте `match.group` для извлечения соответствующей информации.
# 5. Для сравнения приводите все извлеченные имена команд к нижнему регистру.
# 6. Если подозрительная команда найдена, выведи результат в формате: `f'{time_str} | {user} | {command}'`, каждая команда должна быть выведена на отдельной строке.


import re

def analyze_suspicious_actions(filename):
    commands_warning = ['wget', 'curl', 'nmap', 'nc']
  
    # Исправленное регулярное выражение:
    # 1. Время
    # 2. Имя пользователя (ищем слово перед " : TTY=" или аналогичными маркерами sudo)
    # 3. Команда после COMMAND=
    log_pattern = r'(\w+\s+\d+\s+\d+:\d+:\d+).*?\s+(\w+)\s+:\s+.*?COMMAND=(.*)'
  
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
          
        for line in lines:
            match = re.search(log_pattern, line)
          
            if match:
                time_str = match.group(1)
                user = match.group(2)
                command = match.group(3).strip()
              
                for warning in commands_warning:
                    if warning in command.lower():
                        print(f"{time_str} | {user} | {command}")
                        break
                      
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")

if __name__ == "__main__":
    analyze_suspicious_actions('auth.log')
