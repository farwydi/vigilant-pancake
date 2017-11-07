import math
import uuid


def get_move(start_position, angle, distance):
    """
    - `x1 = dx * sin(a) + x`
    - `y1 = dy * cos(a) + y`

    Args:
        start_position (tuple[int, int]): Start object position.
        angle (float): Angel of rotation in degrees.
        distance (int): Distance to move.

    Returns:
        tuple[int, int]: New object position.
    """
    return (int(math.cos(math.radians(angle)) * distance + start_position[0]),
            int(math.sin(math.radians(angle)) * distance + start_position[1]))


def gen_name():
    """
    Returns:
        str: Random name.
    """
    return str(uuid.uuid4())[:8]
