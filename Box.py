import pygame
from Components.MonoBehaviour import MonoBehaviour
from Components.UI.Txt import Text


class Box(MonoBehaviour):
    def __init__(self, size: pygame.Vector2, position: pygame.Vector2, color: tuple, value: int):
        super().__init__(size, position, color)
        self.value = value
        self.text = Text(str(value), "Arial", 50, self.__generate_middle_point(), (255, 255, 255))

    def __generate_middle_point(self):
        return pygame.Vector2(self.position.x + self.size.x / 2, self.position.y + self.size.y / 2)

    def update_pos(self, position: pygame.Vector2):
        self.position = position
        self.text.update_position(self.__generate_middle_point())

    def mult_value(self):
        self.value *= 2
        self.text.update_text(str(self.value))

    def render(self, surface: pygame.Surface):
        super().render(surface)
        self.text.render(surface)
