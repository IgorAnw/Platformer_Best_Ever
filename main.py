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
obstacle1 = Platform(obstacles_group)
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
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.move(1)
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.move(-1)
    if pygame.key.get_pressed()[pygame.K_z]:
        player.jump()
    player.update(pygame.sprite.spritecollideany(player, obstacles_group))
    clock.tick(60)
    pygame.display.flip()
