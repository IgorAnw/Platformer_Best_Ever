import pygame
import sys
from player import Character
from constants import *
from brick import Brick
from enemy import Enemy
from Interface import *
from location import Location
import random


def random_path():
    path = 's'
    n = 5
    for i in range(5):
        path += str(random.randint(1, 5))
    return path + 'l'

pygame.init()
player_group = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
clock = pygame.time.Clock()

start_screen = StartScreen()
dead_screen = DeadScreen()
is_start_screen = True
is_dead_screen = False

screen = pygame.display.set_mode([WIDTH, HEIGHT])
player = Character(player_group)
order_now = 0
enemies_alive = True
pathing = random_path()
loc = Location(obstacles_group, enemy_group, pathing[order_now])
loc.build(enemies_alive)

while True:
    screen.fill('black')
    if player.is_alive:
        player_group.draw(screen)
    else:
        is_dead_screen = True
    if player.rect.center[0] > WIDTH:
        enemies_alive = True
        order_now += 1
        obstacles_group = pygame.sprite.Group()
        enemy_group = pygame.sprite.Group()
        loc = Location(obstacles_group, enemy_group, pathing[order_now])
        loc.build(enemies_alive)
        player.move_to(BRICK_SIZE + 5, 350)
    if player.rect.center[0] < 0:
        enemies_alive = False
        order_now -= 1
        obstacles_group = pygame.sprite.Group()
        enemy_group = pygame.sprite.Group()
        loc = Location(obstacles_group, enemy_group, pathing[order_now])
        loc.build(enemies_alive)
        player.move_to(WIDTH - BRICK_SIZE - 5, 350)

    enemies_check = 0
    for i in enemy_group.sprites():
        if i.is_alive:
            i.move()
            enemies_check += 1
        else:
            i.rect.x = -200
            i.rect.y = -200

    if enemies_check == 0 and enemies_alive:
        enemies_alive = False
        obstacles_group = pygame.sprite.Group()
        loc = Location(obstacles_group, enemy_group, pathing[order_now])
        loc.build(enemies_alive)

    obstacles_group.draw(screen)
    enemy_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                player.jump()
                if is_dead_screen:
                    dead_screen.activate()

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

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN) and is_dead_screen:
                dead_screen.change()

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
        start_screen.show(screen)
    if is_dead_screen:
        dead_screen.show(screen)

    clock.tick(FPS)
    pygame.display.flip()
