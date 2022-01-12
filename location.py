from brick import Brick
from constants import *
from enemy import Enemy


class Location:
    def __init__(self, obst_group, enemy_group, arg):
        self.obst_group = obst_group
        self.enemy_group = enemy_group
        self.map_text = open('location_' + arg).read().split('\n')

    def build(self):
        for i1 in range(Y_BRICKS):
            for i in range(X_BRICKS):
                if self.map_text[i1][i] == '1':
                    obstacle = Brick(self.obst_group, BRICK_SIZE * i, BRICK_SIZE * i1)
        try:
            for i in self.map_text[27:]:
                args = i.split()
                enemy = Enemy(self.enemy_group, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]))
        finally:
            pass
