import PlanetaryEngine

Game = PlanetaryEngine.Engine(900, 600)

while Game.running:
    Game.clear_screen("blac")
    Game.step_physics(60)