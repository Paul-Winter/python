# Напишите скрипт, который автоматически блокирует IP-адреса в файрволе
# (например, через iptables в Linux или netsh в Windows) после нескольких неудачных попыток входа.

#### Пояснение к задаче
# 1. Импортируй необходимые модули
# 2. Создай функцию `check_failure()` для анализа логов
# 3. Запусти бесконечный цикл мониторинга
#    - Вызови функцию `check_failure()` для получения текущих данных
# 4. Проверь IP-адреса на превышение лимита
#    - Для каждого IP, у которого количество попыток больше 5
# 5. Заблокируй подозрительные IP
# 6. Сделай паузу

import re
import time
import subprocess

def check_failure():
    log_file='C:\\Windows\\System32\\winevt\\Logs\\Security.log'
    failed={}
    try:
        with open(log_file,'r', encoding='utf-8') as file:
            for line in file:
                if '4625' in line or "Failure" in line or 'неудач' in line:
                    ip_pattern=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                    ips = re.findall(ip_pattern, line)
                    for ip in ips:
                        if ip in failed:
                            failed[ip]+=1
                        else:
                            failed[ip]=1
        return failed
    except FileNotFoundError:
        print('Файл логов не найден')
        return {}

while True:
    attemps=check_failure()
    for ip,count in attemps.items():
        if count>5:
            rule_name=f'Block_{ip}'
            check_cmd=f'netsh advfirewall feriwall show rule name="{rule_name}"'
            if rule_name not in subprocess.getoutput(check_cmd):
                block_cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=block remoteip={ip}'
                result=subprocess.run(block_cmd, shell=True, capture_output=True, text=True)
    time.sleep(60)
