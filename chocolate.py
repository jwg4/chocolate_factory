import os

import pygame

ASSETS_DIR = 'images'


class Chocolate(object):
    _x = 0
    _y = 0

    def set_state(self, state):
        if state == 'BREAKING':
            self.state = 3
        else:
            self.state = state

    def draw(self, window):
        current_state = self.states[self.state]

        window.blit(current_state, (self._x, self._y))

    def set_position(self, x, y):
        self._x = x
        self._y = y

    def get_position(self):
        return (self._x, self._y)

    def break_(self):
        if self.state != 'BREAKING':
            self.crash.play()
        self.set_state('BREAKING')


class Bar(Chocolate):
    def __init__(self):
        self.state = 0
        self.states = [
            pygame.image.load(os.path.join(ASSETS_DIR, "chocolate/bar_0.png")),
            pygame.image.load(os.path.join(ASSETS_DIR, "chocolate/bar_1.png")),
            pygame.image.load(os.path.join(ASSETS_DIR, "chocolate/bar_2.png")),
            pygame.image.load(os.path.join(ASSETS_DIR, "chocolate/bar_9.png")),
        ]
        self.crash = pygame.mixer.Sound('sounds/crash.wav')


class Egg(Chocolate):
    def __init__(self):
        self.state = 0
        self.states = [
            pygame.image.load(os.path.join(ASSETS_DIR, "chocolate/egg_0.png")),
            pygame.image.load(os.path.join(ASSETS_DIR, "chocolate/egg_1.png")),
            pygame.image.load(os.path.join(ASSETS_DIR, "chocolate/egg_2.png")),
            pygame.image.load(os.path.join(ASSETS_DIR, "chocolate/bar_9.png")),
        ]
        self.crash = pygame.mixer.Sound('sounds/crash.wav')
