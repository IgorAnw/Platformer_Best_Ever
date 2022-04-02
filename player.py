import pygame
from constants import *
from melee_attack import MeleeAttack
from projectile import ProjectileAttack
from enemy import Enemy
from boss import Boss, BossProjectile


class Character(pygame.sprite.Sprite):
    # внешний вид
    image = pygame.image.load('images/player_staying_right.png')
    image.set_colorkey('white')

    # Переменные
    melee_group = pygame.sprite.Group()
    melee_sprite = MeleeAttack(melee_group)
    projectile_group = pygame.sprite.Group()
    projectile_sprite = ProjectileAttack(projectile_group)
    screen = None
    is_melee_attacking = False
    direction = 1
    enemy_group = None
    is_immortal = False
    is_alive = True
    health_points = 5

    def __init__(self, group):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 350
        self.y_speed = 0
        self.n_jump = 0
        self.x_ram = self.rect.x
        self.y_ram = self.rect.y
        self.is_moving = False
        self.is_jumping = False
        self.cur_frame_running_right = 0
        self.frames_run_r = []
        self.cut_sheet_run_right(pygame.image.load('images/player_run_animation_right.png'), 8, 1)
        self.cur_frame_running_left = 0
        self.frames_run_l = []
        self.cut_sheet_run_left(pygame.image.load('images/player_run_animation_left.png'), 8, 1)
        self.running_timer = 0

    def move(self, direction):
        self.direction = direction
        self.x_ram = self.rect.x
        self.rect.x += WALK_SPEED * direction
        self.is_moving = True

    def update(self, inform, screen):
        self.screen = screen

        if inform is None:
            self.y_speed += FALLING_SPEED
            self.y_ram = self.rect.y
            self.rect.y += self.y_speed
            self.is_jumping = True
        if inform and self.y_ram <= self.rect.y and self.y_ram + PLAYER_HEIGHT <= inform.rect.top:
            self.rect.y += inform.rect.top - self.rect.bottom + 1
            self.y_speed = 0
            self.n_jump = 2
        elif inform and self.y_ram > self.rect.y and self.y_ram >= inform.rect.bottom:
            self.rect.y += inform.rect.bottom - self.rect.y + 1
            self.y_speed = 0
        elif inform and self.x_ram >= self.rect.x:
            self.rect.x += inform.rect.right - self.rect.left
            self.y_speed += FALLING_SPEED
            self.y_ram = self.rect.y
            self.rect.y += self.y_speed
            self.is_jumping = True
        elif inform and self.x_ram <= self.rect.x:
            self.rect.x -= self.rect.right - inform.rect.left
            self.y_speed += FALLING_SPEED
            self.y_ram = self.rect.y
            self.rect.y += self.y_speed
            self.is_jumping = True

        # Отвечает за ближнюю атаку
        if self.is_melee_attacking:
            if self.direction == 1:
                self.image = pygame.image.load('images/player_melee_right.png')
                self.image.set_colorkey('white')
                self.melee_sprite.frames = []
                self.melee_sprite.cut_sheet(pygame.image.load('images/melee_attack_right.png'), 3, 1)
                self.melee_sprite.update()
                self.melee_sprite.rect.x = self.rect.right
                self.melee_sprite.rect.y = self.rect.top
                self.melee_group.draw(self.screen)
            if self.direction == 0:
                self.image = pygame.image.load('images/player_melee_up.png')
                self.image.set_colorkey('white')
                self.melee_sprite.frames = []
                self.melee_sprite.cut_sheet(pygame.image.load('images/melee_attack_up.png'), 3, 1)
                self.melee_sprite.update()
                self.melee_sprite.rect.x = self.rect.left
                self.melee_sprite.rect.y = self.rect.top - self.melee_sprite.rect.height
                self.melee_group.draw(self.screen)
            if self.direction == -1:
                self.image = pygame.image.load('images/player_melee_left.png')
                self.image.set_colorkey('white')
                self.melee_sprite.frames = []
                self.melee_sprite.cut_sheet(pygame.image.load('images/melee_attack_left.png'), 3, 1)
                self.melee_sprite.update()
                self.melee_sprite.rect.x = self.rect.left - self.melee_sprite.rect.width
                self.melee_sprite.rect.y = self.rect.top
                self.melee_group.draw(self.screen)

        if self.health_points < 1:
            self.is_alive = False

        # методы класса снаряда
        self.projectile_sprite.update()
        if self.projectile_sprite.get_existing():
            self.projectile_group.draw(self.screen)
        # Анимация
        if self.direction == 0 and not self.is_jumping and self.is_moving and not self.is_melee_attacking:
            self.image = pygame.image.load('images/player_staying_right.png')
            self.image.set_colorkey('white')
        elif self.direction == 0 and not self.is_jumping and not self.is_moving and not self.is_melee_attacking:
            self.image = pygame.image.load('images/player_staying_right.png')
            self.image.set_colorkey('white')
        elif self.direction == 1 and not self.is_jumping and not self.is_moving and not self.is_melee_attacking:
            self.image = pygame.image.load('images/player_staying_right.png')
            self.image.set_colorkey('white')
        elif self.direction == -1 and not self.is_jumping and not self.is_moving and not self.is_melee_attacking:
            self.image = pygame.image.load('images/player_staying_left.png')
            self.image.set_colorkey('white')
        elif self.direction == 1 and self.is_moving and not self.is_jumping and self.running_timer >= 5 and not self.is_melee_attacking:
            self.image = self.frames_run_r[self.cur_frame_running_right]
            self.image.set_colorkey('white')
            self.cur_frame_running_right = (self.cur_frame_running_right + 1) % len(self.frames_run_r)
            self.running_timer = 0
        elif self.direction == -1 and self.is_moving and not self.is_jumping and self.running_timer >= 5 and not self.is_melee_attacking:
            self.image = self.frames_run_l[self.cur_frame_running_left]
            self.image.set_colorkey('white')
            self.cur_frame_running_left = (self.cur_frame_running_left + 1) % len(self.frames_run_l)
            self.running_timer = 0
        elif self.direction == 0 and self.is_jumping and self.is_moving and not self.is_melee_attacking:
            self.image = pygame.image.load('images/player_jumping_right.png')
            self.image.set_colorkey('white')
        elif self.direction == 1 and self.is_jumping and self.is_moving and not self.is_melee_attacking:
            self.image = pygame.image.load('images/player_jumping_right.png')
            self.image.set_colorkey('white')
        elif self.direction == -1 and self.is_jumping and self.is_moving and not self.is_melee_attacking:
            self.image = pygame.image.load('images/player_jumping_left.png')
            self.image.set_colorkey('white')
        elif self.is_jumping and not self.is_moving and not self.is_melee_attacking:
            self.image = pygame.image.load('images/player_jumping_right.png')
            self.image.set_colorkey('white')

        self.running_timer += 1
        self.is_moving = False
        self.is_jumping = False

    def damage(self, enemy_group):
        inform_melee = pygame.sprite.spritecollideany(self.melee_sprite, enemy_group)
        inform_projectile = pygame.sprite.spritecollideany(self.projectile_sprite, enemy_group)
        self.enemy_group = enemy_group
        if type(inform_melee) == Enemy or type(inform_melee) == Boss:
            inform_melee.taking_damage()
        if type(inform_projectile) == Enemy or type(inform_projectile) == Boss:
            inform_projectile.taking_damage()

    def jump(self):
        if self.n_jump >= 1:
            self.rect.y -= 1
            self.y_speed = -1 * JUMPING_SPEED
            self.n_jump -= 1

    # Начало и конец атаки героя
    def attack_start(self):
        self.is_melee_attacking = True

    def attack_end(self):
        self.is_melee_attacking = False
        self.melee_sprite.rect.x = -100
        self.melee_sprite.rect.y = -100

    def taking_damage(self, enemy_group):
        if type(pygame.sprite.spritecollideany(self, enemy_group)) == Enemy \
                or type(pygame.sprite.spritecollideany(self, enemy_group)) == Boss \
                or type(pygame.sprite.spritecollideany(self, enemy_group)) == BossProjectile:
            if not self.is_immortal:
                self.health_points -= 1
                self.is_immortal = True
                return True

    def not_immortal(self):
        self.is_immortal = False

    def move_to(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def take_fall_damage(self):
        self.health_points -= 1
        self.move_to(BRICK_SIZE + 5, 350)

    def shoot(self):
        if self.direction == 1:
            self.projectile_sprite.appear(self.rect.x + self.rect.width, self.rect.y, self.direction)
        elif self.direction == -1:
            self.projectile_sprite.appear(self.rect.x - self.projectile_sprite.rect.width, self.rect.y, self.direction)

    def cut_sheet_run_right(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames_run_r.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def cut_sheet_run_left(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames_run_l.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))