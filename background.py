import pygame


class Background(pygame.sprite.Sprite):
    background = pygame.image.load('images/background.png')
    background_scaled = pygame.transform.scale(background, (960, 540))
    image = background_scaled

    def __init__(self, group):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0