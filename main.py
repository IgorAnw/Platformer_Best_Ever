import pygame
import sys
from player import Character
from constants import *
from brick import Brick
from enemy import Enemy

player_group = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
player = Character(player_group)
enemy = Enemy(enemy_group, 100, 100, 2, 1, 100)
for i in range(38):
    obstacle = Brick(obstacles_group, 100 + i * BRICK_SIZE, 500)
for i in range(10):
    obstacle = Brick(obstacles_group, 100 + i * BRICK_SIZE, 200)
for i in range(10):
    obstacle = Brick(obstacles_group, 500 + i * BRICK_SIZE, 200)

while True:
    screen.fill('black')
    if player.is_alive:
        player_group.draw(screen)
    obstacles_group.draw(screen)

    enemy_group.draw(screen)
    for i in enemy_group.sprites():
        if i.is_alive:
            i.move(pygame.sprite.spritecollideany(enemy, obstacles_group))
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

    player.damage(enemy_group)
    if player.taking_damage(enemy_group):
        pygame.time.set_timer(PLAYER_IMMORTALITY, 1000, loops=1)
    player.update(pygame.sprite.spritecollideany(player, obstacles_group))

    clock.tick(60)
    pygame.display.flip()
