import pygame
import random
from Box import Box
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
                current.append(-1)

            self.grid.append(current)

    def create_random_box(self):
        # create a random (position) box with random choice(2, 4)
        positions = []
        for i in range(self.grid_size):
            for k in range(self.grid_size):
                if self.grid[i][k] == -1:
                    positions.append((k, i))
        pos = random.choice(positions)

    def handle_input(self, action: tuple):
        # i - current row
        # k - current object in row
        # z - current row to checking with the k

        # Up
        if action == (0, 1):
            for i in range(self.grid_size - 1, -1, -1):
                for k in range(self.grid_size):
                    if self.grid[i][k] == -1:
                        continue
                    for z in range(self.grid_size):
                        if self.grid[z][k] == -1:
                            self.grid[z][k] = self.grid[i][k]
                            self.grid[i][k] = -1
                            break

        # down
        if action == (0, -1):
            for i in range(self.grid_size):
                for k in range(self.grid_size):
                    if self.grid[i][k] == -1:
                        continue
                    for z in range(self.grid_size - 1, -1, -1):
                        if self.grid[z][k] == -1:
                            self.grid[z][k] = self.grid[i][k]
                            self.grid[i][k] = -1
                            break

        # right
        if action == (1, 0):
            for i in range(self.grid_size):
                for k in range(self.grid_size):
                    if self.grid[k][i] == -1:
                        continue
                    for z in range(self.grid_size - 1, -1, -1):
                        if self.grid[z][i] == -1:
                            self.grid[z][i] = self.grid[k][i]
                            self.grid[k][i] = -1
                            break

        # left
        if action == (-1, 0):
            for i in range(self.grid_size - 1, -1, -1):
                for k in range(self.grid_size):
                    if self.grid[k][i] == -1:
                        continue
                    for z in range(self.grid_size):
                        if self.grid[z][i] is None:
                            self.grid[z][i] = self.grid[k][i]
                            self.grid[k][i] = -1
                            break

    def update(self, dt: float, events: list):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.handle_input((0, -1))
                if event.key == pygame.K_UP:
                    self.handle_input((0, 1))
                if event.key == pygame.K_RIGHT:
                    self.handle_input((1, 0))
                if event.key == pygame.K_LEFT:
                    self.handle_input((-1, 0))

    def render(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position, self.size))
