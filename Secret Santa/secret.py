import itertools
import random

# print(f"Билет №{random.randint(1, 25)} Вопрос №{random.randint(1,3)}")

# создаём список участников (дарителей)
values_dar = ["Павел", "Марина", "Юлия", "Олег", "Алексей"]
values_pol = values_dar

print(values_dar)

def shuffler(santas):
    random.shuffle(santas)
    return santas

for i in range (len(values_dar)):    
    shuffler(values_pol)
    if (values_pol[i] == values_dar[i]):
        shuffler(values_pol)

print(values_pol)

#secret_santas = 
# проверяем, чтобы ни один даритель не был получателем у самого себя
# перемешиваем его и получаем список получателей
# values_pol = list(itertools.combinations(values_dar, 2))
# print(values_pol)