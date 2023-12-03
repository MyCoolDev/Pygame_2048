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
        self.box_size = pygame.Vector2((self.size.x - (self.grid_size + 1) * gap) / self.grid_size, (self.size.y - (self.grid_size + 1) * gap) / self.grid_size)
        self.init_grid()

    def init_grid(self):
        for i in range(self.grid_size):
            current = []

            for _ in range(self.grid_size):
                current.append(-1)

            self.grid.append(current)

        self.create_random_box()

    def __get_empty_places(self):
        positions = []
        for i in range(self.grid_size):
            for k in range(self.grid_size):
                if self.grid[i][k] == -1:
                    positions.append((k, i))

        return positions

    def create_random_box(self):
        # create a random (position) box with random choice(2, 4)
        positions = self.__get_empty_places()

        for i in range(self.grid_size):
            for k in range(self.grid_size):
                if self.grid[i][k] == -1:
                    positions.append((k, i))

        # this is a grid position: (0, 1) or (2, 1)
        pos = random.choice(positions)
        world_position_x = self.position.x + (self.box_size.x + self.gap) * pos[0] + self.gap
        world_position_y = self.position.y + (self.box_size.y + self.gap) * pos[1] + self.gap

        self.grid[pos[1]][pos[0]] = Box(self.box_size, pygame.Vector2(world_position_x, world_position_y), self.node_color, random.choice([2, 4]))

    def handle_input(self, action: str):
        # i - current row
        # k - current object in row
        # z - current row to checking with the k

        # down
        handled = []

        if action == "down":
            for i in range(self.grid_size - 2, -1, -1):
                for k in range(self.grid_size):
                    if self.grid[i][k] == -1:
                        continue

                    # check for sum to add to
                    for z in range(i + 1, self.grid_size):
                        if self.grid[z][k] != -1:
                            if self.grid[z][k].value == self.grid[i][k].value and (z, k) not in handled:
                                print(self.grid[z][k])
                                self.grid[z][k].mult_value()
                                self.grid[i][k] = -1
                                handled.append((z, k))
                            break

                    # if 'sumed' continue
                    if self.grid[i][k] == -1:
                        continue

                    # check for 'best' empty space
                    best = -1
                    for z in range(i + 1, self.grid_size):
                        if self.grid[z][k] == -1:
                            best = (z, k)

                    if best != -1:
                        self.grid[best[0]][best[1]] = self.grid[i][k]
                        self.grid[i][k] = -1

        elif action == "up":
            for i in range(1, self.grid_size):
                for k in range(self.grid_size):
                    if self.grid[i][k] == -1:
                        continue

                    # check for sum to add to
                    for z in range(i - 1, -1, -1):
                        if self.grid[z][k] != -1:
                            if self.grid[z][k].value == self.grid[i][k].value and (z, k) not in handled:
                                print(self.grid[z][k])
                                self.grid[z][k].mult_value()
                                self.grid[i][k] = -1
                                handled.append((z, k))
                            break

                    # if 'sumed' continue
                    if self.grid[i][k] == -1:
                        continue

                    # check for 'best' empty space
                    best = -1
                    for z in range(i - 1, -1, -1):
                        if self.grid[z][k] == -1:
                            best = (z, k)

                    if best != -1:
                        print(best)
                        self.grid[best[0]][best[1]] = self.grid[i][k]
                        self.grid[i][k] = -1

        elif action == "right":
            for i in range(self.grid_size - 2, -1, -1):
                for k in range(self.grid_size):
                    if self.grid[k][i] == -1:
                        continue

                    # check for sum to add to
                    for z in range(i + 1, self.grid_size):
                        if self.grid[k][z] != -1:
                            if self.grid[k][z].value == self.grid[k][i].value and (k, z) not in handled:
                                print(k, z)
                                self.grid[k][z].mult_value()
                                self.grid[k][i] = -1
                                handled.append((k, z))
                            break

                    # if 'sumed' continue
                    if self.grid[k][i] == -1:
                        continue

                    # check for 'best' empty space
                    best = -1
                    for z in range(i + 1, self.grid_size):
                        if self.grid[k][z] == -1:
                            best = (k, z)

                    if best != -1:
                        print(best)
                        self.grid[best[0]][best[1]] = self.grid[k][i]
                        self.grid[k][i] = -1

        elif action == "left":
            for i in range(1, self.grid_size):
                for k in range(self.grid_size):
                    if self.grid[k][i] == -1:
                        continue

                    # check for sum to add to
                    for z in range(i - 1, -1, -1):
                        if self.grid[k][z] != -1:
                            if self.grid[k][z].value == self.grid[k][i].value and (k, z) not in handled:
                                print(k, z)
                                self.grid[k][z].mult_value()
                                self.grid[k][i] = -1
                                handled.append((k, z))
                            break

                    # if 'sumed' continue
                    if self.grid[k][i] == -1:
                        continue

                    # check for 'best' empty space
                    best = -1
                    for z in range(i - 1, -1, -1):
                        if self.grid[k][z] == -1:
                            best = (k, z)

                    if best != -1:
                        print(best)
                        self.grid[best[0]][best[1]] = self.grid[k][i]
                        self.grid[k][i] = -1

        self.update_positions()
        self.create_random_box()

    def update_positions(self):
        for i in range(self.grid_size):
            for k in range(self.grid_size):
                if self.grid[i][k] != -1:
                    world_position_x = self.position.x + (self.box_size.x + self.gap) * k + self.gap
                    world_position_y = self.position.y + (self.box_size.y + self.gap) * i + self.gap

                    self.grid[i][k].update_pos(pygame.Vector2(world_position_x, world_position_y))

    def update(self, dt: float, events: list):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.handle_input("down")
                if event.key == pygame.K_UP:
                    self.handle_input("up")
                if event.key == pygame.K_RIGHT:
                    self.handle_input("right")
                if event.key == pygame.K_LEFT:
                    self.handle_input("left")

    def render(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position, self.size))

        for i in range(len(self.grid)):
            for k in range(len(self.grid[i])):
                if self.grid[i][k] != -1:
                    self.grid[i][k].render(surface)
