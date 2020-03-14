import pygame

from constants import *
from Player import *


class Game:

    def __init__(self, width, height, caption):
        self.width = width
        self.height = height
        self.caption = caption
        self.screen = 0
        self.player1 = 0
        self.bg = 0
        pygame.init()

    def run(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)
        icon = pygame.image.load(FOLDER_IMG + "comet_32x32px.png")
        pygame.display.set_icon(icon)
        # Init player 1
        self.player1 = Player(self.screen,
                              player_pos_x, player_pos_y,
                              player_w, player_h,
                              BLUE)
        # Load bg
        self.bg = pygame.image.load(FOLDER_IMG +"bg.jpg")
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))

    def draw(self):
        # self.screen.fill((255, 255, 255))
        self.screen.blit(self.bg, (0, 0))
        self.player1.draw()
        pygame.display.update()

    def update(self):
        # self.player1.set_x(self.player1.get_x() + 1)
        self.player1.update()

    # Accesseurs / Accessors
    # Getters
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_screen(self):
        return self.screen

    # Setters
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
