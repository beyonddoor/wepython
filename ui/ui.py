import pygame
from pygame.font import *


class UIObject:
    def __init__(self, screen: pygame.Surface):
        self._screen = screen

    def draw(self):
        pass


class Text(UIObject):
    def __init__(self, screen, text, fontsize, color):
        super().__init__(screen)
        self.font = Font(None, fontsize)
        self.text = text
        self.color = color
        self.image = self.font.render(self.text, True, self.color)
        self.image_rect = self.image.get_rect()

    def draw(self):
        self._screen.blit(self.image, self.image_rect)

    @property
    def pos(self):
        return (self.image_rect.x, self.image_rect.y)

    @pos.setter
    def pos(self, value):
        self.image_rect.x = value[0]
        self.image_rect.y = value[1]
