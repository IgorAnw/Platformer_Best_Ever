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
    
    def move(self, direction):
        self.rect.x += WALK_SPEED * direction
    
    def fall(self):
        self.rect.y += FALLING_SPEED

    def jump(self):
        self.rect.y -= JUMPING_SPEED
