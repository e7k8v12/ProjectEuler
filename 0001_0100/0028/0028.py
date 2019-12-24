#  https://projecteuler.net/problem=28
#  Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#  21 22 23 24 25
#  20  7  8  9 10
#  19  6  1  2 11
#  18  5  4  3 12
#  17 16 15 14 13
#  It can be verified that the sum of the numbers on the diagonals is 101.
#  What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#  https://euler.jakumo.org/problems/view/28.html
#  Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:
#  21 22 23 24 25
#  20  7  8  9 10
#  19  6  1  2 11
#  18  5  4  3 12
#  17 16 15 14 13
#  Можно убедиться, что сумма чисел в диагоналях равна 101.
#  Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?
#
# 669171001

DIMENTION = 1001
RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
spiral = [[0] * DIMENTION for _ in range(DIMENTION)]


def draw(position_value, direction, steps):
    if direction == RIGHT:
        for n in range(1, steps + 1):
            spiral[position_value[1]][position_value[0] + n] = position_value[2] + n
        return position_value[0] + n, position_value[1], position_value[2] + n
    elif direction == DOWN:
        for n in range(1, steps + 1):
            spiral[position_value[1] + n][position_value[0]] = position_value[2] + n
        return position_value[0], position_value[1] + n, position_value[2] + n
    elif direction == LEFT:
        for n in range(1, steps + 1):
            spiral[position_value[1]][position_value[0] - n] = position_value[2] + n
        return position_value[0] - n, position_value[1], position_value[2] + n
    elif direction == UP:
        for n in range(1, steps + 1):
            spiral[position_value[1] - n][position_value[0]] = position_value[2] + n
        return position_value[0], position_value[1] - n, position_value[2] + n


def make_spiral():
    start = (DIMENTION // 2, DIMENTION // 2, 1)
    spiral[DIMENTION // 2][DIMENTION // 2] = 1

    for n in range(1, DIMENTION, 2):
        start = draw(start, RIGHT, n)
        start = draw(start, DOWN, n)
        start = draw(start, LEFT, n + 1)
        start = draw(start, UP, n + 1)
    draw(start, RIGHT, DIMENTION - 1)


make_spiral()
diag1 = sum([spiral[x][x] for x in range(DIMENTION)])
diag2 = sum([spiral[x][DIMENTION - x - 1] for x in range(DIMENTION)])
print(diag1 + diag2 - 1)

