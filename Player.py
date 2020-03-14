import pygame

from constants import *


class Player:

    def __init__(self, screen, x, y, w, h, color=RED):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.player = pygame.image.load(FOLDER_IMG + "player_128px.png")

    def draw(self):
        # rectangle1 = pygame.Rect(self.x, self.y, self.w, self.h)
        # pygame.draw.rect(self.screen, self.color, rectangle1)
        # pygame.draw.rect(self.screen, BLUE, self.rectangle1)
        h = self.player.get_height()
        # self.screen.blit(self.player, (336, 500 - h))
        self.screen.blit(self.player, (self.x, self.y))

    def update(self):
        # print("Update Player")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    print("Move RIGHT")
                    self.x = self.x + SPEED

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x
