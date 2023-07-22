import pygame, random
from constants import *
import time

class Trap(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y


    def update(self):
        time.sleep(5000)
        self.kill()
