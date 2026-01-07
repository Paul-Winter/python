# print(c)
# prin("Hello")
# c = 2/0

while True:
    try:
        # raise IndexError()
        myfile = open("123.txt")
        a = int(input("Введите число: "))
        num = (int(input("Введите число: ")))/a
        b = 2
        c = '2'
        print(b+c)
        n = [1,2,3]
        a = 5/n[4]
    except ValueError:
        print("Это не целое число!")
    except ZeroDivisionError:
        print("Нельзя делить на ноль!")
    except TypeError:
        print('бесконечный цикл')
        break
    except IndexError:
        print('Обращение к элементу за пределами списка')
        break
    except FileNotFoundError:
        print('Файл не найден')
        break
    except:
        print("Неизвестная ошибка!")
        break
    else:
        break
        # print("Введено корректное число")
    finally:
        print("finally работает всегда")

try:
    print(num)
except NameError:
    print("Переменная num не определена")

print('123')