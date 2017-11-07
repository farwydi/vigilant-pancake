import base_object
import config
import graphics as gr
import player
import utilities


class Manager:
    """
    Manager - allows you to create and manage objects.

    Attributes:
        objects (list[base_object.BaseObject]): List of all objects.
    """

    def __init__(self, graphics=None):
        """
        Args:
            graphics (Optional[graphics.Graphics]):
        """
        self.graphics = graphics

        if self.graphics is None:
            self.graphics = gr.Graphics()

        self.objects = []

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

    def create_player(self, size=config.PLAYER_SIZE, name=None):
        """
        Create new Player.

        Args:
            size (Optional[int]): Object size.
            name (Optional[str]): Unique name of object.

        Returns:
            player.Player: Created object.
        """
        if name is None:
            name = utilities.gen_name()

        obj = player.Player(self.graphics, self, size, name)
        self.objects.append(obj)
        return obj

    def draw_all(self):
        """
        Draw All Object.
        """
        for obj in self.objects:
            obj.draw()
