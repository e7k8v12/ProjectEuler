#  https://projecteuler.net/problem=32
#  We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
#  the 5-digit number, 15234, is 1 through 5 pandigital.
#  The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
#  through 9 pandigital.
#  Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
#  pandigital.
#  HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#  https://euler.jakumo.org/problems/view/32.html
#  Каждое n-значное число, которое содержит каждую цифру от 1 до n ровно один раз, будем считать пан-цифровым; к
#  примеру, 5-значное число 15234 является пан-цифровым, т.к. содержит цифры от 1 до 5.
#  Произведение 7254 является необычным, поскольку равенство 39 × 186 = 7254, состоящее из множимого, множителя и
#  произведения является пан-цифровым, т.е. содержит цифры от 1 до 9.
#  Найдите сумму всех пан-цифровых произведений, для которых равенство 'множимое × множитель = произведение' можно
#  записать цифрами от 1 до 9, используя каждую цифру только один раз.
#  ПОДСКАЗКА: Некоторые произведения можно получить несколькими способами, поэтому убедитесь, что включили их в сумму
#  лишь единожды.
#
# 45228

import time


start_time = time.time()


def divisors(n):
    total = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total.append((str(i), str(n // i)))
    return total


def is_match(val):
    for divisor in divisors(val):
        str_prod = ''.join(divisor) + str(val)
        if len(str_prod) != 9:
            continue
        if all_different(str_prod):
            print(f'{divisor[0]} x {divisor[1]} = {val}')
            return True
    return False


def all_different(val):
    count = {}
    for i in str(val):
        if i == '0':
            return False
        count[i] = count.get(i, 0) + 1
        if count[i] > 1:
            return False
    return True


total = 0
for i in [x for x in range(1000, 10000) if all_different(x)]:
    if is_match(i):
        total += i
print(total)

end_time = time.time()

print('time:', end_time - start_time)
