import pygame

class character(pygame.sprite.Sprite):
    image = pygame.Surface([50, 50])
    image.fill(pygame.Color('white'))

    def __init__(self, group):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
    
    def move(self, direction):
        self.rect.x += 10 * direction
    
    def fall(self):
        self.rect.y += 5
