import PlanetaryEngine

Game = PlanetaryEngine.Engine(900, 600)

Planets = []


class Planet:

    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

        Planets.append(self)


def RenderPlanets():
    for x in range(0, len(Planets)):
        planet = Planets[x]
        Game.Graphics.Circle(planet.color, planet.x, planet.y, planet.radius, 1)


Moon = Planet('Gray', 100, 300, 5)
Earth = Planet('blue', 30, 300, 20)
Sun = Planet('yellow', 450, 300, 100)

while Game.running:
    RenderPlanets()

    Game.Graphics.Square("red", 10, 10, 20, 20)

    Game.step_physics(60)
    Game.clear_screen("black")
