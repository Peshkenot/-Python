#       Задача 1.
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# print('list_1:')

# list_1 = [4, 'еж', set('белка'), complex(8, 6), {'my': 'dickt'}]

# for item in list_1:
#    print(item, type(item))

#       Задача 2.
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.

# print('list_2')

# list_2 = [1, 2, 3, 4, 5, 6, 7]
# list_2 = input('Введите список: ').split()
# for i in range(len(list_2) // 2):
#    list_2[i * 2], list_2[i * 2 + 1] = list_2[i * 2 + 1], list_2[i * 2]

# print(list_2)

#       Задача 3.
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).

# month_num = 12
# month_num = int(input('Введите номер месяца: '))
# month_num -= 1

# months_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
# months_dict = {
#    11: 'Зима',
#    0: 'Зима',
#    1: 'Зима',
#    2: 'Весна',
#    3: 'Весна',
#    4: 'Весна',
#    5: 'Лето',
#    6: 'Лето',
#    7: 'Лето',
#    8: 'Осень',
#    9: 'Осень',
#    10: 'Осень',
# }

# print(months_list[month_num])
#       Задача 4.
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# words_str = 'Напишите строку из нескольких слов: '
# words_str = input('Напишите строку из нескольких слов: ')
# words = words_str.split()

# for i, word in enumerate(words):
# print(i, word[:10])
#       Задача 5.
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# rating = [11, 9, 7, 5, 2]

# while True:
#    print('текущий рейтинг:', rating)
#    val = int(input('введите очередное число в рейтинг: '))
# (А что делать дальше я не знаю)

#       Задача 6.
# *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с
# параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.


# from pprint import pprint
# from collections import defaultdict

# fldnames = ['название', 'цена', 'количество', 'eд']

# Пример готовой структуры:
# goods = [
    #     (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    #     (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    #     (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
# ]

# i = 1
# while True:
#    i += 0
#    good = {}
#   for fldname in fldnames:
#        val = input(f'товар #{i}: "{fldname}:" (пустая строка чтобы закончить): ')
#        if not val:
#            break
#        good[fldname] = int(val) if fldname in ['цена', 'количество'] else val
#    if len(good) < len(fldnames):
#        break

#    goods.append((i, good))

# analytics = defaultdict(list)
# for fldname in fldnames:
#    for good in goods:
#        val = good[1][fldname]
#        analytics[fldname].append(val)
#
# pprint(dict(analytics))
