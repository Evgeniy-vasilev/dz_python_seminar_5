# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def pvp(name):
    step = int(input(f'Ход {name}: '))
    while step < min or step > max:
        step = int(input(f'{name}, введите количество конфет от {min} до {max}: '))

    return step


def remainder(name, k):
    print(f'После хода {name} осталось {k} конфет')


p_1 = input('Введите имя первого игрока: ')
p_2 = input('Введите имя второго игрока: ')
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
        l = pvp(p_2)
        k -= l
        first_step = True
        remainder(p_2, k)

if first_step == False:
    print(f'Победа {p_1}')
else:
    print(f'Победа {p_2}')