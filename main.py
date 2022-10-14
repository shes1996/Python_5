# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_string = 'абв напр опалоабв оапио абврн аыом'

my_list = list(filter(lambda x: 'абв' not in x, my_string.split()))

print(' '.join(my_list))

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint

bonbon = 221


def count_bon(player, maxbon, bonbon):
    while True:
        bon1 = int(input(f'Игрок {player} берет конфеты, '
                         f'введите количество конфет(1 - {maxbon} шт)'))
        if 0 < bon1 <= maxbon:
            bonbon -= bon1
            break
        else:
            print('Неправильно, попробуй... ещё... раз')
    return bonbon


def bon_player_vs_player(bonbon: int):
    money = randint(1, 2)
    player1 = input('Введите имя первого игрока ')
    player2 = input('Введите имя второго игрока ')
    if money != 1:
        player1, player2 = player2, player1
    maxbon = 28
    while bonbon > 0:
        bonbon = count_bon(player1, maxbon, bonbon)
        print(f'Осталось конфет: ', bonbon)
        if bonbon < maxbon:
            maxbon = bonbon
        if bonbon == 0:
            print(f'Поздравляю, игрок {player2}, Вы выиграли!')
        player1, player2 = player2, player1


# bon_player_vs_player(bonbon)


def bon_player_vs_bot(bonbon: int):
    money = randint(1, 2)
    player1 = input('Введите имя игрока ')
    player2 = 'Челик'
    if money != 1:
        player1, player2 = player2, player1
    maxbon = 28
    while bonbon > 0:
        if player1 == 'Челик':
            bonbot = randint(1, maxbon)
            print(f'Бот {player1} берет конфеты: {bonbot}')
            bonbon -= bonbot
        else:
            bonbon = count_bon(player1, maxbon, bonbon)
        print(f'Осталось конфет: ', bonbon)
        if bonbon < maxbon:
            maxbon = bonbon
        if bonbon == 0:
            if player1 != 'Челик':
                print(f'Поздравляю, игрок {player1}, Вы выиграли!')
            else:
                print(f'Увы и Ах! Выиграл {player1}!')
        player1, player2 = player2, player1


# bon_player_vs_bot(bonbon)

def bon_player_vs_smart_bot(bonbon: int):
    money = randint(1, 2)
    player1 = input('Введите имя игрока ')
    player2 = 'Ботан'
    if money != 1:
        player1, player2 = player2, player1
    maxbon = 28
    while bonbon > 0:
        if player1 == 'Ботан':
            if bonbon > 57 or bonbon == 29:
                bonbot = randint(1, maxbon)
            elif 29 < bonbon <= 57:
                bonbot = bonbon - 29
            else:
                bonbot = bonbon
            print(f'Бот {player1} берет конфеты: {bonbot}')
            bonbon -= bonbot
        else:
            bonbon = count_bon(player1, maxbon, bonbon)
        print(f'Осталось конфет: ', bonbon)
        if bonbon < maxbon:
            maxbon = bonbon
        if bonbon == 0:
            if player1 != 'Ботан':
                print(f'Поздравляю, игрок {player1}, Вы выиграли!')
            else:
                print(f'Увы и Ах! Выиграл {player1}!')
        player1, player2 = player2, player1

#bon_player_vs_smart_bot(bonbon)

# Создайте программу для игры в ""Крестики-нолики"".

def zeroes_win(cross_zeroes):
    zeroes = ['0', '0', '0']
    if zeroes in cross_zeroes:
        return True
    elif cross_zeroes[0] == cross_zeroes[4] == cross_zeroes[8] == '0':
        return True
    elif cross_zeroes[2] == cross_zeroes[4] == cross_zeroes[6] == '0':
        return True
    for i in range(3):
        if cross_zeroes[i] == cross_zeroes[i+3] == cross_zeroes[i+6] == '0':
            return True
    for i in range(0, 7, 3):
        if cross_zeroes[i] == cross_zeroes[i+1] == cross_zeroes[i+2] == '0':
            return True
    return False

def crosses_win(cross_zeroes):
    crosses = ['x', 'x', 'x']
    if crosses in cross_zeroes:
        return True
    elif cross_zeroes[0] == cross_zeroes[4] == cross_zeroes[8] == 'x':
        return True
    elif cross_zeroes[2] == cross_zeroes[4] == cross_zeroes[6] == 'x':
        return True
    for i in range(3):
        if cross_zeroes[i] == cross_zeroes[i+3] == cross_zeroes[i+6] == 'x':
            return True
    for i in range(0, 7, 3):
        if cross_zeroes[i] == cross_zeroes[i+1] == cross_zeroes[i+2] == 'x':
            return True
    return False
crosses_zeroes= ['1', '2', '3',
               '4','5','6',
               '7','8','9']


def cross_zero(crosses_zeroes):
    print(*crosses_zeroes[0:3])
    print(*crosses_zeroes[3:6])
    print(*crosses_zeroes[6:9])
    player1 = '0'
    player2 = 'x'
    print('Первыми ходят "Нолики"')
    while True:
        while True:
            step = input('Введите номер клетки ')
            if int(step) in range(1, 10) and crosses_zeroes[int(step) - 1] != '0' and crosses_zeroes[int(step) - 1] != 'x':
                for i in range(0, 9):
                    if step in crosses_zeroes[i]:
                        x = crosses_zeroes[i].index(step)
                        crosses_zeroes[i] = player1
                break
            else:
                print('Либо клетка занята, либо её не существует')
        if zeroes_win(crosses_zeroes):
            print('Нолики выиграли')
            print(*crosses_zeroes[0:3])
            print(*crosses_zeroes[3:6])
            print(*crosses_zeroes[6:9])
            break
        if crosses_win(crosses_zeroes):
            print('Крестики выиграли')
            print(*crosses_zeroes[0:3])
            print(*crosses_zeroes[3:6])
            print(*crosses_zeroes[6:9])
            break
        player1, player2 = player2, player1
        print(*crosses_zeroes[0:3])
        print(*crosses_zeroes[3:6])
        print(*crosses_zeroes[6:9])

#cross_zero(crosses_zeroes)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

my_str = 'wwwaaammmmm'
def rle(my_str):
    out_str = ''
    count = 1
    for i in range(len(my_str)-1):
        if i <= len(my_str):
            if my_str[i] == my_str[i + 1]:
                count += 1
            else:
                a = my_str[i]
                print(count, my_str[i])
                count = 1
    print(count, my_str[i])

rle(my_str)

