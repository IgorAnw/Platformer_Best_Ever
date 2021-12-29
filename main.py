import pygame
import sys
from player import Character

all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([960, 540])
player = Character(all_sprites)
is_jump = False

while True:
    screen.fill('#000000')
    all_sprites.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_d]:
        player.move(1)
    if pygame.key.get_pressed()[pygame.K_a]:
        player.move(-1)
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        player.jump()

    if is_jump:
        player.jump()
        is_jump = False
    player.fall()

    clock.tick(60)
    pygame.display.flip()
