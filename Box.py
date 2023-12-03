import pygame
from Components.MonoBehaviour import MonoBehaviour


class Box(MonoBehaviour):
    def __init__(self, size: pygame.Vector2, position: pygame.Vector2, color: tuple):
        super().__init__(size, position, color)

    def update(self, dt: float, position: pygame.Vector2):
        self.position = position
