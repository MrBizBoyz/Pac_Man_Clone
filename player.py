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
        self.speed = 3
        self.x_speed = self.speed
        self.y_speed = 0
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))


        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)



    def update(self, path_group):
        self.key_input()
        self.move()
        # self.collide(path_group)



    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x_speed = -self.speed
            self.y_speed = 0

        elif keys[pygame.K_RIGHT]:

            self.x_speed = self.speed
            self.y_speed = 0
        elif keys[pygame.K_UP] :

            self.x_speed = 0
            self.y_speed = -self.speed

        elif keys[pygame.K_DOWN]:

            self.x_speed = 0
            self.y_speed = self.speed

    # def collide(self, path_group):
    #     for p in path_group:
    #         if self.rect.top >= p.rect.top:
    #             return pygame.sprite.collide_rect(up, top)


    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
