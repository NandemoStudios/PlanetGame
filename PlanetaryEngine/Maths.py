import math
import pygame

def get_point_on_circle(cx, cy, radius, a):
    x = cx + radius * math.cos(a)
    y = cy + radius * math.sin(a)
    result = [x, y]
    return pygame.Vector2(x,y)