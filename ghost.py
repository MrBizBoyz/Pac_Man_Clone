import pygame
import random
import time

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.color = color
        self.width, self.height = 30, 30
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.eatable = False


    def update(self, player):
        self.eat(player)
        if self.eatable:
            self.flash_color()
        else:
            self.image.fill(self.color)

    def eat(self, player):
        for p in player:
            if p.eat_ghost:
                self.eatable = True
            if p.killable:
                if pygame.sprite.spritecollide(self, player, True):
                    p.kill()




        if self.eatable == True and pygame.sprite.spritecollide(self, player, False):
            self.kill()


    def flash_color(self):
        orange = (255, 165, 0)
        blue = (0, 0, 255)
        current_time = pygame.time.get_ticks()
        if current_time % 1000 < 500:
            self.image.fill(orange)
        else:
            self.image.fill(blue)
