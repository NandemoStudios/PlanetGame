import pygame
from PlanetaryEngine import PELogging


class Engine:

    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True

    def clear_screen(self, color):
        try:
            self.screen.fill(color)
        except ValueError:
            PELogging.error("Color: '" + color + "' is not a valid color")
            self.running = False

    def step_physics(self, framerate):
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        self.clock.tick(framerate)