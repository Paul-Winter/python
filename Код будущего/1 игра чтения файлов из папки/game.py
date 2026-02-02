import os

os.mkdir('Test')
files = os.listdir()
print(files)
os.remove('Test')
files = os.listdir()
print(files)