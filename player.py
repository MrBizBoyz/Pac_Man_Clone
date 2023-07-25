import pygame, random
from constants import *
import player

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.x = 64
        self.y = 64

        self.width = width
        self.height = height
        self.speed = 4.5
        self.x_speed = self.speed
        self.y_speed = 0
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,0))
        self.score = 0
        self.eat_ghost = False
        self.killable = True


        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)



    def update(self, map, dots, big_dots, ghost):
        self.key_input()
        self.move()
        self.collision(map, dots, big_dots)

        if self.rect.right < 0:
            self.rect.left = GAME_WIDTH -80

        if self.rect.left > GAME_WIDTH -80:
            self.rect.left = 0



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



    def collision(self, map, dots, big_dots):
        walls = pygame.sprite.spritecollide(self, map, False)




        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.rect.right > wall.rect.left and self.rect.left < wall.rect.left:
                    self.rect.right = wall.rect.left

                elif self.rect.left < wall.rect.right and self.rect.right > wall.rect.right:
                    self.rect.left = wall.rect.right

                if self.rect.bottom > wall.rect.top and self.rect.top < wall.rect.top:
                    self.rect.bottom = wall.rect.top

                elif self.rect.top < wall.rect.bottom and self.rect.bottom > wall.rect.bottom:
                    self.rect.top = wall.rect.bottom

        if pygame.sprite.spritecollide(self, dots, True):
            self.score += 10

        if pygame.sprite.spritecollide(self, big_dots, True):
            self.score += 50
            self.eat_ghost = True
            self.killable = False

            #create ghost



    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
