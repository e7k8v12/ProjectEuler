# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?
#
# 232792560

NUM_OF_VALUES = 20


def is_it_divide(m):
    for i in range(2, NUM_OF_VALUES + 1):
        if m % i != 0:
            return False
    return True


n = NUM_OF_VALUES
while not is_it_divide(n):
    n += NUM_OF_VALUES

print(n)
