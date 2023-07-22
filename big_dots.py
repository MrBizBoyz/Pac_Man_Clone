import pygame, random
from constants import *

class Big_dots(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((16, 16))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
