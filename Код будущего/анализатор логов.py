# Создать программу, которая анализируете строку с логами
# (записями о работе оборудования или сайта) и выводит полезную статистику.
#
# Программа должна:
# 1. Принимать строку с логами (например, из файла или ввода пользователя).
# 2. Анализировать записи и выводить:
#   * общее количество записей в логах;
#   * сколько раз встречается успешный ответ (код 200);
#   * сколько раз встречаются ошибки (коды 404 и 500);
#   * самый частый IP-адрес в логах и сколько раз он появляется.
#
# Пример логов:
# 192.168.1.1 - GET /index.html HTTP/1.1 200
# 192.168.1.2 - GET /error.html HTTP/1.1 404
# 192.168.1.1 - POST /data HTTP/1.1 500
# 192.168.1.1 - GET /image.png HTTP/1.1 200
# 192.168.1.1 - GET /style.css HTTP/1.1 200

# пример логов для проверки
logs = "192.168.1.1 - GET /index.html HTTP/1.1 200\n192.168.1.2 - GET /error.html HTTP/1.1 404\n192.168.1.1 - POST /data HTTP/1.1 500\n192.168.1.1 - GET /image.png HTTP/1.1 200\n192.168.1.1 - GET /style.css HTTP/1.1 200"

# производит анализ логов и вывод статистики


def logs_analyze(logs):
    strings = logs.strip().split('\n')

    # переменные для подсчёта количества
    status_200 = 0
    status_404 = 0
    status_500 = 0
    status_other = 0
    total_entries = 0
    ip_addresses = {}

    # разбиваем строку на части и извлекаем IP-адрес и код статуса
    for string in strings:
        if not string.strip():
            continue
        total_entries += 1
        parts = string.split()
        ip_address = parts[0]
        code_status = parts[-1]
        if not code_status.isdigit():
            continue

        # считаем IP-адреса с помощью словаря
        if ip_address in ip_addresses:
            ip_addresses[ip_address] += 1
        else:
            ip_addresses[ip_address] = 1

        # считаем коды статусов
        if code_status == '200':
            status_200 += 1
        elif code_status == '404':
            status_404 += 1
        elif code_status == '500':
            status_500 += 1
        else:
            status_other += 1

    # находим самый частый IP-адрес в логах и сколько раз он появляется
    popular_ip = 'неизвестен'
    popular_ip_count = 0
    for ip, ip_count in ip_addresses.items():
        if ip_count > popular_ip_count:
            popular_ip = ip
            popular_ip_count = ip_count

    # выводим результаты в консоль
    print('_' * 72)
    print('ПРОИЗВОДИМ АНАЛИЗ ЛОГОВ:')
    print('-' * 72)
    print(f'Всего записей: {total_entries}')
    print(f'Из них успешно (код 200): {status_200}')
    print(f'Из них с ошибкой (код 404): {status_404}')
    print(f'Из них с ошибкой (код 500): {status_500}')
    print(f'Из них другие: {status_other}')
    print('=' * 72)

# принимает логи от пользователя и выводит статистику


def logs_reader():
    print("Введите логи построчно:")
    logs = []
    while True:
        string = input()
        if string == "":
            break
        logs.append(string)
    logs_analyze("/n".join(logs))
