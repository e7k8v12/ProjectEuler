#  https://projecteuler.net/problem=27
#  Euler discovered the remarkable quadratic formula:
#  n^2 + n + 41
#  It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However,
#  when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is
#  clearly divisible by 41.
#  The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <=
#  n <= 79. The product of the coefficients, −79 and 1601, is −126479.
#  Considering quadratics of the form:
#  n^2 + an + b, where |a| < 1000 and |b| <= 1000 where |n| is the modulus/absolute value of n e.g. |11| = 11
#  and |-4| = 4
#  Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
#  primes for consecutive values of n, starting with n = 0.
#  https://euler.jakumo.org/problems/view/27.html
#  Эйлер опубликовал свою замечательную квадратичную формулу:
#  n^2 + n + 41
#  Оказалось, что согласно данной формуле можно получить 40 простых чисел, последовательно подставляя значения 0 <= n
#  <= 39. Однако, при n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 делится на 41 без остатка, и, очевидно, при n =
#  41, 41^2 + 41 + 41 делится на 41 без остатка.
#  При помощи компьютеров была найдена невероятная формула n^2 - 79n + 1601, согласно которой можно получить 80
#  простых чисел для последовательных значений n от 0 до 79. Произведение коэффициентов −79 и 1601 равно −126479.
#  Рассмотрим квадратичную формулу вида:
#  n^2 + an + b, где |a| < 1000 и |b| <= 1000
#  где |n| является модулем (абсолютным значением) n.К примеру, |11| = 11 и |−4| = 4
#  Найдите произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное
#  количество простых чисел для последовательных значений n, начиная со значения n = 0.
#
# -59231


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True


max_n = 0
max_ab = 0
for a in range(-999, 1000):
    # print(f'a={a}')
    for b in range(-1000, 1001):
        n = 0
        while is_prime(n ** 2 + a * n + b):
            n += 1
        if max_n < n:
            max_n = n
            max_ab = a * b
            print(f'n={n-1}, a={a}, b={b}, formula: n^2{a:+d}n{b:+d}')

print(max_ab)