#  https://projecteuler.net/problem=24
#  A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2,
#  3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
#  lexicographic permutations of 0, 1 and 2 are:
#  012   021   102   120   201   210
#  What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#  https://euler.jakumo.org/problems/view/24.html
#  Перестановка - это упорядоченная выборка объектов. К примеру, 3124 является одной из возможных перестановок из цифр
#  1, 2, 3 и 4. Если все перестановки приведены в порядке возрастания или алфавитном порядке, то такой порядок будем
#  называть словарным. Словарные перестановки из цифр 0, 1 и 2 представлены ниже:
#  012   021   102   120   201   210
#  Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?
#
# 2783915460

from itertools import permutations

print(sorted([''.join(x) for x in permutations('0123456789')])[999999])

