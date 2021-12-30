import pygame
import sys
from player import Character
from constants import WIDTH, HEIGHT
from platform import Platform

player_group = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
player = Character(player_group)
obstacle = Platform(obstacles_group)
qq_r = False
qq_l = False

while True:
    screen.fill('black')
    player_group.draw(screen)
    obstacles_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                qq_r = True
            if event.key == pygame.K_LEFT:
                qq_l = True
            if event.key == pygame.K_z:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                qq_r = False
            if event.key == pygame.K_LEFT:
                qq_l = False
    if qq_r:
        player.move(1)
    if qq_l:
        player.move(-1)
    player.update(pygame.sprite.spritecollideany(player, obstacles_group))
    clock.tick(60)
    pygame.display.flip()
