import logging

import pygame
from PlanetaryEngine import PELogging
from PlanetaryEngine import Graphics
from PlanetaryEngine import Maths
import os

if __name__ == "__main__":
    PELogging.error("You cannot run the engine, it will not work")
    os.remove("log.txt")


class Engine:

    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.Graphics = Graphics.Graphics(self, self.screen)
        self.framerate = 0

    def clear_screen(self, color):
        try:
            self.screen.fill(color)
        except ValueError:
            PELogging.error("Color: '" + color + "' is not a valid color")
            self.running = False

    def step_physics(self, framerate):
        self.framerate = framerate
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        self.clock.tick(framerate)

    def get_framerate(self):
        return self.clock.get_fps()

    def delta(self):
        try:
            deltatime = 1/self.get_framerate()
            return deltatime
        except ZeroDivisionError:
            logging.log(1, "Must wait one more frame to get the deltatime")
            return 1/24

    def set_title(self, text):
        pygame.display.set_caption(text)
