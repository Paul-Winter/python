import random

stack_1 = random.randint(2,10)
stack_2 = random.randint(2,10)

select = 0
taken = 0

current_player = 'Игрок'

def take(stack, num):
    global taken
    if current_player == 'Компьютер':
        taken = random.randint(1, stack)
    print(current_player + ' взял ' + str(taken) + ' камней из ' + str(num) + ' кучки')
    stack = stack - taken
    return(stack)

def result():
    print('Камней в 1 кучке: ' + str(stack_1))
    print('Камней в 2 кучке: ' + str(stack_2))
    if stack_1 == 0 and stack_2 == 0:
        print('Игра окончена, победил ' + current_player)
        exit()

def take_computer():
    global stack_1, stack_2, current_player
    if stack_1 == 0:
        stack_2 = take(stack_2, 2)
    elif stack_2 == 0:
        stack_1 = take(stack_1, 1)
    else:
        choice = random.randint(1,2)
        if choice == 1:
            stack_1 = take(stack_1, 1)
        else:
            stack_2 = take(stack_2, 2)

result()

while True:
    if current_player == 'Компьютер':
        take_computer()
        result()
        current_player = 'Игрок'
    else:
        select = int(input('Выберите кучку: '))
        taken = int(input('Сколько камней забрать: '))
        if select == 1:
            stack_1 = take(stack_1, 1)
        else:
            stack_2 = take(stack_2, 2)
        result()
        current_player = 'Компьютер'