from constants import *
import pygame
import player
import path
import time

pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

player_group = pygame.sprite.Group()
path_group = pygame.sprite.Group()

def main():
    global states
    running = True
    start = 0

    plyr = player.Player(32, 32)

    pth = path.Path(64, 64)

    player_group.add(plyr)
    path_group.add(pth)


    while running:
        start = time.time()
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    running = False

        draw()
        update()
        print(time.time() - start)

    pygame.quit()

def draw():
    surface.fill((200, 200, 200))
    path_group.draw(surface)
    player_group.draw(surface)


    pygame.display.flip()

def update():
    player_group.update(path_group)


if __name__ == "__main__":
    main()
