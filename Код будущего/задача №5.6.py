# Задача №5:
# В списке rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# замените Green на значение Зелёный, а элемент Violet на Фиолетовый

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(rainbow)
rainbow[rainbow.index('Green')] = 'Зелёный'
rainbow[rainbow.index('Violet')] = 'Фиолетовый'
print(rainbow)
