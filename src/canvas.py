from random import randint

from numpy import zeros, clip

import config

grid = zeros((config.COUNT_LINE_OBJECT, config.COUNT_LINE_OBJECT), dtype=int)


def fill_grid(type_object, func_fill, count):
    it = count
    while it > 0:
        ri, rj = randint(0, config.COUNT_LINE_OBJECT - 1), randint(0, config.COUNT_LINE_OBJECT - 1)

        if grid[ri][rj] != 0:
            continue

        if grid[ri][rj] == type_object:
            continue

        func_fill(type_object, ri, rj)
        it -= 1


def simple_fill(type_object, ri, rj):
    grid[ri][rj] = type_object


def well_fill(type_object, ri, rj):
    direction = randint(0, 3)

    for length in range(randint(1, config.MAX_WALL_LENGTH)):
        if direction == 0:
            grid[clip(ri + length, 0, config.COUNT_LINE_OBJECT - 1)][rj] = type_object
        elif direction == 1:
            grid[clip(ri - length, 0, config.COUNT_LINE_OBJECT - 1)][rj] = type_object
        elif direction == 2:
            grid[ri][clip(rj + length, 0, config.COUNT_LINE_OBJECT - 1)] = type_object
        elif direction == 3:
            grid[ri][clip(rj - length, 0, config.COUNT_LINE_OBJECT - 1)] = type_object


fill_grid(1, simple_fill, config.MAX_EAT_COUNT)
fill_grid(2, simple_fill, config.MAX_POISON_COUNT)
fill_grid(3, well_fill, config.MAX_WALL_COUNT)

live_x = 23
live_y = 23
grid[live_x][live_y] = 4


def read_canvas(file_name: str):
    with open(file_name, 'r') as f:
        x = f.readlines()[0].rstrip()
        config.PLANCK_LENGTH, config.COUNT_LINE_OBJECT = x.split('-')


def save_canvas(file_name: str):
    with open(file_name, 'w') as f:
        f.write(f"{config.PLANCK_LENGTH}-{config.COUNT_LINE_OBJECT}\n")
