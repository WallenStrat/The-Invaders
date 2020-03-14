import pygame

from Game import *
from constants import *

screen = 0
game = 0


def update():
    game.update()
    pygame.event.get()


def draw():
    game.draw()
    pygame.display.update()


def init():
    global screen
    global game
    game = Game(WIDTH, HEIGHT, CAPTION)
    game.run()
    # screen = game.get_screen()


def main():
    init()
    running = True
    clock = pygame.time.Clock()
    while running:
        if pygame.event.get(pygame.QUIT):
            running = False
        update()
        draw()
        clock.tick(60)
        print(clock.get_time())
        # print("tick " + str(pygame.time.get_ticks()))

    pygame.quit()


if __name__ == '__main__':
    main()
