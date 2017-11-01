import random

import pytest

import base_object as bo


@pytest.fixture(scope="module")
def base():
    random.seed(5)
    obj = bo.BaseObject(None, None, "test")
    yield obj
    del obj


def test_random_position(base):
    """
    Args:
        base (bo.BaseObject):
    """
    base.set_random_position()
    assert base.position == (867, 680)


def test_move(base):
    """
    Args:
        base (bo.BaseObject):
    """
    base.position = (0, 0)
    base.rotation = 0.0

    base.move(10)
    assert base.position == (10, 0)

    base.position = (0, 0)
    base.rotation = 0.0

    base.move(-10)
    assert base.position == (-10, 0)


def test_rotate(base):
    """
    Args:
        base (bo.BaseObject):
    """
    base.rotation = 0.0

    # 180
    base.rotate(0.5)
    assert base.rotation == 180

    base.rotation = 0.0

    base.rotate(4.5)
    assert base.rotation == 180

    base.rotation = 0.0

    base.rotate(-4.5)
    assert base.rotation == -180
