import config
import controller


class Player(controller.Object):
    def __init__(self, gm, manager, name, size):
        super().__init__(gm, manager, name)
        self.size = size
        self.health = 0
        self.death = False
        self.rotation = 0
        self.score = 0
        self.__score_buffer = 0
        self.rotate_mem = False
        self.action = ''
        self.re_init()

    def re_init(self):
        self.set_random_position()
        self.health = 500
        self.death = False
        self.rotation = 0
        self.score = 0
        self.__score_buffer = 0
        self.rotate_mem = False
        self.action = ''

    def get_info(self, offset):
        text = self.name + '    ' + \
               str(self.health) + '   ' + \
               str(self.score) + '  ' + str(self.action)
        self.gmt.drawText(text, offset, self.color)

    def draw(self):
        if not self.death:
            self.gmt.drawLine(tuple(self.position), tuple(
                self.get_move(self.position, self.rotation, 15)), self.color)
            self.gmt.drawCircle(tuple(self.position), self.size, self.color)
            self.gmt.drawCircle(tuple(self.position),
                                self.size + config.PLAYER_VISION, self.color, 1)

    def life(self):
        self.rotate_mem = False
        if not self.death:
            if self.health < 0:
                self.death = True

    def eat(self):
        (wall, posion, food) = self.manager.get_vision(self)
        if not posion == None:
            self.death = True
            self.health = -1
            posion.re_init()
            print(self.name, 'eat poison! and death :(')
            return True

        if not food == None:
            self.health += 250
            food.re_init()
            self.score += config.SCORE * 10
            print(self.name, 'eat food! +250 HP 10x SCORE')
            return True

        self.health -= config.PLAYER_COST_STEP * 10
        self.life()
        return False

    def fix(self):
        (wall, posion, food) = self.manager.get_vision(self)
        if not posion == None:
            self.manager.poison_2_food(posion)
            print(self.name, 'fix poison! +5x SCORE')
            self.score += config.SCORE * 5
            return True

        self.health -= config.PLAYER_COST_STEP * 10
        self.life()
        return False

    def move(self):
        (wall, posion, food) = self.manager.get_vision(self)
        if wall == 1:
            self.health -= config.PLAYER_COST_STEP * 10
            self.life()
            return False

        super().move()

    def rotate(self, angle):
        if self.rotate_mem:
            self.health -= config.PLAYER_COST_STEP * 10
            self.life()
            if self.death:
                return False

        super().rotate(angle)
        self.rotate_mem = True
