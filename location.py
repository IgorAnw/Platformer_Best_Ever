from brick import Brick
from constants import *
from enemy import Enemy
from boss import Boss


class Location:
    def __init__(self, obst_group, enemy_group, arg):
        self.obst_group = obst_group
        self.enemy_group = enemy_group
        self.map_text = open('location_' + arg).read().split('\n')
        self.n_enemies = 0
        self.enemy_room = False
        self.arg = arg

    def build(self, enemies_alive):
        for i1 in range(Y_BRICKS):
            for i in range(X_BRICKS):
                if self.map_text[i1][i] == '1':
                    obstacle = Brick(self.obst_group, BRICK_SIZE * i, BRICK_SIZE * i1)
        try:
            if enemies_alive == '1':
                for i in self.map_text[27:]:
                    args = i.split()
                    enemy = Enemy(self.enemy_group, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]))
                    self.enemy_room = True
        except BaseException:
            pass
        if self.arg == 'l':
            boss = Boss(self.enemy_group)
        if enemies_alive == '1':
            br0 = Brick(self.obst_group, 0, 340)
            br1 = Brick(self.obst_group, 0, BRICK_SIZE * 1 + 340)
            br2 = Brick(self.obst_group, 0, BRICK_SIZE * 2 + 340)
            br3 = Brick(self.obst_group, 0, BRICK_SIZE * 3 + 340)
            br4 = Brick(self.obst_group, WIDTH - BRICK_SIZE, BRICK_SIZE * 0 + 340)
            br5 = Brick(self.obst_group, WIDTH - BRICK_SIZE, BRICK_SIZE * 1 + 340)
            br6 = Brick(self.obst_group, WIDTH - BRICK_SIZE, BRICK_SIZE * 2 + 340)
            br7 = Brick(self.obst_group, WIDTH - BRICK_SIZE, BRICK_SIZE * 3 + 340)
        else:
            if self.arg != 's':
                br0 = Brick(self.obst_group, BRICK_SIZE, 420)
                br1 = Brick(self.obst_group, BRICK_SIZE * 2, 420)
                br2 = Brick(self.obst_group, BRICK_SIZE * 3, 420)
            if self.arg != 'l':
                br3 = Brick(self.obst_group, WIDTH - BRICK_SIZE * 2, 420)
                br4 = Brick(self.obst_group, WIDTH - BRICK_SIZE * 3, 420)
                br5 = Brick(self.obst_group, WIDTH - BRICK_SIZE * 4, 420)