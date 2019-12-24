#  https://projecteuler.net/problem=30
#  Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#  1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
#  8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
#  9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
#  As 1 = 1⁴ is not a sum it is not included.
#  The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#  Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#  https://euler.jakumo.org/problems/view/30.html
#  Удивительно, но существует только три числа, которые могут быть записаны в виде суммы четвертых степеней их цифр:
#  1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
#  8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
#  9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
#  1 = 1⁴ не считается, так как это - не сумма.
#  Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.
#  Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.
#
# 443839

import time

POWER = 5


def check_number(num):
    total = 0
    for i in str(num):
        total += int(i) ** POWER
    return total == num


start_time = time.time()

tot = 0
for n in range(10, 5 * 9 ** 5):
    if check_number(n):
        tot += n
        print(f'value: {n}, total: {tot}')

end_time = time.time()

print('time:', end_time - start_time)
