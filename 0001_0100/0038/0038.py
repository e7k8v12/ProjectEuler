# https://projecteuler.net/problem=38
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
# of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
# (1,2, ... , n) where n > 1?
# https://euler.jakumo.org/problems/view/38.html
# Возьмем число 192 и умножим его по очереди на 1, 2 и 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# Объединяя все три произведения, получим девятизначное число 192384576 из цифр от 1 до 9 (пан-цифровое число). Будем
# называть число 192384576 объединенным произведением 192 и (1,2,3)
# Таким же образом можно начать с числа 9 и по очереди умножать его на 1, 2, 3, 4 и 5, что в итоге дает пан-цифровое
# число 918273645, являющееся объединенным произведением 9 и (1,2,3,4,5).
# Какое самое большое девятизначное пан-цифровое число можно образовать как объединенное произведение целого числа и
# (1,2, ... , n), где n > 1?
#
# 

import time

start_time = time.time()


def concatenated_product(n, m):
    prod = ''.join([str(n * x) for x in range(1, m + 1)])

    if len(prod) != 9:
        return -1
    digs = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, }
    for i in prod:
        if i == '0':
            return -1
        digs[i] += 1
        if digs[i] > 1:
            return -1
    for key in digs:
        if digs[key] != 1:
            return -1
    return int(prod)


max_num = 0
max_comp = ()
for i in range(10000):
    for j in range(9 // len(str(i)) + 1):
        res = concatenated_product(i, j)
        if res != -1:
            print((i, j), res)
        if max_num < res:
            max_num = res
            max_comp = (i, j)

end_time = time.time()
print()
print(max_comp, max_num)

print()
print('time:', end_time - start_time)
