# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
#
# def my_round(number, ndigits):
#    pass
#    numberOne = number * 10**ndigits # ввел дополнительные переменные для того, чтобы было понятнее в режиме отладки.
#    numberTwo = (number*10**ndigits)//1
#
#    if numberOne - numberTwo > 0.5:
#       numberOne = ((numberOne + 1) // 1) / 10**ndigits
#
#    return numberOne
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
#
# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
#
# def lucky_ticket(ticket_number):
#    pass
#    strTicketNumber = str(ticket_number)
#    firstSum = 0
#    secondSum = 0
#
#    if len(strTicketNumber) % 2 != 0:
#        return False
#
#    for i in range(len(strTicketNumber) % 2):
#        firstSum += int(strTicketNumber[i])
#        secondSum += int(strTicketNumber[-i - 1])
#
#    return firstSum == secondSum
#
#
# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))
#
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
#
# def fibonacci(n, m):
#    pass
#    fib = []
#    sumFib = 0
#    firstSum = n
#    secondSum = 0
#
#    while (sumFib < m):
#        sumFib = firstSum + secondSum
#        firstSum = secondSum
#        secondSum = sumFib
#        if sumFib > m:
#            break
#
#        fib.append(sumFib)

#    return fib
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# def sort_to_max(origin_list):
#    pass
# sortList = []
#    sortOriginList = list(origin_list)
#    while len(sortList) != len(origin_list):
#        m = min(sortOriginList)
#        sortList.append(min(sortOriginList))
#        sortOriginList.remove(m)
#    return sortList
# sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# A1, A2, A3, A4 = (5, 5), (2, 4), (6, 3), (9, 4)
#
# def parallelogram(a, b, c, d):
#    if a[0] - d[0] == b[0] - c[0] and a[1] - d[1] == b[1] - c[1]:
#        print("Стороны попарно параллельны, а значит и равны. Данные точки являются вершинами параллелограмма")
#    else:
#        print("Стороны не равны и не параллельны. Данные точки не являются вершинами параллелограмма")


# parallelogram (A1, A2, A3, A4)