import pygame


class ProjectileAttack(pygame.sprite.Sprite):
    image = pygame.image.load('images/fireball_right.png')
    image.set_colorkey('white')

    def __init__(self, group):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.does_exist = False
        self.direction = 1
        self.cool_down = 0

    def appear(self, x, y, direction):
        if direction == 1:
            self.image = pygame.image.load('images/fireball_right.png')
            self.image.set_colorkey('white')
        if direction == -1:
            self.image = pygame.image.load('images/fireball_left.png')
            self.image.set_colorkey('white')
        if self.cool_down <= 0:
            self.rect.x = x
            self.rect.y = y
            self.does_exist = True
            self.direction = direction
            self.cool_down = 300

    def update(self):
        if self.cool_down >= 0:
            self.cool_down -= 1
        if self.rect.x > 2000 or self.rect.x < -100:
            self.does_exist = False
        elif self.does_exist:
            self.rect.x += 15 * self.direction

    def get_existing(self):
        return self.does_exist