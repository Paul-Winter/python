# Стеганография 
# Напишите программу, которая скрывает текст в изображении методом LSB (Least Significant Bit).

#### Пояснение к задаче
#  - Используйте библиотеки Pillow (для работы с изображениями) и numpy (для обработки данных)
#  - Используйте изображение cat.png (оно уже находится в рабочей папке программы)
#  - Текст для скрытия: "Hello world!".
#  - Каждый бит текста должен быть записан в младший бит (LSB) пикселей изображения (начиная с первого канала первого пикселя).
#  - Сохраните результат в файл secret_cat.png в формате PNG

from PIL import Image
import numpy as np

INPUT_IMAGE = "cat.png"
OUTPUT_IMAGE = "secret_cat.png"
SECRET_TEXT = "Hello world!"

try:
    # 1. Загружаем изображение
    img = Image.open(INPUT_IMAGE).convert('RGB')
    img_array = np.array(img, dtype=np.uint8) # Явно указываем тип

    # 2. Подготовка сообщения
    binary_message = ''.join(format(ord(c), '08b') for c in SECRET_TEXT) + '00000000'
    message_bits = np.array([int(bit) for bit in binary_message], dtype=np.uint8)

    # 3. Подготовка данных
    flat_img = img_array.flatten()

    if len(message_bits) > len(flat_img):
        print("Ошибка: Сообщение слишком длинное.")
    else:
        # 4. Внедрение LSB
        # Используем 254 (11111110), чтобы обнулить последний бит безопасно для uint8
        flat_img[:len(message_bits)] = (flat_img[:len(message_bits)] & 254) | message_bits

        # 5. Сохранение
        new_img_array = flat_img.reshape(img_array.shape)
        result_img = Image.fromarray(new_img_array)
        result_img.save(OUTPUT_IMAGE, "PNG")
        print(f"Готово! Сообщение скрыто в {OUTPUT_IMAGE}")

except FileNotFoundError:
    print(f"Ошибка: Файл {INPUT_IMAGE} не найден.")
except Exception as e:
    print(f"Ошибка при выполнении программы: {e}")
