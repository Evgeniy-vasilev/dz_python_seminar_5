# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random


def pvp(name):
    step = int(input(f'Ход {name}: '))
    while step < min or step > max:
        step = int(input(f'{name}, введите количество конфет от {min} до {max}: '))

    return step


def pve(step):
    step = k % (max + 1)
    if step < min:
        step = random.randint(min, max)

    return step


def remainder(name, k):
    print(f'После хода {name} осталось {k} конфет')


p_1 = input('Введите имя игрока: ')
p_2 = 'Bot'
k = int(input('Введите количество конфет: '))
min = int(input('Введите минимум конфет, которые можно взять за ход: '))
max = int(input('Введите максимум конфет, которые можно взять за ход: '))

first_step = random.randint(0, 2)
if first_step:
    print(f'Первый ходит {p_1}')
else:
    print(f'Первый ходит {p_2}')

while k > 0:
    if first_step:
        l = pvp(p_1)
        k -= l
        first_step = False
        remainder(p_1, k)
    else:
        l = pve(p_2)
        print(f'Ход Bot: {l}')
        k -= l
        first_step = True
        remainder(p_2, k)

if first_step == False:
    print(f'Победа {p_1}')
else:
    print(f'Победа {p_2}')
