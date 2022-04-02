import pygame
from constants import *


class Brick(pygame.sprite.Sprite):
    image = pygame.image.load('images/bricks_sprite.png')

    def __init__(self, group, x, y):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y