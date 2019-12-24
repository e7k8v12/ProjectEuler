#  https://projecteuler.net/problem=25
#  The Fibonacci sequence is defined by the recurrence relation:
#  Fₙ = Fₙ₋₁ + Fₙ₋₂, where F₁ = 1 and F₂ = 1.
#  Hence the first 12 terms will be:
#  F₁ = 1
#  F₂ = 1
#  F₃ = 2
#  F₄ = 3
#  F₅ = 5
#  F₆ = 8
#  F₇ = 13
#  F₈ = 21
#  F₉ = 34
#  F₁₀ = 55
#  F₁₁ = 89
#  F₁₂ = 144
#  The 12th term, F₁₂, is the first term to contain three digits.
#  What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
#  https://euler.jakumo.org/problems/view/25.html
#  Последовательность Фибоначчи определяется рекурсивным правилом:
#  Fₙ = Fₙ₋₁ + Fₙ₋₂, где F₁ = 1 и F₂ = 1.
#  Таким образом, первые 12 членов последовательности равны:
#  F₁ = 1
#  F₂ = 1
#  F₃ = 2
#  F₄ = 3
#  F₅ = 5
#  F₆ = 8
#  F₇ = 13
#  F₈ = 21
#  F₉ = 34
#  F₁₀ = 55
#  F₁₁ = 89
#  F₁₂ = 144
#  Двенадцатый член F₁₂ - первый член последовательности, который содержит три цифры.Каков порядковый номер первого
#  члена последовательности Фибоначчи, содержащего 1000 цифр?
#
# 4782

import time

start_time = time.time()

a = b = 1
count = 1
while len(str(a)) != 1000:
    a, b = b, a + b
    count += 1

print(count)
end_time = time.time()

print('time:', end_time - start_time)
