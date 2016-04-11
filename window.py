import os

import pygame
from pygame.locals import *

import dimensions
from character import Noam, Rosa
from zone import Conveyor, LoadingBay, DropZone
from chocolate import Bar

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
        self.zones = list(self.setup_zones())
        self.zones[-1].add_choc(Bar())

        self.init()

    def setup_zones(self):
        loading_bay = LoadingBay()
        yield loading_bay
        previous = loading_bay
        for x in range(3):
            drop_zone1 = DropZone(self.character1, 2 - x, 250, 55 + x * 140, previous)
            yield drop_zone1
            conveyor1 = Conveyor(660, 55 + x * 140, -1, drop_zone1)
            yield conveyor1
            drop_zone2 = DropZone(self.character2, 2 - x, 700, 125 + x * 140, conveyor1)
            yield drop_zone2
            conveyor2 = Conveyor(290, 125 + x * 140, 1, drop_zone2)
            previous = conveyor2
            yield conveyor2

    def init(self):
        # Draw
        self.draw()

    # THE WHILE LOOP
    def main(self):
        self.clock.tick(FPS)
        self.update()

        self.listen_for_input()

        self.draw()

    def update(self):
        for zone in self.zones:
            zone.update()

    # Drawing
    def draw(self):
        self.window.blit(self.background, (0,0))
        self.draw_conveyor()
        self.character1.draw()
        self.character2.draw()
        for zone in self.zones:
            zone.draw(self.window)

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
