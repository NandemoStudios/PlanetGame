import PlanetaryEngine
from PlanetaryEngine import Maths
from PlanetaryEngine import PELogging
import Planets
import pygame

global PlanetsRendered
PlanetsRendered = 0

Camera = pygame.Vector2(0, 0)
CameraZoom = 1

Game = PlanetaryEngine.Engine(900, 900)
Game.set_title("Planet Game")


def RenderMoon(self, orbit_speed, screensize):
    global PlanetsRendered
    getpos = Maths.get_point_on_circle(self.parent.x, self.parent.y,
                                       self.parent.radius * CameraZoom + self.orbit_distance * CameraZoom, self.loop)
    if not self.parent.visible:
        pass
    elif getpos.x > screensize.x or getpos.x < 0:
        self.visible = False
    elif getpos.y > screensize.y or getpos.y < 0:
        self.visible = False
    else:
        if self.radius * CameraZoom < 1:
            self.visible = False
        else:
            self.visible = True
            x = getpos.x
            y = getpos.y
            Game.Graphics.Circle(self.color, x, y, self.radius * CameraZoom, 1)
            PlanetsRendered += 1
    self.loop += (1 * Game.delta()) * orbit_speed


def RenderPlanet(self, orbit_speed, screensize):
    global PlanetsRendered
    orbit_pos = PlanetaryEngine.Maths.get_point_on_circle(self.parent.x + Camera.x, self.parent.y + Camera.y,
                                                          self.parent.radius * CameraZoom + (self.orbit_distance + self.parent.radius) * CameraZoom,
                                                          self.loop)
    if orbit_pos.x > screensize.x or orbit_pos.x < 0:
        self.visible = False
    elif orbit_pos.y > screensize.y or orbit_pos.y < 0:
        self.visible = False
    else:
        if self.radius * CameraZoom < 1:
            self.visible = False
        else:
            self.visible = True
            Game.Graphics.Circle(self.color, orbit_pos.x, orbit_pos.y, self.radius * CameraZoom, 1)
            self.x = orbit_pos.x
            self.y = orbit_pos.y
            PlanetsRendered += 1
    self.loop += (1 * Game.delta()) * orbit_speed


def RenderSun(self, screensize):
    global PlanetsRendered
    if self.x < 0 or self.x > screensize.y:
        self.visible = False
    elif self.y < 0 or self.y > screensize.x:
        self.visible = False
    else:
        if not self.radius * CameraZoom < 1:
            self.visible = True
            Game.Graphics.Circle(self.color, self.x + Camera.x, self.y + Camera.y, self.radius * CameraZoom, 5)
            PlanetsRendered += 1
        else:
            self.visible = False


def DrawText(text, x, y, fontSize, color, Localtype):
    try:
        if Localtype == "local":
            Game.Graphics.Text(text, x, y, fontSize, color)
        elif Localtype == "global":
            Game.Graphics.Text(text, x + Camera.x, y + Camera.y, fontSize, color)
    except ValueError:
        PELogging.error("That is not the right value type")


theSun = Planets.Sun('yellow', 450, 450, 696)
Earth = Planets.Planet('green', 63, theSun, 1496)
earthMoon = Planets.Moon('gray', 10, Earth, 384)
mars = Planets.Planet('red', 33, theSun, 2279)
marsMoon = Planets.Moon('white', 3, mars, 10)
marsMoon2 = Planets.Moon('gray', 2, mars, 25)

loop = 0

while Game.running:
    screen_size = Game.get_window_size()
    keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #   Camera.x = Earth.x
    #    Camera.y = Earth.y
    if keys[pygame.K_LSHIFT]:
        speed_m = 400
    else:
        speed_m = 100
    if keys[pygame.K_a]:
        Camera.x += speed_m * Game.delta()
    if keys[pygame.K_d]:
        Camera.x -= speed_m * Game.delta()
    if keys[pygame.K_w]:
        Camera.y += speed_m * Game.delta()
    if keys[pygame.K_s]:
        Camera.y -= speed_m * Game.delta()
    if keys[pygame.K_e]:
        CameraZoom += 1 * Game.delta()
    if keys[pygame.K_q]:
        CameraZoom -= 1 * Game.delta()

    # Runs the render planets command, displays the planets on screen
    RenderSun(theSun, screen_size)
    RenderPlanet(Earth, 1, screen_size)
    RenderMoon(earthMoon, 12, screen_size)
    RenderPlanet(mars, 0.5319148936, screen_size)
    RenderMoon(marsMoon, 0.75, screen_size)
    RenderMoon(marsMoon2, 0.5, screen_size)

    Game.set_title(
        "Planet Engine | FPS: " + str(round(Game.get_framerate())) + " | Planets Rendered: " + str(PlanetsRendered))

    DrawText(str(Camera), 20, 20, 24, 'White', 'local')
    DrawText(str(round(CameraZoom, 2))+'x', 20, 40, 24, 'White', 'local')

    # Standard refresh function
    Game.step_physics(pygame.display.get_current_refresh_rate())
    Game.clear_screen("black")
    PlanetsRendered = 0
