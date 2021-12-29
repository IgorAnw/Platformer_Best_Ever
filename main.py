import pygame
import sys
from player import character

all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([960, 540])
player = character(all_sprites)

while True:
    screen.fill('#000000')
    all_sprites.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move(1)

        # Работает не так как надо, но требуется что то в этом роде
        # if pygame.key.get_pressed()[pygame.K_d]:
        #     player.move(1)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move(-1)

    player.fall()

    clock.tick(60)
    pygame.display.flip()