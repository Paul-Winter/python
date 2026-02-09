import re
import requests

path = "https://httpbin.org/"
response = requests.get(path)
text = response.text

pattern_link = r'href=["\'](.*?)["\']'
links = re.findall(pattern_link, text)
print("Найденные ссылки:")
for link in links:
    print(link)