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
        self.player_move_right = False
        self.player_move_left = False

    def draw(self):
        # rectangle1 = pygame.Rect(self.x, self.y, self.w, self.h)
        # pygame.draw.rect(self.screen, self.color, rectangle1)
        # pygame.draw.rect(self.screen, BLUE, self.rectangle1)
        h = self.player.get_height()
        # self.screen.blit(self.player, (336, 500 - h))
        self.screen.blit(self.player, (self.x, self.y))

    def update(self):
        # print("Update Player")
        # Events
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key == pygame.K_d:
                self.player_move_right = True
            if event.key == pygame.K_a:
                self.player_move_left = True
        for event in pygame.event.get(pygame.KEYUP):
            if event.key == pygame.K_d:
                self.player_move_right = False
            if event.key == pygame.K_a:
                self.player_move_left = False

        # Update
        if self.player_move_right:
            self.x = self.x + SPEED
        if self.player_move_left:
            self.x = self.x + -SPEED

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def set_player_move_right(self, value):
        self.player_move_right = value
