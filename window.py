import os

import pygame
from pygame.locals import *

import dimensions

ASSETS_DIR = 'images'
BLACK = (  0,   0,   0)
FPS = 59.37

class Window(object):
    locations = dimensions.CHARACTER_A
    x = 0

    def __init__(self):
        self.window = pygame.display.set_mode(dimensions.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(os.path.join(ASSETS_DIR, "background.png"))

        self.init()
        self.x = 0

    def init(self):
        # Draw
        self.draw()

    # THE WHILE LOOP
    def main(self):
        self.clock.tick(FPS)

        self.listen_for_input()

        self.draw()

    # Drawing
    def draw(self):
        self.window.blit(self.background, (0,0))
        self.draw_character()

    def draw_character(self):
        image = pygame.image.load(os.path.join(ASSETS_DIR, "noam.png"))
        self.window.blit(image, self.locations[self.x])

    def listen_for_input(self):
        # Discrete key presses
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_DOWN):
                    if self.x > 0:
                        self.x = self.x - 1
                elif (event.key == pygame.K_UP):
                    if self.x < 2:
                        self.x = self.x + 1
                break
