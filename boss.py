import pygame
from constants import *


class BossProjectile(pygame.sprite.Sprite):
    image = pygame.image.load('images/fireball_left.png')
    image.set_colorkey('white')

    def __init__(self, group):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.does_exist = False
        self.cool_down = 60

    def appear(self, y):
        self.image = pygame.image.load('images/fireball_left.png')
        self.image.set_colorkey('white')
        if self.cool_down <= 0:
            self.rect.x = 810
            self.rect.y = y
            self.does_exist = True
            self.cool_down = 60

    def update(self):
        if self.cool_down >= 0:
            self.cool_down -= 1
        if self.rect.x > 2000 or self.rect.x < -100:
            self.does_exist = False
        elif self.does_exist:
            self.rect.x -= 15

    def get_existing(self):
        return self.does_exist

    def not_immortal(self):
        pass


class Boss(pygame.sprite.Sprite):
    # внешний вид
    image = pygame.Surface([100, 540])
    image.fill(pygame.Color('green'))

    # перемнные
    is_immortal = False
    is_alive = True
    health_points = 10
    range_cooldown = 0

    def __init__(self, group):
        super().__init__(group)
        self.range_attack = BossProjectile(group)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 100
        self.rect.y = 0

    def shoot(self, y):
        self.range_attack.appear(y)

    def update(self, player, screen):
        self.shoot(player.rect.y)

        if self.health_points < 1:
            self.is_alive = False

    def taking_damage(self):
        if not self.is_immortal:
            self.health_points -= 1
            self.is_immortal = True
            self.image.fill('blue')
            pygame.time.set_timer(ENEMY_IMMORTALITY, 300, loops=1)

    def not_immortal(self):
        self.image.fill('green')
        self.is_immortal = False

    def cut_sheet_r(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames_move_r.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def cut_sheet_l(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames_move_l.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))