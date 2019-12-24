# https://projecteuler.net/problem=40
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12ᵗʰ digit of the fractional part is 1.
# If d<ᵢ>ₙ represents the nᵗʰ digit of the fractional part, find the value of the following expression.
# d₁ × d₁₀ × d₁₀₀ × d₁₀₀₀ × d₁₀₀₀₀ × d₁₀₀₀₀₀ × d₁₀₀₀₀₀₀
#
# https://euler.jakumo.org/problems/view/40.html
# Дана иррациональная десятичная дробь, образованная объединением положительных целых чисел:
# 0.123456789101112131415161718192021...
# Видно, что 12-ая цифра дробной части - 1.
# Также дано, что dₙ представляет собой n-ую цифру дробной части. Найдите значение следующего выражения:
# d₁ × d₁₀ × d₁₀₀ × d₁₀₀₀ × d₁₀₀₀₀ × d₁₀₀₀₀₀ × d₁₀₀₀₀₀₀
#
# 210

import time

start_time = time.time()

places = [1, 100, 1000, 10000, 100000, 1000000]

res = 1
counter = 0
digits = 0
while digits <= 1000000:
    counter += 1
    str_count = str(counter)
    for s in str_count:
        digits += 1
        if digits in places:
            res *= int(s)

print(res)
end_time = time.time()

print()
print('time:', end_time - start_time)
