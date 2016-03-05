import os

import pygame
from pygame.locals import *

import dimensions
from character import Noam, Rosa

ASSETS_DIR = 'images'
BLACK = (  0,   0,   0)
FPS = 59.37

class Window(object):

    def __init__(self):
        self.window = pygame.display.set_mode(dimensions.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(os.path.join(ASSETS_DIR, "background.png"))
        self.character1 = Noam(self.window)
        self.character2 = Rosa(self.window)

        self.init()

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
        self.draw_conveyor()
        self.character1.draw()
        self.character2.draw()

    def draw_conveyor(self):
        image = pygame.image.load(os.path.join(ASSETS_DIR, "conveyor.png"))
        for i in range(5):
            for j in range(4):
                x = 300 + j * 100
                y = 105 + i * 70
                self.window.blit(image, (x, y))

    def listen_for_input(self):
        # Discrete key presses
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_z):
                    self.character1.down()
                elif (event.key == pygame.K_a):
                    self.character1.up()
                elif (event.key == pygame.K_DOWN):
                    self.character2.down()
                elif (event.key == pygame.K_UP):
                    self.character2.up()
                break
