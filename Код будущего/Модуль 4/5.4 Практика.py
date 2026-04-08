# Напишите скрипт, который отправляет уведомления в Telegram-бот при обнаружении критических событий (например, запуск подозрительного процесса или превышение порога загрузки системы).

#### Пояснение к задаче
# 1. Импортируй необходимые модули
# 2. Настрой параметры Telegram-бота
# 3. Создай функцию `send_tg()` для отправки сообщений
# 4. Запусти бесконечный цикл мониторинга
# 5. Проверь превышение порогового значения
# 6. Сделай паузу

import requests
import time
import psutil

bot_token='My_Key'
chat_id="My_chat"

def send_tg(message):
    url=f'https:/api.telegram.org/bot{bot_token}/sendMessage'
    params={
        'chat_id':chat_id,
        'text': message
    }
    response = requests.get(url,params=params)

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    memory=psutil.virtual_memory()
    memory_percent=memory.percent

    if cpu_percent >85:
        message=f'Внимание! Загрузка процессора достигла {cpu_percent}'
        send_tg(message)
    time.sleep(60)
