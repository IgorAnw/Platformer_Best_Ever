import pygame
from constants import FALLING_SPEED


class Enemy(pygame.sprite.Sprite):
    # внешний вид
    image = pygame.Surface([50, 50])
    image.fill(pygame.Color('green'))

    # перемнные
    direction = 1
    is_immortal = False
    is_alive = True
    health_points = 3

    def __init__(self, group, x, y, speed_x, speed_y, time):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.time = time
        self.rear = False
        self.timer = 0

    def move(self):
        self.timer += 1
        if self.timer == self.time:
            self.timer = 0
            self.speed_x *= -1
            self.speed_y *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.health_points < 1:
            self.is_alive = False

    # Почему то умирает на 1 удар быстрее нужного
    def taking_damage(self):
        if not self.is_immortal:
            self.health_points -= 1
            self.is_immortal = True
            self.image.fill((10, 100, 10))

    def not_immortal(self):
        self.image.fill((0, 255, 0))
        self.is_immortal = False

    def move(self, inform):
        self.update(inform)
        self.walk(inform)
