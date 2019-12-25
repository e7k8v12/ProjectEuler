# https://projecteuler.net/problem=43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
# order, but it also has a rather interesting sub-string divisibility property.
# Let d₁ be the 1ˢᵗ digit, d₂ be the 2ⁿᵈ digit, and so on. In this way, we note the following:
# d₂d₃d₄=406 is divisible by 2
# d₃d₄d₅=063 is divisible by 3
# d₄d₅d₆=635 is divisible by 5
# d₅d₆d₇=357 is divisible by 7
# d₆d₇d₈=572 is divisible by 11
# d₇d₈d₉=728 is divisible by 13
# d₈d₉d₁₀=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
#
# https://euler.jakumo.org/problems/view/43.html
# Число 1406357289, является пан-цифровым, поскольку оно состоит из цифр от 0 до 9 в определенном порядке. Помимо этого,
# оно также обладает интересным свойством делимости подстрок.
# Пусть d₁ будет 1-ой цифрой, d₂ будет 2-ой цифрой, и т.д. В таком случае, можно заметить следующее:
# d₂d₃d₄=406 делится на 2 без остатка
# d₃d₄d₅=063 делится на 3 без остатка
# d₄d₅d₆=635 делится на 5 без остатка
# d₅d₆d₇=357 делится на 7 без остатка
# d₆d₇d₈=572 делится на 11 без остатка
# d₇d₈d₉=728 делится на 13 без остатка
# d₈d₉d₁₀=289 делится на 17 без остатка
# Найдите сумму всех пан-цифровых чисел из цифр от 0 до 9, обладающих данным свойством.
#
# 16695334890

import time
from itertools import permutations

start_time = time.time()


def is_our_num(n):
    str_n = ' ' + n
    if int(''.join((str_n[2], str_n[3], str_n[4]))) % 2 == 0 and \
            int(''.join((str_n[3], str_n[4], str_n[5]))) % 3 == 0 and \
            int(''.join((str_n[4], str_n[5], str_n[6]))) % 5 == 0 and \
            int(''.join((str_n[5], str_n[6], str_n[7]))) % 7 == 0 and \
            int(''.join((str_n[6], str_n[7], str_n[8]))) % 11 == 0 and \
            int(''.join((str_n[7], str_n[8], str_n[9]))) % 13 == 0 and \
            int(''.join((str_n[8], str_n[9], str_n[10]))) % 17 == 0:
        return True
    return False


total = 0
for i in [''.join(x) for x in permutations('0123456789')]:
    if is_our_num(i):
        total += int(i)

print(total)

end_time = time.time()

print()
print('time:', end_time - start_time)
