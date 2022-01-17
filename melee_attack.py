import pygame


class MeleeAttack(pygame.sprite.Sprite):

    def __init__(self, group):
        self.frames = []
        self.running_timer = 0
        self.cur_frame = 0
        self.cut_sheet(pygame.image.load('images/melee_attack_right.png'), 3, 1)
        self.image = self.frames[self.cur_frame]
        self.image.set_colorkey('white')
        super().__init__(group)
        self.rect = self.image.get_rect()

    def update(self):
        if self.running_timer >= 5:
            self.image = self.frames[self.cur_frame]
            self.image.set_colorkey('white')
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.running_timer = 0
        self.running_timer += 1

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))