import pygame
from Components.MonoBehaviour import MonoBehaviour


class Button(MonoBehaviour):
    def __init__(self, size: pygame.Vector2, position: pygame.Vector2, color: tuple):
        super().__init__(size, position, color)
        self.rect: pygame.Rect or None = None

    def is_collide(self, point: tuple):
        return self.rect.collidepoint(point[0], point[1])

    def update(self, dt: float, events: list) -> bool or None:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                return self.is_collide(mouse_pos)
        return None

    def render(self, surface: pygame.Surface):
        self.rect = super().render(surface)
