import os
import sys

import pygame
from pygame.locals import *

from dimensions import *
from character import Noam, Rosa
from zone import Conveyor, LoadingBay, DropZone, StartMachine
from chocolate import Bar

ASSETS_DIR = 'images'
BLACK = (  0,   0,   0)
FPS = 59.37

class Window(object):

    def __init__(self):
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.splash = pygame.image.load(os.path.join(ASSETS_DIR, "splash.png"))
        self.background = pygame.image.load(os.path.join(ASSETS_DIR, "background.png"))
        self.character1 = Noam(self.window)
        self.character2 = Rosa(self.window)
        self.zones = list(self.setup_zones())

        self.window.blit(self.splash, (0,0))
        pygame.display.update()
        exit_splash = False
        while not exit_splash:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        exit_splash = True

        self.draw()

    def setup_zones(self):
        loading_bay = LoadingBay()
        yield loading_bay
        previous = loading_bay
        for x in range(3):
            height = CONVEYOR_Y_SPRITE_START + 2 * x * CONVEYOR_Y_SPACING
            drop_zone1 = DropZone(self.character1, 2 - x, CONVEYOR_DROP_LEFT, height, previous)
            yield drop_zone1
            conveyor1 = Conveyor(CONVEYOR_SPRITE_END, height, -1, drop_zone1)
            yield conveyor1
            height = CONVEYOR_Y_SPRITE_START + (2 * x + 1) * CONVEYOR_Y_SPACING
            if x < 2:
                drop_zone2 = DropZone(self.character2, 2 - x, CONVEYOR_DROP_RIGHT, height, conveyor1)
                yield drop_zone2
                conveyor2 = Conveyor(CONVEYOR_SPACE_START, height, 1, drop_zone2, 1 - x)
                previous = conveyor2
                yield conveyor2
            else:
                drop_zone2 = DropZone(self.character2, 2 - x, START_CONVEYOR_DROP_X, height, conveyor1)
                yield drop_zone2
                yield StartMachine(drop_zone2)

    # THE WHILE LOOP
    def main(self):
        self.clock.tick(FPS)
        self.update()

        self.listen_for_quit()
        self.listen_for_input()

        self.draw()

    def listen_for_quit(self):
        def quit():
            pygame.quit()
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Mouse
                quit()
            elif event.type == pygame.KEYUP:  # Keyboard
                if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
                    quit()
            # Return the event if not quitting
            else:
                pygame.event.post(event)

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
                x = CONVEYOR_START + j * CONVEYOR_SEGMENT_LENGTH
                y = CONVEYOR_Y_START + i * CONVEYOR_Y_SPACING
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
