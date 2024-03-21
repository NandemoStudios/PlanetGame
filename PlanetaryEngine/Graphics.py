import pygame
import PlanetaryEngine as PE
from PlanetaryEngine import PELogging

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

    def Square(self, color, x1, y1, x2, y2):
        try:
            rect = pygame.Rect(x1, y1, x2, y2)
            pygame.draw.rect(self.screen, color, rect)
        except ValueError:
            PELogging.error("A value you entered is invalid")
