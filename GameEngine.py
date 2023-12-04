import pygame

import Colors
import config
from Grid import Grid
from Components.UI.Txt import Text
import random


class GameEngine:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((config.config["ScreenResolution"]))
        self.events = None

        self.state = "intro"

        # intro
        self.intro_timer = 0

        # intro production text fade
        self.intro_production_fade_in_duration = 2
        self.intro_production_duration = 1
        self.intro_production_fade_out_duration = 2
        self.intro_production_fade_sum_duration = self.intro_production_fade_in_duration + self.intro_production_duration + self.intro_production_fade_out_duration
        self.intro_fade_timer = 0
        self.intro_production_content = "Shalev & Ron Productions"
        self.intro_production_text = Text(self.intro_production_content, "Poppins", 70, pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2), (255, 255, 255))

        # 2048 logo number intro
        self.logo_duration = 3
        self.logo_parts_duration_each = (self.logo_duration - 1) / 4
        self.logo_content = 0000
        self.logo_starting_font_size = 120
        self.logo_start_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.logo_text = Text("0000", "Poppins", self.logo_starting_font_size, self.logo_start_pos, (255, 255, 255), alpha=0)
        self.logo_shrink_duration = 1.5
        self.logo_final_font_size = 80
        self.logo_delta_font_size = self.logo_starting_font_size - self.logo_final_font_size
        self.logo_end_pos = pygame.Vector2(self.screen.get_width() / 2, 1 * self.screen.get_height() / 5)
        self.logo_delta_pos = self.logo_start_pos - self.logo_end_pos

        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.grid = None
        self.init_vars()

        self.txt = "Score: 0"
        self.text = Text(self.txt, "Arial", 30, pygame.Vector2(100), (255, 255, 255))

    def init_vars(self):
        self.grid = Grid(pygame.Vector2(600), pygame.Vector2((self.screen.get_width() - 600) / 2, (self.screen.get_height() - 600) / 2), (255, 255, 255), (50, 50, 50), 4, 5)

    def start(self):
        while self.running:
            # limit the fps to 60
            self.dt = self.clock.tick(60) / 1000

            self.reset()
            self.events = pygame.event.get()
            self.handle_events()

            self.update()
            self.render()
            pygame.display.flip()

    def handle_events(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def reset(self):
        self.screen.fill("black")

    def update(self):
        if self.state == "intro":
            self.intro_timer += self.dt
            if self.intro_fade_timer < self.intro_production_fade_sum_duration:
                self.intro_fade_timer += self.dt

            if self.intro_timer < self.intro_production_fade_in_duration:
                alpha = int((255 / 3) * self.intro_fade_timer)
                self.intro_production_text.alpha = alpha
                self.intro_production_text.update_alpha()
            elif 0 < self.intro_timer - self.intro_production_fade_in_duration < self.intro_production_duration:
                self.intro_fade_timer = 0
            elif 0 < self.intro_timer - self.intro_production_fade_in_duration - self.intro_production_duration < self.intro_production_fade_out_duration:
                self.intro_fade_timer += self.dt
                alpha = int((255 / 3) * (3 - self.intro_fade_timer))
                self.intro_production_text.alpha = alpha
                self.intro_production_text.update_alpha()

            # logo 2048
            elif 0 < self.intro_timer - self.intro_production_fade_sum_duration < self.logo_duration:
                self.logo_text.alpha = 255
                self.logo_text.update_alpha()

                self.logo_content = [f"{random.randint(0, 9)}", f"{random.randint(0, 9)}", f"{random.randint(0, 9)}",
                                     f"{random.randint(0, 9)}"]
                if self.logo_parts_duration_each <= self.intro_timer - self.intro_production_fade_sum_duration:
                    self.logo_content[0] = "2"
                    if 2 * self.logo_parts_duration_each <= self.intro_timer - self.intro_production_fade_sum_duration:
                        self.logo_content[1] = "0"
                    if 3 * self.logo_parts_duration_each <= self.intro_timer - self.intro_production_fade_sum_duration:
                        self.logo_content[2] = "4"
                    if 4 * self.logo_parts_duration_each <= self.intro_timer - self.intro_production_fade_sum_duration:
                        self.logo_content[3] = "8"

                self.logo_text.update_text("".join(self.logo_content))

            elif 0 < self.intro_timer - self.intro_production_fade_sum_duration - self.logo_duration < self.logo_shrink_duration:
                ds = (self.intro_timer - self.intro_production_fade_sum_duration - self.logo_duration) / self.logo_shrink_duration * self.logo_delta_font_size
                dp = (self.intro_timer - self.intro_production_fade_sum_duration - self.logo_duration) / self.logo_shrink_duration * self.logo_delta_pos
                self.logo_text.update_font_size(round(self.logo_starting_font_size - ds))
                self.logo_text.update_position(self.logo_start_pos - dp)

            elif 0 < self.intro_timer - self.intro_production_fade_sum_duration - self.logo_duration - self.logo_shrink_duration:
                self.logo_text.update_font_size(self.logo_final_font_size)
        elif self.state == "game":
            self.grid.update(self.dt, self.events)
            score = self.grid.get_score()
            self.txt = "score: " + str(score)
            self.text.update_text(self.txt)

    def render(self):
        if self.state == "intro":
            self.intro_production_text.render(self.screen)
            self.logo_text.render(self.screen)
        elif self.state == "game":
            self.grid.render(self.screen)
            self.text.render(self.screen)
