# https://projecteuler.net/problem=41
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
# 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
#
# https://euler.jakumo.org/problems/view/41.html
# Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до n используется в нем ровно один раз. К примеру,
# 2143 является 4-значным пан-цифровым числом, а также простым числом.
# Какое существует наибольшее n-значное пан-цифровое простое число?
#
# 7652413

import time
from itertools import permutations

start_time = time.time()


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for m in range(3, int(n ** 0.5) + 1, 2):
        if n % m == 0:
            return False
    return True


break_flag = False
for a in range(9, 0, -1):
    number = ''.join([str(x) for x in range(1, a + 1)])
    perm = sorted([int(''.join(x)) for x in permutations(number)], reverse=True)
    for i in perm:
        if is_prime(i):
            print(i)
            break_flag = True
            break
    if break_flag:
        break

end_time = time.time()

print()
print('time:', end_time - start_time)
