def prn_z(a):
    global b
    if b > 20:
        return
    print('*' * a)
    b = b + 10


b = 5
prn_z(b)
prn_z(b)
prn_z(b)

# def double(a):
#     return a*2


def double(x): return x*2


a = double(2)
a = double(a)
a = double(a)
print(a)


def multi(x, y): return x*y


print(multi(5, 5))
print(multi(y=12.8, x=10))


def greet(name='Guest', message='Hello, '):
    print(message + name)


greet()
greet('Ivan')
greet(message='GoodBye, ')
