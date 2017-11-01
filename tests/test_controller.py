import random

import pytest

import controller as cl


@pytest.fixture(scope="module")
def controller():
    random.seed(5)
    obj = cl.Object(None, None, "test")
    yield obj
    del obj


def test_random_position(controller):
    """
    Args:
        controller (cl.Object):
    """
    controller.set_random_position()
    assert controller.position == (867, 680)


def test_move(controller):
    """
    Args:
        controller (cl.Object):
    """
    controller.position = (0, 0)
    controller.rotation = 0.0

    controller.move(10)
    assert controller.position == (10, 0)

    controller.position = (0, 0)
    controller.rotation = 0.0

    controller.move(-10)
    assert controller.position == (-10, 0)


def test_rotate(controller):
    """
    Args:
        controller (cl.Object):
    """
    controller.rotation = 0.0

    # 180
    controller.rotate(0.5)
    assert controller.rotation == 180

    controller.rotation = 0.0

    controller.rotate(4.5)
    assert controller.rotation == 180

    controller.rotation = 0.0

    controller.rotate(-4.5)
    assert controller.rotation == -180
