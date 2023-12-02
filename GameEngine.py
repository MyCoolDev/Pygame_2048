import pygame
import config


class GameEngine:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((config.config["ScreenResolution"]))
        self.events = None

        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0

    def start(self):
        while self.running:
            self.events = pygame.event.get()
            self.handle_events()

            self.reset()

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
        pass

    def render(self):
        pass