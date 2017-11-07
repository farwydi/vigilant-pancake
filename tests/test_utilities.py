import utilities


def test_move():
    assert utilities.get_move((0, 0), 90, 5) == (0, 5)
    assert utilities.get_move((0, 0), 450, 5) == (0, 5)
    assert utilities.get_move((0, 0), -90, 5) == (0, -5)
    assert utilities.get_move((0, 0), 0, 5) == (5, 0)


def test_gen_name():
    assert isinstance(utilities.gen_name(), str) is True
    assert len(utilities.gen_name()) == 8
