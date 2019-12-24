# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 5².
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
# a² + b² = c²
# Например, 3² + 4² = 9 + 16 = 25 = 5².
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.
#
# 200 × 375 × 425 = 31875000

for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c = 1000 - a - b
        if a * a + b * b == c * c:
            print(f"{a} × {b} × {c} = {a * b * c}")
            exit()
