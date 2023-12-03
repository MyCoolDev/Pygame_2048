import pygame

import Colors
import config
from Grid import Grid


class GameEngine:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((config.config["ScreenResolution"]))
        self.events = None

        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.grid = None
        self.init_vars()

    def init_vars(self):
        self.grid = Grid(pygame.Vector2(600), pygame.Vector2((self.screen.get_width() - 600) / 2, (self.screen.get_height() - 600) / 2), (255, 255, 255), (50, 50, 50), 4, 5)

    def start(self):
        while self.running:
            self.reset()

            self.events = pygame.event.get()
            self.handle_events()

            self.update()
            self.render()

            pygame.display.flip()

            # limit the fps to 60
            self.dt = self.clock.tick(60) / 1000

    def handle_events(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()

    def reset(self):
        self.screen.fill("black")

    def update(self):
        self.grid.update(self.dt, self.events)

    def render(self):
        self.grid.render(self.screen)
