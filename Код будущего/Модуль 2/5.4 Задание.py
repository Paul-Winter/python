# Реализуйте класс для хранения результатов анализа файла vulnreport.json

# 1. Созжать класс VulnReport, который хранит результаты анализа файла vulnreport.json.
# 2. В конструкторе __init__ загрузить данные из JSON-файла и сохранить их в атрибут data.
# 3. Если файла нет, вывести сообщение: Файл vulnreport.json не найден.
# 4. Если файл не является корректным JSON, вывести сообщение:
#    Ошибка чтения JSON файла.
# 5. Реализовать метод count_vulnerabilities, который возвращает количество уязвимостей в данных.
# 6. Реализовать метод list_ips, который возвращает список всех IP-адресов, если они есть в данных.
# 7. Реализовать метод highest_cvss, который возвращает запись с самой высокой оценкой CVSS.
# 8. Класс должен содержать хотя бы один атрибут и хотя бы один метод.
# 9. Не использовать запрещённые конструкции: eval, exec, subprocess.

import json

class VulnReport:
    def __init__(self, data_file="vulnreport.json"):
        """Загружает JSON-файл и хранит данные"""
        self.data = []
        try:
            with open(data_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"Файл {data_file} не найден")
        except json.JSONDecodeError:
            print("Ошибка чтения JSON файла")
    
    def count_vulnerabilities(self):
        """Возвращает количество уязвимостей"""
        return len(self.data)
    
    def list_ips(self):
        """Возвращает список всех IP, если они есть"""
        result = []
        for item in self.data:
            ip = item.get("ip") or item.get("IP") or item.get("address")
            if ip:
                result.append(ip)
        return result
    
    def highest_cvss(self):
        """Возвращает уязвимость с самым высоким CVSS"""
        highest = None
        max_score = -1
        for item in self.data:
            cvss = float(item.get("cvss", -1))
            if cvss > max_score:
                max_score = cvss
                highest = item
        return highest
