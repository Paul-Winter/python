# Напишите класс ученика класса.
# Опишите в классе все возможные свойства, которые можно обобщить
# для каждого ученика, а также создать несколько методов.

# 1. Создать класс Student, который описывает ученика.
# 2. В конструкторе __init__ определить свойства: имя, возраст, класс
#    (например, 10А) и список оценок.
# 3. Создать метод add_mark, который добавляет оценку в список оценок.
# 4. Создать метод get_averate_mark, который возвращает среднюю оценку ученика
#    (если оценок нет, возвращать 0).
# 5. Создать метод get_info, который возвращает строку с информацией о ученике
#    в формате: имя, возраст, класс.
# 6. Класс должен содержать хотя бы один метод и хотя бы один атрибут экземпляра.
# 7. Не использовать запрещённые конструкции: import, eval, exec, subprocess.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = []
    
    def add_mark(self, mark):
        self.marks.append(mark)

    def get_average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)
    
    def get_info(self):
        return f"{self.name}, {self.age}, {self.grade}"
