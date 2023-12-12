import pygame

import Colors
import config
from Grid import Grid
from Components.UI.Txt import Text
from Components.UI.Button import Button
import random


class GameEngine:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((config.config["ScreenResolution"]))
        pygame.display.set_caption("2048")
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

        # menu
        self.start_button = Button(pygame.Vector2(250, 70), pygame.Vector2(self.screen.get_width() / 2, 4 * self.screen.get_height() / 5), (68, 148, 206), "Start", "Poppins", 60, (255, 255, 255), border_radius=10)
        self.mid_display = Button(pygame.Vector2(200, 200), pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2), self.generate_random_color(), "2", "Poppins", 60, (255, 255, 255), border_radius=10)
        self.quit_button = Button(pygame.Vector2(250, 70), pygame.Vector2(self.screen.get_width() / 2, 4 * self.screen.get_height() / 5 + 80), (206, 68, 68), "Quit", "Poppins", 60, (255, 255, 255), border_radius=10)

        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.grid = None
        self.init_vars()

        self.txt = "Score: 0"
        self.text = Text(self.txt, "Poppins", 30, pygame.Vector2(100), (255, 255, 255))

        self.txt2 = "Game Over"
        self.text2 = Text(self.txt2, "Poppins", 77, pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 5), (255, 255, 255))

        self.txt3 = "Best: 0"
        self.text3 = Text(self.txt3, "Poppins", 30, pygame.Vector2(200, 100), (255, 255, 255))

        # game over buttons
        self.restart_button = Button(pygame.Vector2(280, 70), pygame.Vector2(self.screen.get_width() / 2, 3 * self.screen.get_height() / 5), (68, 148, 206), "Restart", "Poppins", 50, (255, 255, 255), border_radius=10)
        self.back_to_menu_button = Button(pygame.Vector2(280, 70), pygame.Vector2(self.screen.get_width() / 2, 3 * self.screen.get_height() / 5 + 80), (153, 128, 106), "Back To Menu", "Poppins", 50, (255, 255, 255), border_radius=10)
        self.quit = Button(pygame.Vector2(280, 70), pygame.Vector2(self.screen.get_width() / 2, 3 * self.screen.get_height() / 5 + 160), (206, 68, 68), "Quit", "Poppins", 50, (255, 255, 255), border_radius=10)

    def init_vars(self):
        self.grid = Grid(pygame.Vector2(600), pygame.Vector2((self.screen.get_width() - 600) / 2, (self.screen.get_height() - 600) / 2), (255, 255, 255), (50, 50, 50), 4, 5)

    @staticmethod
    def generate_random_color() -> tuple:
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

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

                self.logo_content = [f"{random.randint(0, 9)}", f"{random.randint(0, 9)}", f"{random.randint(0, 9)}", f"{random.randint(0, 9)}"]
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
                self.state = "menu"

        elif self.state == "menu":
            if self.start_button.update(self.dt, self.events):
                self.state = "game"
            if self.quit_button.update(self.dt, self.events):
                pygame.quit()
                quit()
            if self.mid_display.update(self.dt, self.events):
                self.mid_display.color = self.generate_random_color()
                if int(self.mid_display.text.txt) < 1000000:
                    self.mid_display.text.update_text(str(int(self.mid_display.text.txt) * 2))

        elif self.state == "game":
            if self.grid.game_over():
                print("Game Over")
                self.state = "game_over"
            else:
                self.grid.update(self.dt, self.events)
                score = self.grid.get_score()
                self.txt = "Score: " + str(score)
                self.text.update_text(self.txt)

        elif self.state == "game_over":
            over = self.grid.get_game_over_msg()
            self.txt = str(over)
            self.text.update_text(self.txt)
            if self.quit.update(self.dt, self.events):
                pygame.quit()
                quit()
            if self.back_to_menu_button.update(self.dt, self.events):
                self.state = "menu"
                self.init_vars()
            if self.restart_button.update(self.dt, self.events):
                self.state = "game"
                self.init_vars()

    def render(self):
        if self.state == "intro":
            self.intro_production_text.render(self.screen)
            self.logo_text.render(self.screen)

        elif self.state == "menu":
            self.logo_text.render(self.screen)
            self.start_button.render(self.screen)
            self.quit_button.render(self.screen)
            self.mid_display.render(self.screen)

        elif self.state == "game":
            self.grid.render(self.screen)
            self.text.render(self.screen)
            self.text3.render(self.screen)

        elif self.state == "game_over":
            self.text2.render(self.screen)
            self.restart_button.render(self.screen)
            self.back_to_menu_button.render(self.screen)
            self.quit.render(self.screen)
