import pygame
from brick import Brick
from constants import *


class Location:
    map_text = open('location_memory').read().split('\n')

    def __init__(self, obst_group):
        self.obst_group = obst_group

    def build(self):
        for i1 in range(Y_BRICKS):
            for i in range(X_BRICKS):
                if self.map_text[i1][i] == '1':
                    obstacle = Brick(self.obst_group, BRICK_SIZE * i, BRICK_SIZE * i1)