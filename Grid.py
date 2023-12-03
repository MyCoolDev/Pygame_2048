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

    def handle_input(self, action: tuple):
        # i - current row
        # k - current object in row
        # z - current row to checking with the k

        if action == (0, 1):
            for i in range(self.grid_size, -1, -1):
                for k in range(self.grid_size):
                    for z in range(self.grid_size):
                        if self.grid[z][k] is None:
                            self.grid[z][k] = self.grid[i][k]
                            del self.grid[z][k]
                            break
        if action == (0, -1):
            pass



    def update(self, dt: float, events: list):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pass

    def render(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position, self.size))
