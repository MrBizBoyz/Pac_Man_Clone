from constants import *
import pygame
import player

pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

player_group = pygame.sprite.Group()

def main():
    global states
    running = True

    # Create an instance of the Player class
    player_instance = player.Player(64, 64)
    # Add the player instance to the player_group
    player_group.add(player_instance)

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    running = False

        draw()
        update()

    pygame.quit()

def draw():
    surface.fill((200, 200, 200))
    player_group.draw(surface)
    pygame.display.flip()

def update():
    player_group.update()

if __name__ == "__main__":
    main()
