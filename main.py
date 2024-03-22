import PlanetaryEngine
from PlanetaryEngine import Maths
import random
import math
import Planets
import pygame

global PlanetsRendered
PlanetsRendered = 0

Camera = pygame.Vector2(0, 0)
CameraZoom = 1

Game = PlanetaryEngine.Engine(900, 900)
Game.set_title("Planet Game")


def RenderMoon(self, orbit_speed):
    global PlanetsRendered
    getpos = Maths.get_point_on_circle(self.parent.x, self.parent.y, self.parent.radius*CameraZoom + self.orbit_distance*CameraZoom, self.loop)
    if not self.parent.visible:
        pass
    elif getpos.x > 900 or getpos.x < 0:
        self.visible = False
    elif getpos.y > 900 or getpos.y < 0:
        self.visible = False
    else:
        if self.radius*CameraZoom < 1:
            self.visible = False
        else:
            self.visible = True
            x = getpos.x
            y = getpos.y
            Game.Graphics.Circle(self.color, x, y, self.radius*CameraZoom, 1)
            PlanetsRendered += 1
    self.loop += (1 * Game.delta()) * orbit_speed


def RenderPlanet(self, orbit_speed):
    global PlanetsRendered
    orbit_pos = PlanetaryEngine.Maths.get_point_on_circle(self.sun.x+Camera.x, self.sun.y+Camera.y, self.sun.radius*CameraZoom + self.orbit_distance*CameraZoom,
                                                          self.loop)
    if orbit_pos.x > 900 or orbit_pos.x < 0:
        self.visible = False
    elif orbit_pos.y > 900 or orbit_pos.y <0:
        self.visible = False
    else:
        if self.radius * CameraZoom < 1:
            self.visible = False
        else:
            self.visible = True
            Game.Graphics.Circle(self.color, orbit_pos.x, orbit_pos.y, self.radius*CameraZoom, 1)
            self.x = orbit_pos.x
            self.y = orbit_pos.y
            PlanetsRendered += 1
    self.loop += (1 * Game.delta()) * orbit_speed


def RenderSun(self):
    global PlanetsRendered
    if self.x < 0 or self.x > 900:
        self.visible = False
    elif self.y < 0 or self.y > 900:
        self.visible = False
    else:
        if not self.radius*CameraZoom < 1:
            self.visible = True
            Game.Graphics.Circle(self.color, self.x+Camera.x, self.y+Camera.y, self.radius*CameraZoom, 5)
            PlanetsRendered += 1
        else:
            self.visible = False


theSun = Planets.Sun('yellow', 450, 450, 50)
Earth = Planets.Planet('green', 20, theSun, 200)
earthMoon = Planets.Moon('gray', 5, Earth, 20)
mars = Planets.Planet('red', 15, theSun, 100)
marsMoon = Planets.Moon('white', 3, mars, 10)

loop = 0

while Game.running:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        Camera.x += 100 * Game.delta()
    if keys[pygame.K_d]:
        Camera.x -= 100 * Game.delta()
    if keys[pygame.K_w]:
        Camera.y += 100 * Game.delta()
    if keys[pygame.K_s]:
        Camera.y -= 100 * Game.delta()
    if keys[pygame.K_e]:
        CameraZoom += 1 * Game.delta()
    if keys[pygame.K_q]:
        CameraZoom -= 1 * Game.delta()

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
