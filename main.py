from constants import *
import pygame
import player
import time
import load_level


pygame.init()
states = 0
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
flashing = False
flash_timer = 0
FLASH_INTERVAL = 300
player_group = pygame.sprite.Group()
map = load_level.Load_level()
background1_image = pygame.image.load("menu.png").convert()
background2_image = pygame.image.load("pause.png").convert()





plyr = player.Player(32, 32)

player_group.add(plyr)

def main():
    global states
    running = True
    if states == 0:
        menu()

    if states == 2:
        pause()
    start = 0




    while running:
        start = time.time()
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    running = False

                if event.key == pygame.K_p:

                    if states == 1:
                        states = 2

                    elif states == 2:
                        states = 1


                if event.key == pygame.K_SPACE:
                    if states == 0:
                        states = 1


        draw()
        update()

    pygame.quit()

def draw():
    global flashing, flash_timer, states
    if states == 0:
        menu()
    if states == 1:
        surface.fill((0, 0, 0))
        player_group.draw(surface)
        map.get_blocks().draw(surface)
        map.get_dots().draw(surface)
        map.get_big_dots().draw(surface)
        map.get_trap().draw(surface)
        map.get_ghost().draw(surface)


        draw_scores()
        draw_text()

        current_time = pygame.time.get_ticks()
        if current_time - flash_timer >= FLASH_INTERVAL:
            flashing = not flashing
            flash_timer = current_time

    if states == 2:
        pause()
    pygame.display.flip()

def update():
    global states
    if states == 0:
        pass
    if states == 1:

        player_group.update(map.get_blocks(), map.get_dots(), map.get_big_dots(), map.get_ghost())
        map.get_ghost().update(player_group)
    # map.get_trap().update()

def menu():
    surface.blit(background1_image, [0, 0])



def pause():
    surface.blit(background2_image, [0, 0])



def draw_scores():

    message_display(str(plyr.score), GAME_WIDTH - 0.001 - FONT_SIZE, FONT_SIZE)



def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()



def message_display(text, x, y):
    largeText = pygame.font.Font('font.ttf',50)
    TextSurf, TextRect = arcade_text(text, largeText)
    TextRect.center = (x, y)
    surface.blit(TextSurf, TextRect)

def draw_text():
    if not flashing:
        display("1UP", GAME_WIDTH - 0.001 - FONT_SIZE, FONT_SIZE + 50)



def arcade_text(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()



def display(text, x, y):
    largeText = pygame.font.Font('font.ttf',50)
    TextSurf, TextRect = arcade_text(text, largeText)
    TextRect.center = (x, y)
    surface.blit(TextSurf, TextRect)
if __name__ == "__main__":
    main()
