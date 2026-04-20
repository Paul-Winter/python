# Создайте скрипт, который анализирует конфигурационный файл Nginx и проверяет,
# отключена ли директива `server_tokens` (защита от утечки версии веб-сервера).

#### Пояснение к задаче
# 1. Импортируйте модуль `re` для работы с регулярными выражениями.
# 2. Откройте файл `'4/4.8/nginx.conf'` в режиме чтения с кодировкой `utf-8`.
# 3. Прочитайте всё содержимое файла с помощью `read()` и сохраните в переменную `config_content`.
# 4. С помощью `re.search()` найдите в конфигурации директиву `server_tokens`.
# Используйте регулярное выражение `r'server_tokens\s+(\w+);'` с флагом `re.IGNORECASE` для поиска без учета регистра.
#    - `server_tokens` — название директивы
#    - `\s+` — один или более пробельных символов
#    - `(\w+)` — захватывающая группа для значения (off, on и т.д.)
#    - `;` — завершение директивы
# 5. Проверьте, найдена ли директива:
#    - Если директива не найдена (`server_token_match` равен `None`), выведи сообщение: `'server_tokens не найден'`
# 6. Если директива найдена, извлеките значение с помощью `group(1)`.
# 7. Приведите значение к нижнему регистру с помощью `lower()` и проверьте:
#    - Если значение равно `'off'`, выведи сообщение: `'server_tokens отключен'`
#    - Иначе выведите сообщение: `'server_tokens включен'`


import re
with open('4/4.8/nginx.conf', 'r' , encoding='utf-8') as file:
    config_content = file.read()
server_token_match = re.search(r'server_tokens\s+(\w+);', config_content,re.IGNORECASE)
if not server_token_match:
    print('server_tokens не найден')
else:
    token_value = server_token_match.group(1)
    if token_value.lower() == 'off':
        print('server_tokens отключен')
    else:
        print('server_tokens включен')
