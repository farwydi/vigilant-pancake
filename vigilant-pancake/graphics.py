import cv2
import numpy as np

import config


class Graphics(object):
    """
    The object visualization helper class.
    """

    def __init__(self):
        self.BG = None
        self.clear()

    def __del__(self):  # pragma: no cover
        cv2.destroyWindow(config.WORLD_NAME)
        self.BG = None

    def clear(self):
        self.BG = np.zeros((config.WORLD_SIZE[0], config.WORLD_SIZE[1], 3), np.uint8)

    def render(self):
        cv2.imshow(config.WORLD_NAME, self.BG)  # pragma: no cover

    def draw_rectangle(self, start, end, color, thickness=-1):
        cv2.rectangle(self.BG, start, end, color, thickness)

    def draw_circle(self, position, radius, color, thickness=-1):
        cv2.circle(self.BG, position, radius, color, thickness)

    def draw_text(self, text, top_offset, color):
        cv2.putText(self.BG, text, (10, top_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, color)

    def draw_line(self, start, end, color):
        cv2.line(self.BG, start, end, color, 5)
