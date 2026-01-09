# Реализовать класс и переопределить методы базовых математических операций
# (сложение, вычитание, умножение, деление),
# добавив туда выводы в консоль текущего действия.

# 1. Создать класс VerboseCalculator, который хранит числовое значение.
# 2. В конструкторе __init__ определить свойство value,
#    которое хранит текущее значение объекта.
# 3. Переопределить методы арифметических операций:
#    __add__, __sub__, __mul__, __truediv__.
# 4. В каждом методы перед выполнением операции выводить сообщение о текущем действии,
#    например: "Выполняется сложение", "Выполняется вычитание", "Выполняется умножение",
#    "Выполняется деление".
# 5. В методе деления предусмотреть проверку деления на ноль.
#    Если деление на ноль, вывести сообщение "Ошибка: деление на ноль" и
#    вернуть объект с value равным nan.
# 6. Методы должны возвращать новый объект класса VerboseCalculator с результатом операции.
# 7. Переопределить метод __str__, чтобы при выводе объекта отображалось его значение.
# 8. Не использовать запрещённые конструкции: import, eval, exec, subprocess.

class VerboseCalculator:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        print("Выполняется сложение")
        return VerboseCalculator(self.value + other.value)
    
    def __sub__(self, other):
        print("Выполняется вычитание")
        return VerboseCalculator(self.value - other.value)
    
    def __mul__(self, other):
        print("Выполняется умножение")
        return VerboseCalculator(self.value * other.value)
    
    def __truediv__(self, other):
        print("Выполняется деление")
        if other.value == 0:
            print("Ошибка: деление на ноль")
            return VerboseCalculator(float('nan'))
        return VerboseCalculator(self.value / other.value)
    
    def __str__(self):
        return str(self.value)
