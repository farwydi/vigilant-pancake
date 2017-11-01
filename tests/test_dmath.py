import dmath


def test_move():
    assert dmath.get_move((0, 0), 90, 5) == (0, 5)
    assert dmath.get_move((0, 0), 450, 5) == (0, 5)
    assert dmath.get_move((0, 0), -90, 5) == (0, -5)
    assert dmath.get_move((0, 0), 0, 5) == (5, 0)