import pygame
class Text:
    def __init__(self, txt: str, font: str, size: int, position: pygame.Vector2, color: tuple):
        self.txt = txt
        self.font = font
        self.size = size
        self.position = position
        self.color: color



