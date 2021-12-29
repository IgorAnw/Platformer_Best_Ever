import pygame
import sys
from player import character

all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

while True:
    pygame.init()
    screen = pygame.display.set_mode([960, 540])
    screen.fill('#000000')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move(1)
                
    player = character(all_sprites)
    all_sprites.draw(screen)

    pygame.display.flip()