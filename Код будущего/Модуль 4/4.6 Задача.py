# Проанализируйте  файл сетевого трафика 6traffic.pcap с помощью библиотеки scapy.
# Найдите HTTP-запросы к доменам из чёрного списка (malware.com, c2server.net, evil.org)
# и выведите информацию о таких запросах.

#### Пояснения к задаче:
# 1. Используйте функцию rdpcap из модуля scapy.all для чтения файла и классы TCP, IP для анализа слоев пакета.
# 2. Создайте список blacklist с доменами malware.com, c2server.net, evil.org.
# 3. Загрузите все пакеты из файла в переменную с помощью rdpcap().
# 4. Переберите каждый пакет в цикле.
#     - Проверьте, содержит ли пакет одновременно уровни IP и TCP (используйте метод .haslayer()).
#     - Извлеките полезную нагрузку (payload) из TCP-слоя. Чтобы работать с ней как с текстом, преобразуйте её в строку: str(packet[TCP].payload).
# 5. Поиск хоста:
#     - Проверьте, содержится ли в полезной нагрузке заголовок Host:
#     - Если заголовок найден, проверьте, есть ли в этой же строке любой домен из вашего blacklist (приведите текст к нижнему регистру для надежности).
# 6. Вывод результатов:
#     - При обнаружении совпадения выведите:
#     - Название подозрительного домена.
#     - IP-адрес назначения (dst), извлеченный из IP-слоя пакета.

from scapy.all import rdpcap, TCP, IP, Raw
import os

def analyze_traffic(filename):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return

    blacklist = ["malware.com", "c2server.net", "evil.org"]
  
    try:
        packets = rdpcap(filename)
        print(f"Анализ трафика в файле: {filename}")
        print("-" * 30)

        for pkt in packets:
            # Проверяем наличие слоев IP, TCP и сырых данных Raw
            if pkt.haslayer(TCP) and pkt.haslayer(Raw):
                # Извлекаем байты нагрузки и декодируем в текст
                payload = pkt[Raw].load.decode('utf-8', errors='ignore')
              
                if "Host:" in payload:
                    payload_lower = payload.lower()
                    for domain in blacklist:
                        if domain in payload_lower:
                            # Извлекаем IP из слоя IP
                            dest_ip = pkt[IP].dst if pkt.haslayer(IP) else "Unknown"
                            print(f"[!] ОБНАРУЖЕНА УГРОЗА: Запрос к {domain}")
                            print(f"    IP назначения: {dest_ip}")
                            print("-" * 20)
                          
    except Exception as e:
        print(f"Ошибка при анализе трафика: {e}")

if __name__ == "__main__":
    analyze_traffic("6traffic.pcap")
