#!/usr/bin/env python

import pygame
from window import Window

if __name__ == "__main__":
    # Initialise the game engine
    pygame.init()
    # Create the window/game/b
    window = Window()

    while True:
        window.main()
        pygame.display.update()
