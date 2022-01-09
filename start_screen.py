import pygame
from constants import WIDTH, HEIGHT


def start_screen(screen):
    background = pygame.Surface([WIDTH, HEIGHT])
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 40)
    text = 'Best_game_ever'
    text2 = 'Press any button to start'

    string_rendered = font.render(text, True, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = (WIDTH - intro_rect.width) / 2
    intro_rect.y = 150

    string_rendered2 = font.render(text2, True, pygame.Color('white'))
    intro_rect2 = string_rendered2.get_rect()
    intro_rect2.x = (WIDTH - intro_rect2.width) / 2
    intro_rect2.y = 300

    screen.blit(string_rendered, intro_rect)
    screen.blit(string_rendered2, intro_rect2)
