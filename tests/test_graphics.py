import numpy as np
import pytest

import config


@pytest.fixture(scope="module")
def graphics():
    import graphics as gh
    gr = gh.Graphics()
    yield gr
    del gr


def test_init(graphics):
    assert np.count_nonzero(graphics.BG) == 0
    assert graphics.BG.shape == (config.WORLD_SIZE[0], config.WORLD_SIZE[1], 3)


def test_draw_rectangle(graphics):
    graphics.clear()
    graphics.draw_rectangle((1, 1), (2, 2), (255, 255, 255))
    assert np.count_nonzero(graphics.BG) == 12


def test_clear(graphics):
    graphics.draw_rectangle((1, 1), (2, 2), (255, 255, 255))
    graphics.clear()
    assert np.count_nonzero(graphics.BG) == 0


# def test_draw_circle(graphics):
#     graphics.clear()
#     graphics.draw_circle((1, 1), 5, (255, 255, 255))
#     assert np.count_nonzero(graphics.BG) == 111


def test_draw_text(graphics):
    graphics.clear()
    graphics.draw_text("Test", 0, (255, 255, 255))
    assert np.count_nonzero(graphics.BG) == 36


def test_draw_line(graphics):
    graphics.clear()
    graphics.draw_line((1, 1), (2, 2), (255, 255, 255))
    assert np.count_nonzero(graphics.BG) == 81