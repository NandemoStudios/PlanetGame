import PlanetaryEngine


class Planet:

    def __init__(self, color, radius, sun, orbit_distance):
        self.color = color
        self.radius = radius
        self.sun = sun
        self.orbit_distance = orbit_distance
        self.loop = 0
        self.x = 0
        self.y = 0


class Sun:

    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

class Moon:

    def __init__(self, color, radius, parent, orbit_distance):
        self.color = color
        self.radius = radius
        self.parent = parent
        self.orbit_distance = orbit_distance
        self.loop = 0