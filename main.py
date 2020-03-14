import pygame

from Game import *
from constants import *

screen = 0
game = 0


def update():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("Hello Allan & Peter")

    game.update()


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
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        update()
        draw()

    pygame.quit()


if __name__ == '__main__':
    main()
