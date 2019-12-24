# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
# n! означает n × (n − 1) × ... × 3 × 2 × 1
# Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Найдите сумму цифр в числе 100!.
#
# 648


def fac(n):
    if n <= 0:
        return 1
    return n * fac(n - 1)


print(sum([int(x) for x in str(fac(100))]))
