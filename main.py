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
enemy = Enemy(enemy_group)
for i in range(38):
    obstacle = Brick(obstacles_group, 100 + i * BRICK_SIZE, 500)
for i in range(10):
    obstacle = Brick(obstacles_group, 100 + i * BRICK_SIZE, 200)
for i in range(10):
    obstacle = Brick(obstacles_group, 500 + i * BRICK_SIZE, 200)

while True:
    screen.fill('black')
    player_group.draw(screen)
    obstacles_group.draw(screen)
    enemy_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                player.jump()

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.move(1)
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.move(-1)

    enemy.move(pygame.sprite.spritecollideany(enemy, obstacles_group))
    player.update(pygame.sprite.spritecollideany(player, obstacles_group))
    clock.tick(60)

    pygame.display.flip()
