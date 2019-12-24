#  https://projecteuler.net/problem=26
#  A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators ₂ to
#  ₁₀ are given:
#  ¹/₂= 0.5
#  ¹/₃= 0.(3)
#  ¹/₄= 0.25
#  ¹/₅= 0.2
#  ¹/₆= 0.1(6)
#  ¹/₇= 0.(142857)
#  ¹/₈= 0.125
#  ¹/₉= 0.(1)
#  ¹/₁₀= 0.1
#  Where 0.¹(₆) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that ¹/₇ has a 6-digit recurring
#  cycle.
#  Find the value of d < 1000 for which ¹/d contains the longest recurring cycle in its decimal fraction part.
#  https://euler.jakumo.org/problems/view/26.html
#  Единичная дробь имеет 1 в числителе. Десятичные представления единичных дробей со знаменателями от 2 до 10 даны ниже:
#  ¹/₂= 0.5
#  ¹/₃= 0.(3)
#  ¹/₄= 0.25
#  ¹/₅= 0.2
#  ¹/₆= 0.1(6)
#  ¹/₇= 0.(142857)
#  ¹/₈= 0.125
#  ¹/₉= 0.(1)
#  ¹/₁₀= 0.1
#  Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры. Заметим, что ¹/₇ имеет
#  повторяющуюся последовательность из 6 цифр.
#  Найдите значение d < 1000, для которого ¹/d в десятичном виде содержит самую длинную повторяющуюся
#  последовательность цифр.
#
# 983

def long_division(divident, divider):
    str_divident = str(divident)
    curs = []
    if divident < divider:
        result = '0.'
        rem = str_divident
        curs.append('#')
    else:
        result = ''
        rem = ''

    while rem != '0':
        current = rem
        while current == '' or int(current) < divider:
            if len(str_divident) > 0 and int(str_divident) > divider:
                current += str_divident[0]
                str_divident = str_divident[1:]
            else:
                current += '0'
                if not '.' in result:
                    result += '.'
                result += '0'

        if len(result) != 0 and result[-1] == '0':
            result = result[:-1]

        res = str(int(current) // divider)
        rem = str(int(current) % divider)
        if current in curs:
            position = curs.index(current) - len(curs)
            repeat_part = result[position:]
            result = result[:position] + '(' + result[position:] + ')'
            return result, len(repeat_part)
        curs.append(current)

        result += res + (str_divident if (len(str_divident) != 0 and rem == '0') else '')

    return result, 0


max_d = 0
max_len = 0
for d in range(2, 1000):
    res_len = long_division(1, d)[1]
    if max_len < res_len:
        max_len = res_len
        max_d = d
print(max_d)


