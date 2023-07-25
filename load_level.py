from constants import *
import pygame
import wall
import dots
import big_dots
import ghost_trap
import ghost


class Load_level():
    def __init__(self):
        self.blocks = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.big_dots = pygame.sprite.Group()
        self.ghost = pygame.sprite.Group()
        self.trap = pygame.sprite.Group()
        self.level = "level.txt"
        self.load_level(self.level)

    def load_level(self, level):
        r, c = 0, 0

        with open(level, "r") as file:
            lines = file.readlines()

            for line in lines:
                for letter in line:
                    if letter == ",":
                        continue
                    if letter == "W":
                        self.blocks.add(wall.Wall(c * BLOCK_SIZE, r * BLOCK_SIZE, BLUE))

                    if letter == "-":
                        self.dots.add(dots.Dots(c * BLOCK_SIZE + 15, r * BLOCK_SIZE + 15, (255, 192, 203)))

                    if letter == "C":
                        self.big_dots.add(big_dots.Big_dots(c * BLOCK_SIZE + 8 , r * BLOCK_SIZE + 8, (255, 192, 203)))

                    if letter == "T":
                        self.trap.add(ghost_trap.Trap(c * BLOCK_SIZE , r * BLOCK_SIZE, (255, 192, 203)))

                    if letter == "G":
                        self.ghost.add(ghost.Ghost(c * BLOCK_SIZE , r * BLOCK_SIZE, (255, 192, 203)))



                    c += 1

                r += 1
                c = 0


    def get_blocks(self):
        return self.blocks

    def get_dots(self):
        return self.dots

    def get_big_dots(self):
        return self.big_dots

    def get_trap(self):
        return self.trap

    def get_ghost(self):
        return self.ghost
