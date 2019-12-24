# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
# Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
# Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, а каждое из чисел a и b - дружественным числом.
# Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.
# Подсчитайте сумму всех дружественных чисел меньше 10000.
#
#


def d(n):
    total = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i + n // i

    return total


total = 0
for i in range(1, 10000):
    di = d(i)
    if i == d(di) and i != di:
        total += i

print(total)
