import sys
import pygame
from constants import WIDTH, HEIGHT


class StartScreen:
    def __init__(self):
        self.background = pygame.Surface([WIDTH, HEIGHT])
        font = pygame.font.Font(None, 40)
        text = 'Best_game_ever'
        text2 = 'Press any button to start'

        self.string_rendered = font.render(text, True, pygame.Color('white'))
        self.intro_rect = self.string_rendered.get_rect()
        self.intro_rect.x = (WIDTH - self.intro_rect.width) / 2
        self.intro_rect.y = 150

        self.string_rendered2 = font.render(text2, True, pygame.Color('white'))
        self.intro_rect2 = self.string_rendered2.get_rect()
        self.intro_rect2.x = (WIDTH - self.intro_rect2.width) / 2
        self.intro_rect2.y = 300

    def show(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.string_rendered, self.intro_rect)
        screen.blit(self.string_rendered2, self.intro_rect2)


class DeadScreen:
    def __init__(self):
        self.background = pygame.Surface([WIDTH, HEIGHT])
        self.screen = None

        self.font = pygame.font.Font(None, 40)
        self.text = 'YOU DIED'
        self.text2 = '=> Restart'
        self.text3 = 'Quit game'

        self.string_rendered = self.font.render(self.text, True, pygame.Color('white'))
        self.intro_rect = self.string_rendered.get_rect()
        self.intro_rect.x = (WIDTH - self.intro_rect.width) / 2
        self.intro_rect.y = 150

        self.string_rendered2 = self.font.render(self.text2, True, pygame.Color('white'))
        self.intro_rect2 = self.string_rendered2.get_rect()
        self.intro_rect2.x = (WIDTH - self.intro_rect2.width) / 2
        self.intro_rect2.y = 350

        self.string_rendered3 = self.font.render(self.text3, True, pygame.Color('white'))
        self.intro_rect3 = self.string_rendered3.get_rect()
        self.intro_rect3.x = (WIDTH - self.intro_rect3.width) / 2
        self.intro_rect3.y = 400

    def show(self, screen):
        self.screen = screen
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.string_rendered, self.intro_rect)
        self.screen.blit(self.string_rendered2, self.intro_rect2)
        self.screen.blit(self.string_rendered3, self.intro_rect3)

    def change(self):
        if self.text2 == '=> Restart':
            self.text2 = 'Restart'
            self.text3 = '=> Quit game'
            self.string_rendered2 = self.font.render(self.text2, True, pygame.Color('white'))
            self.intro_rect2 = self.string_rendered2.get_rect()
            self.intro_rect2.x = (WIDTH - self.intro_rect2.width) / 2
            self.intro_rect2.y = 350
            self.string_rendered3 = self.font.render(self.text3, True, pygame.Color('white'))
            self.intro_rect3 = self.string_rendered3.get_rect()
            self.intro_rect3.x = (WIDTH - self.intro_rect3.width) / 2
            self.intro_rect3.y = 400

        elif self.text3 == '=> Quit game':
            self.text2 = '=> Restart'
            self.text3 = 'Quit game'
            self.string_rendered2 = self.font.render(self.text2, True, pygame.Color('white'))
            self.intro_rect2 = self.string_rendered2.get_rect()
            self.intro_rect2.x = (WIDTH - self.intro_rect2.width) / 2
            self.intro_rect2.y = 350
            self.string_rendered3 = self.font.render(self.text3, True, pygame.Color('white'))
            self.intro_rect3 = self.string_rendered3.get_rect()
            self.intro_rect3.x = (WIDTH - self.intro_rect3.width) / 2
            self.intro_rect3.y = 400

    def activate(self):
        if self.text2 == '=> Restart':
            pass
            # тут должна быть функция рестарта

        if self.text3 == '=> Quit game':
            pygame.quit()
            sys.exit()
