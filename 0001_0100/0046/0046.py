# https://projecteuler.net/problem=46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a
# square.
# 9 = 7 + 2×1²
# 15 = 7 + 2×2²
# 21 = 3 + 2×3²
# 25 = 7 + 2×3²
# 27 = 19 + 2×2²
# 33 = 31 + 2×1²
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#
# https://euler.jakumo.org/problems/view/46.html
# Кристиан Гольдбах показал, что любое нечетное составное число можно записать в виде суммы простого числа и удвоенного
# квадрата.
# 9 = 7 + 2×1²
# 15 = 7 + 2×2²
# 21 = 3 + 2×3²
# 25 = 7 + 2×3²
# 27 = 19 + 2×2²
# 33 = 31 + 2×1²
# Оказалось, что данная гипотеза неверна.
# Каково наименьшее нечетное составное число, которое нельзя записать в виде суммы простого числа и удвоенного квадрата?
#
# 5777

import math
import time

start_time = time.time()


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    primes = []
    for p in range(n + 1):
        if prime[p]:
            primes.append(p)
    return primes


def is_odd_composite(n):
    if n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return True
    return False


def is_good(n):
    for i in sieve_of_eratosthenes(n):
        if math.sqrt((n - i) / 2) % 1 == 0:
            print(f'{n} = {i} + 2×{math.sqrt((n - i) / 2):.0f}²')
            return True
    return False


i = 1
while True:
    i += 2
    if not is_odd_composite(i):
        continue
    if not is_good(i):
        print('Found', i)
        break

end_time = time.time()

print()
print('time:', end_time - start_time)
