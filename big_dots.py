import pygame, random
from constants import *



class Big_dots(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)  # Use SRCALPHA for transparency support
        self.color = color
        self.draw_circle()  # Draw the circle on initialization
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def draw_circle(self):
        radius = 8  # Half the size of the surface to create a circle with a diameter of 16
        center = (radius, radius)
        pygame.draw.circle(self.image, self.color, center, radius)
