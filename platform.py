import pygame


class Platform(pygame.sprite.Sprite):
    image = pygame.Surface([500, 10])
    image.fill(pygame.Color('red'))

    def __init__(self, group):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300
