import re

text = """fdslkfjsdlfjsdlk sdlfkj@mail.ru
dslkfjdslkfj 192.168.111.121 asdkfljdsl@gmail.com dlsfjldskfj; dkjfls
dslkfjdslf lkjfdslkfj 192.168.11.12 sdflkfjsdlk """

pattern_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2.}"
pattern_ip = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

emails = re.findall(pattern_email, text)
ips = re.findall(pattern_ip, text)

print("Найденные email-адреса:")
for m in emails:
    print(m)
print("Найденные IP-адреса:")
for a in ips:
    print(a)