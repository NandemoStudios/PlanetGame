import PlanetaryEngine
from PlanetaryEngine import Maths
import random
import math
import Planets
import pygame

global PlanetsRendered
PlanetsRendered = 0

Game = PlanetaryEngine.Engine(900, 900)
Game.set_title("Planet Game")


def RenderMoon(self, orbit_speed):
    global PlanetsRendered
    getpos = Maths.get_point_on_circle(self.parent.x,
                                       self.parent.y,
                                       self.parent.radius + self.orbit_distance,
                                       self.loop)
    x = getpos.x
    y = getpos.y
    Game.Graphics.Circle(self.color, x, y, self.radius, 1)
    self.loop += (1 * Game.delta()) * orbit_speed
    PlanetsRendered += 1


def RenderPlanet(self, orbit_speed):
    global PlanetsRendered
    orbit_pos = PlanetaryEngine.Maths.get_point_on_circle(self.sun.x, self.sun.y, self.sun.radius + self.orbit_distance,
                                                          self.loop)
    Game.Graphics.Circle(self.color, orbit_pos.x, orbit_pos.y, self.radius, 1)
    self.x = orbit_pos.x
    self.y = orbit_pos.y
    self.loop += (1 * Game.delta()) * orbit_speed
    PlanetsRendered += 1


def RenderSun(self):
    global PlanetsRendered
    Game.Graphics.Circle(self.color, self.x, self.y, self.radius, 5)
    PlanetsRendered += 1


theSun = Planets.Sun('yellow', 450, 450, 50)
Earth = Planets.Planet('green', 20, theSun, 200)
earthMoon = Planets.Moon('gray', 5, Earth, 20)
mars = Planets.Planet('red', 15, theSun, 100)
marsMoon = Planets.Moon('white', 3, mars, 10)

loop = 0

while Game.running:
    # Runs the render planets command, displays the planets on screen
    RenderSun(theSun)
    RenderPlanet(Earth, 1)
    RenderMoon(earthMoon, 12)
    RenderPlanet(mars, 0.5)
    RenderMoon(marsMoon, 0.75)

    Game.set_title(
        "Planet Engine | FPS: " + str(round(Game.get_framerate())) + " | Planets Rendered: " + str(PlanetsRendered))

    # Standard refresh function
    Game.step_physics(pygame.display.get_current_refresh_rate())
    Game.clear_screen("black")
    PlanetsRendered = 0
