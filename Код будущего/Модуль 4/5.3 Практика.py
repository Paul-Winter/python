# Создайте скрипт, который временно отключает учётную запись пользователя
# (например, через usermod -L в Linux или net user в Windows)
# при обнаружении подозрительной активности (например, множественные неудачные попытки входа).

#### Пояснение к задаче
# 1. Импортируй необходимые модули
# 2. Создай глобальный словарь `blocked_user` для хранения заблокированных пользователей и времени разблокировки
# 3. Создай функцию `check_failure()` для анализа логов
# 4. Создай функцию `enable_user()` для разблокировки
# 5. Запусти бесконечный цикл мониторинга
# 6. Проверь и разблокируй пользователей
# 7. Проверь новые неудачные попытки
# 8. Сделай паузу

import subprocess
import re
import time
from datetime import datetime, timedelta

blocked_user = {}
def check_failure():
    log_file='C:\\Windows\\System32\\winevt\\Logs\\Security.log'
    user_attempts={}
    try:
        with open(log_file,'r', encoding='utf-8') as file:
            for line in file:
                if '4625' in line or "Failure" in line or 'неудач' in line:
                    if 'Account name:' in line:
                        parts=line.splite('Account name:')
                        if len(parts) > 1:
                            username=parts[1].split()[0].strip()
                            if username in user_attempts:
                                user_attempts[username]+=1
                            else:
                                user_attempts[username]=1
        for user, count in user_attempts.item():
            if count>5 and user not in blocked_user:
                return user
        return None
    except FileNotFoundError:
        return None
def enable_user(username):
    enable_cmd=f'net user {username} /active:yes'
    result = subprocess.run(enable_cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        del blocked_user[username]
while True:
    current_time=datetime.now()
    for username in list(blocked_user.keys()):
        if current_time>=blocked_user[username]:
            enable_user(username)
    warning_user=check_failure()
    if warning_user:
        disable_cmd=f'net user {username} /active:no'
        result = subprocess.run(disable_cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            blocked_user[warning_user]=datetime.now()+timedelta(minutes=60)
    time.sleep(60)
