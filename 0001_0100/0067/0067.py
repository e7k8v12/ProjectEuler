# https://projecteuler.net/problem=67
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
# top to bottom is 23.
# 37 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file
# containing a triangle with one-hundred rows.
# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this
# problem, as there are 2⁹⁹ altogether! If you could check one trillion (10¹²) routes every second it would take over
# twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
#
# https://euler.jakumo.org/problems/view/67.html
# Начиная с вершины представленного ниже треугольника и переходя к прилежащим числам в следующем ряду, максимальная
# возможная сумма пройденных чисел по пути от вершины до основания равна 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# Т.е., 3 + 7 + 4 + 9 = 23.
# Найти максимальную сумму при переходе от вершины до основания треугольника, представленного текстовым файлом размером
# 15КБ triangle.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), в котором содержится треугольник
# с одной сотней строк.
# ПРИМЕЧАНИЕ: Это намного усложненная версия 
# 18-й задачи. Данную задачу нельзя решить, испробовав каждый возможный вариант, поскольку всего их 2⁹⁹! Если бы удалось
# проверять один триллион (10¹²) вариантов в секунду, потребовалось бы двадцать биллионов лет, чтобы испробовать их все.
# Существует эффективный алгоритм решения данной задачи. ;o)
#
# 7273

import time
from functools import lru_cache

DATA = []

with open("p067_triangle.txt", "r") as fi:
    for line in fi.readlines():
        DATA.append([int(x) for x in line.split(" ")])

max_sum = 0


@lru_cache(maxsize=None)
def check_route(total, row, position):
    global max_sum, DATA

    if row == len(DATA):
        max_sum = max(max_sum, total)
    else:
        total += DATA[row][position]
        check_route(total, row + 1, position)
        check_route(total, row + 1, position + 1)
    return total


ts =time.time()
check_route(0, 0, 0)
te = time.time()
print(max_sum, f'in {te-ts:.9} seconds')