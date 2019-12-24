# https://projecteuler.net/probl57em=35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
# prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
# https://euler.jakumo.org/problems/view/35.html
# Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми
# числами: 197, 719 и 971.
# Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.
# Сколько существует круговых простых чисел меньше миллиона?
#
# 55

import time
from itertools import permutations

start_time = time.time()


def is_prime(n):
    if n <= 2:
        return True
    if n % 2 == 0:
        return False
    for m in range(3, int(n ** 0.5) + 1, 2):
        if n % m == 0:
            return False
    return True


def get_rotations(n):
    str_n = str(n)
    rotations = []
    for n in range(len(str_n)):
        str_n = str_n[-1] + str_n[:-1]
        rotations.append(str_n)
    return rotations


def is_round(n):
    for m in get_rotations(n):
        if not is_prime(int(''.join(m))):
            return False
    return True


total = 0
for n in range(2, 1000000):
    if is_round(n):
        print(n)
        total += 1

print(total)

end_time = time.time()

print('time:', end_time - start_time)
