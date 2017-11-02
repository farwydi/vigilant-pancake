# import box
import uuid

# import config
import base_object
import player


class Manager:
    """
    Manager - allows you to create and manage objects.

    Attributes:
        objects (list[base_object.BaseObject]): List of all objects.
    """

    def __init__(self, graphics):
        """
        Args:
            graphics (graphics.Graphics):
        """
        self.graphics = graphics
        self.objects = []

    @classmethod
    def gen_name(cls):
        """
        Returns:
            str: Random name.
        """
        return str(uuid.uuid4())[:8]

    def get_by_name(self, name):
        """
        Get object by name or None.

        Args:
            name (str): Object name.

        Returns:
            base_object.BaseObject | None:
        """
        for obj in self.objects:
            if obj.name == name:
                return obj

        return None

    def create_player(self, size, name=None):
        """
        Create new Player.

        Args:
            size (int): Object size.
            name (str): Unique name of object.

        Returns:
            player.Player: Created object.
        """
        if name is None:
            name = self.gen_name()

        obj = player.Player(self.graphics, self, name, size)
        self.objects.append(obj)
        return obj
