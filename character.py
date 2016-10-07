import os

import pygame

import dimensions

ASSETS_DIR = 'images'


class Character(object):
    def __init__(self, window):
        self.window = window
        image_path = os.path.join(ASSETS_DIR, self.image_location)
        self.image = pygame.image.load(image_path)

    def draw(self):
        self.window.blit(self.image, self.locations[self.position])

    def down(self):
        if self.position > 0:
            self.position = self.position - 1

    def up(self):
        if self.position < 2:
            self.position = self.position + 1


class Noam(Character):
    locations = dimensions.CHARACTER_A
    position = 0
    image_location = "characters/noam.png"


class Rosa(Character):
    locations = dimensions.CHARACTER_B
    position = 0
    image_location = "characters/rosa.png"
