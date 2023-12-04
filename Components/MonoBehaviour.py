import pygame


class MonoBehaviour:
    def __init__(self, size: pygame.Vector2, position: pygame.Vector2, color: tuple, width: int = 0, border_radius: int = -1, border_top_left_radius: int = -1, border_top_right_radius: int = -1, border_bottom_left_radius: int = -1, border_bottom_right_radius: int = -1):
        self.size = size
        self.position = position
        self.color = color
        self.width, self.border_radius, self.border_top_left_radius, self.border_top_right_radius, self.border_bottom_left_radius, self.border_bottom_right_radius = width, border_radius, border_top_left_radius, border_top_right_radius, border_bottom_left_radius, border_bottom_right_radius

    def update(self, dt: float, events: list):
        pass

    def render(self, surface: pygame.Surface, ) -> pygame.Rect:
        return pygame.draw.rect(surface, self.color, pygame.Rect(self.position, self.size), self.width, self.border_radius, self.border_top_left_radius, self.border_top_right_radius, self.border_bottom_left_radius, self.border_bottom_right_radius)
