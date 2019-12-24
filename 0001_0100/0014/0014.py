# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
# Следующая повторяющаяся последовательность определена для множества натуральных чисел:
# n → n/2 (n - четное)
# n → 3n + 1 (n - нечетное)
# Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов. Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким образом последовательности оканчиваются на 1.
# Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?
# Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.
#
# 837799 525

from operator import itemgetter
from functools import lru_cache


@lru_cache(maxsize=None)
def get_sequence_length(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + get_sequence_length(n // 2)
    else:
        return 1 + get_sequence_length(3 * n + 1)


result = max([(i, get_sequence_length(i)) for i in range(1, 1000000 + 1)], key=itemgetter(1))

print(f'{result[0]} {result[1]}')
