# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.
# Сколько существует таких маршрутов в сетке 20×20?
#
# 137846528820

from functools import lru_cache

HORIZ, VERT = 20, 20
RIGHT, DOWN = 1, 2


@lru_cache(maxsize=None)
def move(x, y, direction):
    if direction == RIGHT:
        x += 1
    elif direction == DOWN:
        y += 1
    if x == HORIZ and y == VERT:
        return 1
    moves = 0
    if x < HORIZ:
        moves += move(x, y, RIGHT)
    if y < VERT:
        moves += move(x, y, DOWN)
    return moves


print(move(0, 0, 0))
