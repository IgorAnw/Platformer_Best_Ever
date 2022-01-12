import pygame
from constants import *
from melee_attack import MeleeAttack
from enemy import Enemy


class Character(pygame.sprite.Sprite):
    # внешний вид
    image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
    image.fill(pygame.Color('white'))

    # Переменные
    melee_group = pygame.sprite.Group()
    melee_sprite = MeleeAttack(melee_group)
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
        self.rect.x = 200
        self.rect.y = 100
        self.y_speed = 0
        self.n_jump = False
        self.x_ram = self.rect.x
        self.y_ram = self.rect.y

    def move(self, direction):
        self.direction = direction
        self.x_ram = self.rect.x
        self.rect.x += WALK_SPEED * direction

    def update(self, inform):
        if inform is None:
            self.y_speed += FALLING_SPEED
            self.y_ram = self.rect.y
            self.rect.y += self.y_speed
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
        elif inform and self.x_ram <= self.rect.x:
            self.rect.x -= self.rect.right - inform.rect.left
            self.y_speed += FALLING_SPEED
            self.y_ram = self.rect.y
            self.rect.y += self.y_speed

        # Отвечает за ближнюю атаку
        if self.is_melee_attacking:
            if self.direction == 1:
                self.melee_sprite.rect.x = self.rect.right
                self.melee_sprite.rect.y = self.rect.top
                self.melee_group.draw(self.screen)
            if self.direction == 0:
                self.melee_sprite.rect.x = self.rect.left
                self.melee_sprite.rect.y = self.rect.top - self.melee_sprite.rect.height
                self.melee_group.draw(self.screen)
            if self.direction == -1:
                self.melee_sprite.rect.x = self.rect.left - self.melee_sprite.rect.width
                self.melee_sprite.rect.y = self.rect.top
                self.melee_group.draw(self.screen)

        if self.health_points < 1:
            self.is_alive = False

    def damage(self, enemy_group):
        inform = pygame.sprite.spritecollideany(self.melee_sprite, enemy_group)
        self.enemy_group = enemy_group
        if type(inform) == Enemy:
            inform.taking_damage()

    def jump(self):
        if self.n_jump >= 1:
            self.rect.y -= 1
            self.y_speed = -1 * JUMPING_SPEED
            self.n_jump -= 1

    # Начало и конец атаки героя
    def attack_start(self, screen):
        self.screen = screen
        self.is_melee_attacking = True

    def attack_end(self):
        self.is_melee_attacking = False
        for i in self.enemy_group.sprites():
            i.not_immortal()

    def taking_damage(self, enemy_group):
        if type(pygame.sprite.spritecollideany(self, enemy_group)) == Enemy:
            if not self.is_immortal:
                self.health_points -= 1
                self.is_immortal = True
                self.image.fill(pygame.Color('blue'))
                return True

    def not_immortal(self):
        self.is_immortal = False
        self.image.fill(pygame.Color('white'))

    def move_to(self, x, y):
        self.rect.x = x
        self.rect.y = y
