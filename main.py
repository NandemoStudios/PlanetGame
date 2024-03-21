import PlanetaryEngine

Game = PlanetaryEngine.Engine(900, 600)


class Planet:

    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def drawPlanet(self):
        Game.Graphics.Circle(Game.Graphics, Game.screen, self.color, self.x, self.y, self.radius, 1)


Earth = Planet('blue', 10, 300, 20)
Sun = Planet('yellow', 450, 300, 100)

while Game.running:

    Earth.drawPlanet()
    Sun.drawPlanet()

    Game.step_physics(60)
    Game.clear_screen("black")
