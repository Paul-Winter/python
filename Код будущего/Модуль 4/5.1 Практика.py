# Напишите скрипт на Python, который отслеживает загрузку процессора и памяти.
# Если загрузка CPU превышает 85 %, скрипт должен отправлять уведомление на email администратора.
# Используйте библиотеки psutil для сбора данных, smtplib и email.mime.text для формирования и отправки письма.

#### Пояснение к задаче
# Вам понадобятся библиотеки psutil, smtplib, MIMEText из email.mime.text, а также time.
# Настройте параметры SMTP-сервера (например, для Gmail):
# Адрес сервера: smtp.gmail.com
# Порт: 587
# Укажите email отправителя и пароль для аутентификации
# Укажите email получателя уведомлений
# Создайте бесконечный цикл мониторинга, который будет выполняться с интервалом 60 секунд.
# В цикле получите текущую загрузку CPU и процент использования памяти
# Если загрузка CPU превышает 85 %:
# Сформируйте текстовое сообщение о размере текущей загрузки
# Создайте объект MIMEText с этим сообщением.
# Добавьте заголовки письма: тему, отправителя и получателя.
# Установите соединение с SMTP-сервером, включите шифрование (starttls()), выполните вход и отправьте письмо.
# После проверки (и возможной отправки) приостановите выполнение программы на 60 секунд перед следующим измерением загрузки CPU.

import psutil
import smtplib
from email.mime.text import MIMEText
import time

smtp_server='smtp.gmail.com'
smtp_port=578
sender_email='your_email@gmail.com'
sender_password = 'password'
receiver_email='admin@gmail.com'

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    memory=psutil.virtual_memory()
    memory_percent=memory.percent

    if cpu_percent >85:
        message=f'Внимание! Загрузка процессора достигла {cpu_percent}'
        msg=MIMEText(message)
        msg['Subject']='Загрузка процессора'
        msg['From']=sender_email
        msg['To']=receiver_email
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server,quit
    time.sleep(60)
