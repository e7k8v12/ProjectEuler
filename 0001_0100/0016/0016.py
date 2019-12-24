# 2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2¹⁰⁰⁰?
# 2¹⁵ = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
# Какова сумма цифр числа 2¹⁰⁰⁰?
#
# 1366

from functools import reduce

power = 1000
print(reduce(lambda x, y: int(x) + int(y), str(2 ** power)))
