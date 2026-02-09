import re
import requests
import urllib3

response = requests.get("https://httpbin.org/forms/post", verify=False)
pattern_field = r'<input '
fields = re.findall(pattern_field, response.text, re.IGNORECASE)
print(f'Итого полей: {len(fields)}')
