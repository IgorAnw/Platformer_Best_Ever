import pygame
from constants import WALK_SPEED, FALLING_SPEED


class Enemy(pygame.sprite.Sprite):
    image = pygame.Surface([50, 50])
    image.fill(pygame.Color('green'))
    direction = 1

    def __init__(self, group):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 200
        self.y_speed = 0

    def walk(self, inform):
        if inform is not None:
            if inform.rect.right < self.rect.right:
                self.direction = -1
            elif inform.rect.left > self.rect.left:
                self.direction = 1
            self.rect.x += 3 * self.direction

    def update(self, inform):
        if inform is None:
            self.y_speed += FALLING_SPEED
            self.rect.y += self.y_speed
        elif inform.rect.top == self.rect.bottom:
            pass

    def move(self, inform):
        self.update(inform)
        self.walk(inform)
