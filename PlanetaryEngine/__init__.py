import pygame
from PlanetaryEngine import PELogging
from PlanetaryEngine import Graphics

if __name__ == "__main__":
    PELogging.log(2, "You cannot run the engine, it will not work")

class Engine:

    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.Graphics = Graphics.Graphics

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
