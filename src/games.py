import time

import pygame

import config

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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


score = 0

mgScore = pygame.font.SysFont('Comic Sans MS', 60)

while not done:
    start_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    fps = 1.0 / (time.time() - start_time)
    score_text = mgScore.render("FPS: " + str(round(fps, 2)), False, (0, 0, 0))
    screen.blit(score_text, (20, 0))

    for i in range(config.COUNT_LINE_OBJECT):
        for j in range(config.COUNT_LINE_OBJECT):
            x, y = (i * config.PLANCK_LENGTH, j * config.PLANCK_LENGTH)
            h, w = (config.PLANCK_LENGTH, config.PLANCK_LENGTH)

            pygame.draw.rect(screen, RED, (x, config.HEADER_SIZE + y, h, w), 1)

    score += 1

    pygame.display.flip()

pygame.quit()
