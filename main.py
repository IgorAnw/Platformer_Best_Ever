import pygame
import sys
from player import Character
from constants import *
from brick import Brick
from enemy import Enemy
from start_screen import start_screen
from location import Location
import random


def random_path():
    path = '0'
    n = 5
    for i in range(5):
        path += str(random.randint(1, 5))
    return path


player_group = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
clock = pygame.time.Clock()
is_start_screen = True

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
player = Character(player_group)
order_now = 0
pathing = random_path()
loc = Location(obstacles_group, enemy_group, pathing[order_now])
loc.build()

while True:
    screen.fill('black')
    if player.is_alive:
        player_group.draw(screen)
    if player.rect.center[0] > WIDTH:
        order_now += 1
        obstacles_group = pygame.sprite.Group()
        enemy_group = pygame.sprite.Group()
        print(pathing[order_now])
        loc = Location(obstacles_group, enemy_group, pathing[order_now])
        loc.build()
        player.move_to(0, 350)
    if player.rect.center[0] < 0:
        order_now -= 1
        obstacles_group = pygame.sprite.Group()
        enemy_group = pygame.sprite.Group()
        loc = Location(obstacles_group, enemy_group, pathing[order_now])
        loc.build()
        player.move_to(WIDTH - 50, 350)
    obstacles_group.draw(screen)
    enemy_group.draw(screen)
    for i in enemy_group.sprites():
        if i.is_alive:
            i.move()
        else:
            i.rect.x = -200
            i.rect.y = -200

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                player.jump()

        # Отвечает за ближнюю атаку
        if event.type == pygame.KEYDOWN:
            is_start_screen = False
            if event.key == pygame.K_x:
                player.attack_start(screen)
                pygame.time.set_timer(ATTACK_END, 250, loops=1)

        if event.type == ATTACK_END:
            player.attack_end()

        if event.type == PLAYER_IMMORTALITY:
            player.not_immortal()

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.move(1)
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.move(-1)
    if pygame.key.get_pressed()[pygame.K_UP]:
        player.move(0)

    if player.rect.y > HEIGHT:
        player.take_fall_damage()
    player.damage(enemy_group)
    if player.taking_damage(enemy_group):
        pygame.time.set_timer(PLAYER_IMMORTALITY, 1000, loops=1)
    player.update(pygame.sprite.spritecollideany(player, obstacles_group))

    if is_start_screen:
        start_screen(screen)

    clock.tick(FPS)
    pygame.display.flip()
