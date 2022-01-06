import pygame


class MeleeAttack(pygame.sprite.Sprite):
    image = pygame.Surface([50, 50])
    image.fill(pygame.Color('red'))

    def __init__(self, group):
        super().__init__(group)
        self.rect = self.image.get_rect()
