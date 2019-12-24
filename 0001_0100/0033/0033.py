#  https://projecteuler.net/problem=33
#  The fraction ⁴⁹/₉₈ is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
#  incorrectly believe that ⁴⁹/₉₈ = ⁴/₈, which is correct, is obtained by cancelling the 9s.
#  We shall consider fractions like, ³⁰/₅₀ = ³/₅, to be trivial examples.
#  There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
#  digits in the numerator and denominator.
#  If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
#  https://euler.jakumo.org/problems/view/33.html
#  Дробь ⁴⁹/₉₈ является любопытной, поскольку неопытный математик, пытаясь сократить ее, будет ошибочно полагать, что
#  ⁴⁹/₉₈ = ⁴/₈, являющееся истиной, получено вычеркиванием девяток.
#  Дроби вида ³⁰/₅₀ = ³/₅ будем считать тривиальными примерами.
#  Существует ровно 4 нетривиальных примера дробей подобного типа, которые меньше единицы и содержат двухзначные числа
#  как в числителе, так и в знаменателе.
#  Пусть произведение этих четырех дробей дано в виде несократимой дроби (числитель и знаменатель дроби не имеют общих
#  сомножителей). Найдите знаменатель этой дроби.
#
# 100

import time
from functools import reduce

start_time = time.time()


def is_non_trivial(a, b):
    if a >= b:
        return False
    str_a = str(a)
    str_b = str(b)
    for i in '123456789':
        if i in str_a and i in str_b:
            ind_a = str_a.index(i)
            aa = int(str_a[:ind_a] + str_a[ind_a + 1:])
            ind_b = str_b.index(i)
            bb = int(str_b[:ind_b] + str_b[ind_b + 1:])
            if bb == 0:
                continue
            if a / b == aa / bb:
                return True
    return False


def greatest_common_factor(a, b):
    if b == 0:
        return a
    return greatest_common_factor(b, a % b)


fractions_a = []
fractions_b = []
for i in range(10, 100):
    for j in range(10, 100):
        if is_non_trivial(i, j):
            fractions_a.append(i)
            fractions_b.append(j)

print([f'{x[0]}/{x[1]}' for x in zip(fractions_a, fractions_b)])

prod_a = reduce(lambda x, y: x * y, fractions_a)
prod_b = reduce(lambda x, y: x * y, fractions_b)

print(prod_b / greatest_common_factor(prod_a, prod_b))

end_time = time.time()

print('time:', end_time - start_time)
