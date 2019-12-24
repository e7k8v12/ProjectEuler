# https://projecteuler.net/problem=39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions
# for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
#
# https://euler.jakumo.org/problems/view/39.html
# Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c}, то существует ровно три решения
# для p = 120:{20,48,52}, {24,45,51}, {30,40,50}
# Какое значение p ≤ 1000 дает максимальное число решений?
#
# 840

import time
import math

start_time = time.time()


def solutions(p):
    found_sol = set()
    for a in range(int(p / (2 + math.sqrt(2))), p // 2):
        for b in range(a, 1, -1):
            c = p - a - b
            if c < a + b and c * c == a * a + b * b:
                found_sol.add(', '.join(sorted([str(a), str(b), str(c)])))
    return found_sol


max_len = 0
max_list = []
max_p = 0

for p in range(3, 1001):
    sol = solutions(p)

    if p % 100 == 0:
        print(p, len(sol), sol)

    if max_len < len(sol):
        max_len = len(sol)
        max_list = sol
        max_p = p
        print(p, len(sol))

print(max_p)

end_time = time.time()

print()
print('time:', end_time - start_time)
