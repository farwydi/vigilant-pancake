import graphics
import manager

if __name__ == 'main':
    graphics = graphics.Graphics()
    manager = manager.Manager(graphics)

    manager.create_player(30)
