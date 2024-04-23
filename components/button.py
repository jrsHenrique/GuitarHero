from tkinter import font
import pygame


class Button:
    def __init__(self, window, x, y, text, callback):
        self.window = window
        self.rect = pygame.Rect(x, y, 200, 50)
        self.text = text
        self.callback = callback

    def draw(self):
        # draw rectangle and text centered
        pygame.draw.rect(self.window, (0, 0, 255), self.rect)
        # assume font has been defined and loaded
        text_surface = font.render(self.text, True, (255, 255, 255))
        self.window.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def check_click(self, position):
        if self.rect.collidepoint(position):
            self.callback()

