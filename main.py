import pygame
import sys
from player import Character
from constants import WIDTH, HEIGHT

player_group = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
player = Character(player_group)

while True:
    screen.fill('#000000')
    player_group.draw(screen)

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

    if pygame.sprite.spritecollideany(player, obstacles_group) is None:
        player.fall()
    elif pygame.sprite.spritecollideany(player, obstacles_group).rect.top == player.rect.bottom:
        pass

    clock.tick(60)
    pygame.display.flip()
