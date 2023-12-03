import pygame
import random
from Components.MonoBehaviour import MonoBehaviour


class Grid(MonoBehaviour):
    def __init__(self, size, position, base_color, node_color, grid_size, gap):
        super().__init__(size, position, base_color)
        self.node_color = node_color
        self.grid_size = grid_size
        self.gap = gap
        self.grid = []

        self.init_grid()

    def init_grid(self):
        for i in range(self.grid_size):
            current = []

            for _ in range(self.grid_size):
                current.append([])

            self.grid.append(current)

        print(self.grid)

    def create_random_box(self):
        pass

    def update(self, dt: float, events: list):
        pass

    def render(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position, self.size))
