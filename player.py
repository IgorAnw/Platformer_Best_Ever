import pygame
from constants import JUMPING_SPEED, WALK_SPEED, FALLING_SPEED


class Character(pygame.sprite.Sprite):
    image = pygame.Surface([50, 50])
    image.fill(pygame.Color('white'))

    def __init__(self, group):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.y_speed = 0

    def move(self, direction):
        self.rect.x += WALK_SPEED * direction

    def update(self, inform):
        if inform is None:
            self.y_speed += FALLING_SPEED
            self.rect.y += self.y_speed
        else:
            self.rect.y += inform.rect.top - self.rect.bottom + 1
            self.y_speed = 0

    def jump(self):
        self.rect.y -= 1
        self.y_speed = -1 * JUMPING_SPEED
