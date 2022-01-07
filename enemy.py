import pygame
from constants import ENEMY_WALK_SPEED, FALLING_SPEED


class Enemy(pygame.sprite.Sprite):
    # внешний вид
    image = pygame.Surface([50, 50])
    image.fill(pygame.Color('green'))

    # перемнные
    direction = 1
    is_immortal = False
    is_alive = True
    health_points = 3

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
            self.rect.x += ENEMY_WALK_SPEED * self.direction

    def update(self, inform):
        if inform is None:
            self.y_speed += FALLING_SPEED
            self.rect.y += self.y_speed
        else:
            self.rect.y += inform.rect.top - self.rect.bottom + 1
            self.y_speed = 0

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
