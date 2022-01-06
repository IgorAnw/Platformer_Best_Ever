import pygame
from constants import JUMPING_SPEED, WALK_SPEED, FALLING_SPEED
from melee_attack import MeleeAttack
from enemy import Enemy


class Character(pygame.sprite.Sprite):
    image = pygame.Surface([50, 50])
    image.fill(pygame.Color('white'))

    melee_group = pygame.sprite.Group()
    melee_sprite = MeleeAttack(melee_group)
    screen = None
    is_melee_attacking = False
    direction = 1

    def __init__(self, group):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.y_speed = 0

    def move(self, direction):
        self.direction = direction
        self.rect.x += WALK_SPEED * direction

    def update(self, inform):
        if inform is None:
            self.y_speed += FALLING_SPEED
            self.rect.y += self.y_speed
        else:
            self.rect.y += inform.rect.top - self.rect.bottom + 1
            self.y_speed = 0

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

    def damage(self, enemy_group):
        inform = pygame.sprite.spritecollideany(self.melee_sprite, enemy_group)
        if type(inform) == Enemy:
            inform.taking_damage()
        # Доработать, чтобы враг получал только 1 еденицу урона за раз

    def jump(self):
        self.rect.y -= 1
        self.y_speed = -1 * JUMPING_SPEED

    # Начало и конец атаки героя
    def attack_start(self, screen):
        self.screen = screen
        self.is_melee_attacking = True

    def attack_end(self):
        self.is_melee_attacking = False
