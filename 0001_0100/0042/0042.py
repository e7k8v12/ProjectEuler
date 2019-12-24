# https://projecteuler.net/problem=42
# The nᵗʰ term of the sequence of triangle numbers is given by, tₙ = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
# form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t₁₀. If the word value is a triangle
# number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
# English words, how many are triangle words?
#
# https://euler.jakumo.org/problems/view/42.html
# n-ый член последовательности треугольных чисел задается как tₙ = ½n(n+1). Таким образом, первые десять треугольных
# чисел:1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Преобразовывая каждую букву в число, соответствующее ее порядковому номеру в алфавите, и складывая эти значения, мы
# получим числовое значение слова. Для примера, числовое значение слова SKY равно 19 + 11 + 25 = 55 = t₁₀. Если числовое
# значение слова является треугольным числом, то мы назовем это слово треугольным словом.
# Используя words.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), 16 КБ текстовый файл,
# содержащий около двух тысяч часто используемых английских слов, определите, сколько в нем треугольных слов. 
#
# 162

import time

start_time = time.time()

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def word_value(word):
    return sum([alphabet.index(letter) for letter in word])


with open("p042_words.txt", 'r') as f:
    words = f.read()[1:-1].split('","')

max_len = 0
for word in words:
    max_len = max(max_len, len(word))

triangles = [int(x * (x + 1) / 2) for x in range(1, max_len * (len(alphabet) - 1) + 1)]

count = 0
for word in words:
    count += int(word_value(word) in triangles)

# :)
# count = sum(int(sum([alphabet.index(letter) for letter in word]) in [int(x * (x + 1) / 2) for x in range(1, reduce(max, [len(word) for word in words]) * (len(alphabet) - 1) + 1)]) for word in words)

print(f'{count=}')

end_time = time.time()

print()
print('time:', end_time - start_time)
