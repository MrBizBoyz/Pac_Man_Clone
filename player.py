import pygame, random
from constants import *
import player

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT
        self.width = width
        self.height = height
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)

        self.move_x = 0
        self.move_y = 0

    def update(self):
        self.key_input()
        self.move()



    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.move_x = -self.speed
            self.move_y = 0

        elif keys[pygame.K_RIGHT]:

            self.move_x = self.speed
            self.move_y = 0
        elif keys[pygame.K_UP] :

            self.move_x = 0
            self.move_y = -self.speed
        elif keys[pygame.K_DOWN]:

            self.move_x = 0
            self.move_y = self.speed



    def move(self):

        if 0 <= self.rect.left + self.move_x <= GAME_WIDTH - self.width:
            self.rect.x += self.move_x
        if 0 <= self.rect.top + self.move_y <= GAME_HEIGHT - self.height:
            self.rect.y += self.move_y
