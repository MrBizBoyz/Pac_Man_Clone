import pygame, random
from constants import *
import player

class Path(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT
        self.width = width
        self.height = height
        self.speed = 3
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0, 0 ,0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)
