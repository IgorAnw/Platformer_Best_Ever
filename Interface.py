import pygame
from constants import WIDTH, HEIGHT


class StartScreen:
    def __init__(self):
        self.background = pygame.Surface([WIDTH, HEIGHT])
        self.screen = None

        self.font = pygame.font.Font(None, 40)
        self.text = 'Welcome'
        self.text2 = '=> Start'
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
        if self.text2 == '=> Start':
            self.text2 = 'Start'
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
            self.text2 = '=> Start'
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
        if self.text2 == '=> Start':
            return 'r'
        if self.text3 == '=> Quit game':
            return 'q'


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
            return 'r'
        if self.text3 == '=> Quit game':
            return 'q'


class VictoryScreen:
    def __init__(self):
        self.background = pygame.Surface([WIDTH, HEIGHT])
        self.screen = None

        self.font = pygame.font.Font(None, 40)
        self.text = 'You Won!!!'
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
            return 'r'
        if self.text3 == '=> Quit game':
            return 'q'


class HpBar:
    def __init__(self):
        self.image = pygame.Surface([15, 30])
        self.image.fill(pygame.Color('red'))

    def draw(self, screen, hp):
        for i in range(hp):
            screen.blit(self.image, (10 + 18 * i, 10))
