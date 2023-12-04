import pygame
from Components.MonoBehaviour import MonoBehaviour
from Components.UI.Txt import Text


class Button(MonoBehaviour):
    def __init__(self, size: pygame.Vector2, position: pygame.Vector2, color: tuple, content: str, font: str, font_size: int, text_color: tuple, width: int = 0, border_radius: int = -1, border_top_left_radius: int = -1, border_top_right_radius: int = -1, border_bottom_left_radius: int = -1, border_bottom_right_radius: int = -1):
        super().__init__(size, position - 1/2 * size, color, width, border_radius, border_top_left_radius, border_top_right_radius, border_bottom_left_radius, border_bottom_right_radius)
        self.rect: pygame.Rect or None = None
        self.content = content
        self.font_size = font_size
        self.text_color = text_color
        self.text = Text(content, font, font_size, position, text_color)

    def is_collide(self, point: tuple):
        return self.rect.collidepoint(point[0], point[1])

    def update(self, dt: float, events: list) -> bool:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                return self.is_collide(mouse_pos)
        return False

    def render(self, surface: pygame.Surface):
        self.rect = super().render(surface)
        self.text.render(surface)
