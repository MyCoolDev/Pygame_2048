import pygame


class MonoBehaviour:
    def __init__(self, size: pygame.Vector2, position: pygame.Vector2, color: tuple):
        self.size = size
        self.position = position
        self.color = color

    def update(self, dt: float, events: list):
        pass

    def render(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position, self.size))
