import pygame
from constants import *


class Enemy(pygame.sprite.Sprite):
    # внешний вид
    image = pygame.Surface([50, 30])
    image.fill(pygame.Color('green'))

    # перемнные
    direction = 1
    is_immortal = False
    is_alive = True
    health_points = 3

    def __init__(self, group, x, y, speed_x, speed_y, time):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.time = time
        self.rear = False
        self.timer = 0
        self.cur_frame = 0
        self.running_timer = 0
        self.frames_move_r = []
        self.frames_move_l = []
        self.cut_sheet_r(pygame.image.load('images/enemy_move_right.png'), 2, 1)
        self.cut_sheet_l(pygame.image.load('images/enemy_move_left.png'), 2, 1)
        self.move_to()

    def move_to(self):
        self.rect.x = self.x
        self.rect.y = self.y
    def move(self):
        self.timer += 1
        if self.timer == self.time:
            self.timer = 0
            self.speed_x *= -1
            self.speed_y *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.running_timer >= 5 and not self.is_immortal:
            if self.speed_x >= 0:
                self.image = self.frames_move_r[self.cur_frame]
            if self.speed_x < 0:
                self.image = self.frames_move_l[self.cur_frame]
            self.image.set_colorkey('white')
            self.cur_frame = (self.cur_frame + 1) % len(self.frames_move_r)
            self.running_timer = 0
        self.running_timer += 1

        if self.health_points < 1:
            self.is_alive = False

    def taking_damage(self):
        if not self.is_immortal:
            self.health_points -= 1
            self.is_immortal = True
            if self.speed_x < 0 :
                self.image = pygame.image.load('images/enemy_take_damage_l.png')
            elif self.speed_x >= 0:
                self.image = pygame.image.load('images/enemy_take_damage_r.png')
            self.image.set_colorkey('white')
            pygame.time.set_timer(ENEMY_IMMORTALITY, 300, loops=1)

    def not_immortal(self):
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