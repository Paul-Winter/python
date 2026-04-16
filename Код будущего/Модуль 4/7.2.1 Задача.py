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

from collections import Counter
import matplotlib.pyplot as plt

with open ('text.txt', 'r', encoding='utf-8') as file:
    text=file.read()
punctuatian = '.,!?;:-—()"\'«»[]{}<>/\\|@#$%^&*_+=<>'
for char in punctuatian:
    text = text.replace(char, ' ')

words=text.lower().split()
word_count = Counter(words)
top_words = word_count.most_common(10)
word_list = [item[0] for item in top_words]
count_list = [item[1] for item in top_words]
plt.figure(figsize=(10,6))
plt.bar(word_list,count_list,color="blue")
plt.title("Топ 10 слов", fontsize=16)
plt.xlabel('Слова', fontsize=12)
plt.ylabel('Количество', fontsize=12)
for i, (word,count) in enumerate(zip(word_list, count_list)):
    plt.text(i, count+0.5, str(count), ha='center', va='bottom',fontsize=10)

plt.tight_layout()
plt.show()
