# https://projecteuler.net/problem=37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
# left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
# 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
# https://euler.jakumo.org/problems/view/37.html
# Число 3797 обладает интересным свойством. Будучи само по себе простым числом, из него можно последовательно
# выбрасывать цифры слева направо, число же при этом остается простым на каждом этапе: 3797, 797, 97, 7. Точно таким же
# способом можно выбрасывать цифры справа налево: 3797, 379, 37, 3.
# Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать цифры как справа налево, так и
# слева направо, но числа при этом остаются простыми.
# ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.
#
# 748317

import time

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


def is_interesting(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
        if not is_prime(int(str_n[:-i])):
            return False

    return True


a = 7
count = 0
total = 0
while count < 11:
    a += 1
    if not is_prime(a):
        continue
    if is_interesting(a):
        print(a)
        total += a
        count += 1

print()
print(total)
end_time = time.time()

print()
print('time:', end_time - start_time)
