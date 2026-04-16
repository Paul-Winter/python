# Создайте скрипт, который анализирует текстовый файл и строит гистограмму топ-10
# наиболее часто встречающихся слов.

#### Пояснение к задаче
# 1. Для подсчета используйте класс `Counter` из модуля `collections`,
#    а для построения графика библиотеку `matplotlib.pyplot`.
# 2. Текст для анализа находится в файле `text.txt` в кодировке `utf-8`
# 3. Избавьтесь от всех символов пунктуации (`.,!?;:-—()"'«»[]{}<>/\|@#$%^&*_+=<>`) тексте,
#    заменив их на пробелы: .
# 4. Приведите текст к нижнему регистру и разбейте его на отдельные слова 
# 5. Создайте объект `Counter` из списка слов для подсчета частоты встречаемости.
# 6. Извлеки 10 самых частых слов с помощью метода `most_common`.
# 7. Подготовьте для построения гистограммы два списка:
#    (1) список слов и (2) соответствующий им список количеств.
# 8. Постройте гистограмму:
#    - Установите размер графика
#    - Создайте столбчатую диаграмму (`plt.bar()`)
#    - Добавьте заголовок "Топ 10 слов"
#    - Подпишите оси: "Слова" (X) и "Количество" (Y)
# 10. Добавьте подписи значений над каждым столбцом.
# 11. Используйте автоматическую настройку отступов и отобразите график с помощью `plt.show()`

import matplotlib.pyplot as plt
from collections import Counter

def build_word_histogram(filename):
    # 3. Символы пунктуации
    punctuation = ".,!?;:-—()\"'«»[]{}<>/\|@#$%^&*_+=<>"
  
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
      
        # 4. Удаление пунктуации (замена на пробелы)
        for char in punctuation:
            text = text.replace(char, ' ')
      
        # 5. Нижний регистр и разбиение на слова
        words = text.lower().split()
      
        # 6. Подсчет частоты
        word_counts = Counter(words)
      
        # 7. Топ-10 слов
        top_10 = word_counts.most_common(10)
      
        # 8. Списки для графика
        labels, values = zip(*top_10) if top_10 else ([], [])
      
        # 9. Построение гистограммы
        plt.figure(figsize=(10, 6))
        bars = plt.bar(labels, values, color='skyblue')
      
        plt.title("Топ 10 слов")
        plt.xlabel("Слова")
        plt.ylabel("Количество")
      
        # 10. Подписи значений над столбцами
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, yval, ha='center', va='bottom')
      
        # 11. Настройка и показ
        plt.tight_layout()
        plt.show()
      
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    build_word_histogram("text.txt")
