# https://projecteuler.net/problem=34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
# https://euler.jakumo.org/problems/view/34.html
# 145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.
# Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не
# следует.
#
# 40730

import time

start_time = time.time()

f = 1
fac = {"0": 1}
for n in range(1, 10):
    f *= n
    fac[str(n)] = f

total = 0
for n in range(10, 100000):
    if n == sum([fac[x] for x in str(n)]):
        total += n

end_time = time.time()
print(total)
print()
print('time:', end_time - start_time)
