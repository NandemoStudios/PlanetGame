import pygame
import PlanetaryEngine as PE

class Graphics:

    def __init__(self):
        pass

    def Circle(self, screen, color, xpos, ypos, radius, lineWidth):
        try:
            center = pygame.Vector2(xpos, ypos)
            pygame.draw.circle(screen, color, center, radius, lineWidth)
        except ValueError:
            PE.PELogging.error("one of the values in circle is not valid")