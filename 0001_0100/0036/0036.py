# https://projecteuler.net/problem=36
# The decimal number, 585 = 1001001001₂ (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
# https://euler.jakumo.org/problems/view/36.html
# Десятичное число 585 = 1001001001₂ (в двоичной системе), является палиндромом по обоим основаниям.
# Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по основаниям 10 и 2.
# (Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований).
#
# 872187

import time

start_time = time.time()


def is_palindrome(n):
    for i in range(len(n) // 2):
        if n[i] != n[-i - 1]:
            return False
    return True

total = 0
for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(f'{i:b}'):
        print(i, f'{i:b}')
        total += i

print(total)

end_time = time.time()

print('time:', end_time - start_time)
