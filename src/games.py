import random
import time

import numpy
import pygame

import config
from canvas import grid, live_x, live_y

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (0, 255, 255)
BLUE = (0, 0, 255)

color = {
    0: WHITE,
    1: GREEN,
    2: YELLOW,
    3: BLUE,
    4: RED
}

object_color = {
    0: WHITE,
    1: GREEN,  # EAT
    2: RED,  # POISON
    3: YELLOW,  # WALL
    4: BLUE  # PLAYER
}

object_fill = {
    0: 0,
    1: 1,  # EAT
    2: 1,  # POISON
    3: 0,  # WALL
    4: 0  # PLAYER
}

pygame.init()

screen = pygame.display.set_mode(config.DISPLAY_SIZE)

clock = pygame.time.Clock()
done = False


class LiveObject(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        pass


class AI(LiveObject):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.type = 1


def move(grid, i: int, j: int, vertical: int, horizontal: int):
    if grid[i][j] != 4:
        raise Exception()

    vertical = numpy.clip(vertical, -1, 1)
    vertical = i + vertical
    if vertical >= config.COUNT_LINE_OBJECT:
        vertical = 0

    if vertical < -config.COUNT_LINE_OBJECT:
        vertical = config.COUNT_LINE_OBJECT - 1

    horizontal = numpy.clip(horizontal, -1, 1)
    horizontal = horizontal + j
    if horizontal >= config.COUNT_LINE_OBJECT:
        horizontal = 0

    if horizontal < -config.COUNT_LINE_OBJECT:
        horizontal = config.COUNT_LINE_OBJECT - 1

    if grid[vertical][horizontal] == 0:
        grid[vertical][horizontal] = 4
        grid[i][j] = 0

        return vertical, horizontal

    return i, j


score = 0

mgScore = pygame.font.SysFont('Comic Sans MS', 60)

while not done:
    start_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    try:
        fps = 1.0 / (time.time() - start_time)
    except ZeroDivisionError:
        fps = 1.0

    score_text = mgScore.render("FPS: " + str(round(fps, 2)), False, (0, 0, 0))
    screen.blit(score_text, (20, 0))

    live_x, live_y = move(grid, live_x, live_y, random.randint(-1, 1), random.randint(-1, 1))

    for i in range(config.COUNT_LINE_OBJECT):
        for j in range(config.COUNT_LINE_OBJECT):
            object_type = grid[i][j]
            if object_type == 0:
                continue
            x, y = (i * config.PLANCK_LENGTH, j * config.PLANCK_LENGTH)
            h, w = (config.PLANCK_LENGTH, config.PLANCK_LENGTH)

            pygame.draw.rect(screen, object_color[object_type], (x, config.HEADER_SIZE + y, h, w),
                             object_fill[object_type])

    score += 1

    pygame.display.flip()

pygame.quit()
