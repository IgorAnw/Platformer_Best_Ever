import pygame
import random
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
        self.range_attack1 = BossProjectile(group)
        self.delay1 = 0
        self.cur_frame = 0
        self.running_timer = 0
        self.frames = []
        self.cut_sheet(pygame.image.load('images/boss_animation.png'), 2, 1)
        self.image = self.frames[0]
        self.image.set_colorkey('white')
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 100
        self.rect.y = 0


    def shoot(self, y):
        self.range_attack.appear(y)

    def shoot1(self, y):
        self.range_attack1.appear(y)

    def shoot2(self, y):
        self.range_attack1.appear(y)

    def update(self, player, screen):
        self.shoot(player.rect.y)
        if self.delay1 >= 90:
            self.shoot1(random.randint(0, 470))
        else:
            self.delay1 += 1

        if self.running_timer >= 5 and not self.is_immortal:
            self.image = self.frames[self.cur_frame]
            self.image.set_colorkey('white')
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.running_timer = 0
        self.running_timer += 1

        if self.health_points < 1:
            self.is_alive = False

    def taking_damage(self):
        if not self.is_immortal:
            self.image = pygame.image.load('images/boss_immortal.png')
            self.image.set_colorkey('white')
            self.health_points -= 1
            self.is_immortal = True
            pygame.time.set_timer(ENEMY_IMMORTALITY, 300, loops=1)

    def not_immortal(self):
        self.is_immortal = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
