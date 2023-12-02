import pygame
from Components.MonoBehaviour import MonoBehaviour


class Grid(MonoBehaviour):
    def __init__(self, size, position, base_color, node_color, grid_size, gap):
        super().__init__(size, position, base_color)
        self.node_color = node_color
        self.grid_size = grid_size
        self.gap = gap

