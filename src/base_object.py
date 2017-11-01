import random

import config
import dmath


class BaseObject(object):
    def __init__(self, graphics, manager, name):
        """
        Args:
            graphics (Graphics): Graphics ref.
            manager (Manager): Manager ref.
            name (str): Object name.
        """
        self.size = 60
        self.graphics = graphics
        self.name = name
        self.manager = manager
        self.position = (int(config.WORLD_SIZE[0] / 2), int(config.WORLD_SIZE[1] / 2))
        self.rotation = 0
        self.color = (int(random.uniform(0, 255)), int(random.uniform(0, 255)), int(random.uniform(0, 255)))

    def set_random_position(self):
        self.position = (int(random.uniform(0, config.WORLD_SIZE[0])), int(random.uniform(0, config.WORLD_SIZE[1])))

    def re_init(self):
        pass  # pragma: no cover

    def draw(self):
        pass  # pragma: no cover

    def life(self):
        pass  # pragma: no cover

    def move(self, force=config.PLAYER_STEP):
        """
        Move object forward.

        Args:
            force (float): The distance to which the object moves.

        Returns:
            None:
        """
        self.position = dmath.get_move(self.position, self.rotation, force)

    def rotate(self, angle):
        """
        Rotate object on angle.

        Args:
            angle (float): Angel of rotate.

        Returns:
            None:
        """
        self.rotation += angle * 360
        self.rotation -= round(self.rotation / 360) * 360
