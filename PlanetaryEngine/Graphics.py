import pygame
import PlanetaryEngine as PE

class Graphics:

    def __init__(self, parent, screen):
        self.screen = screen
        self.parent = parent

    def Circle(self, color, xpos, ypos, radius, lineWidth):
        try:
            center = pygame.Vector2(xpos, ypos)
            pygame.draw.circle(self.screen, color, center, radius, lineWidth)
        except ValueError:
            PE.PELogging.error("one of the values in circle is not valid")
