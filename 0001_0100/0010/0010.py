# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
# Найдите сумму всех простых чисел меньше двух миллионов.
#
# 142913828922


def sum_of_primes(n):
    sum, sieve = 0, [True] * n
    for i in range(2, n):
        if sieve[i]:
            sum += i
            for j in range(i * i, n, i):
                sieve[j] = False
    return sum


print(sum_of_primes(2000000))
