import pygame, random
from constants import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill((0,0,0))
        pygame.draw.rect(self.image, color, self.image.get_rect(), width=2)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
