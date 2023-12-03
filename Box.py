import pygame
from Components.MonoBehaviour import MonoBehaviour


class Box(MonoBehaviour):
    def __init__(self, size: pygame.Vector2, position: pygame.Vector2, color: tuple, value: int):
        super().__init__(size, position, color)
        self.value = value

    def update(self, dt: float, position: pygame.Vector2):
        self.position = position
