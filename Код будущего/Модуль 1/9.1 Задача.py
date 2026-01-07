import math
import random
import datetime
import psutil
import os

a = 1.5
b = 5
print(math.pow(a, b))
print(math.sqrt(b))
print(math.isqrt(b))
print(math.sin(60))
print(math.exp(b))
print(2.71828**5)
print(math.log(b))
print(math.factorial(b))

list = [1,2,3,4,5,6,7,8]
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.choice(list))
print(random.choice(list))
print(random.choice(list))
print(random.choice(list))
print(random.sample(list,8))
print(random.sample(list,8))
print(random.sample(list,8))
print(random.sample(list,8))
print(random.sample(list,8))
random.shuffle(list)
print(list)

print(datetime.datetime.now())

# загрузка CPU (%)
cpu_usage = psutil.cpu_percent(interval=1)
# использование оперативной памяти
mem = psutil.virtual_memory()
# дисковая активность
disk = psutil.disk_usage('/')
# список процессов
processes = psutil.process_iter()
print(f"{cpu_usage}\n{mem}\n{disk}\n{processes}")

# работа с файлами и директориями
os.mkdir("folder")
os.rename("old.txt", "new.txt")
os.remove("file.txt")
# получение информации
current_dir = os.getcwd()
files = os.listdir()
# получить переменную окружения
path = os.getenv("PATH")