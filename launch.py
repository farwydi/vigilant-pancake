import cv2

import config
import graphics as gr
import manager as mg

graphics = gr.Graphics()
manager = mg.Manager(graphics)


def init():
    """
    First initialization world.
    """
    manager.create_player()


def cycle(iteration):
    """
    Life cycle.

    Args:
        iteration:

    Returns:
        bool: False - end game.

    """
    print('New cycle: {}'.format(iteration))
    graphics.clear()
    manager.draw_all()
    graphics.render()

    key = cv2.waitKey()

    if key & 0xFF == ord('1'):
        pass

    if key & 0xFF == ord('q'):
        return False

    graphics.clear()
    manager.draw_all()

    graphics.render()
    return True


if __name__ == '__main__':
    tick = 0

    init()

    while cycle(tick):
        tick += 1
