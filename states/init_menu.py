import pygame
from settings import WIDTH, HEIGHT
from states.music_selection import MusicSelection

class InitMenu:
    def __init__(self, window, change_state):
        self.window = window
        self.change_state = change_state
        self.font = pygame.font.SysFont(None, 48)
        self.text = self.font.render('Press Any Key to Start', True, (255, 255, 255))

    def display(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.text, (WIDTH / 2 - 100, HEIGHT / 2 - 24))
        self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.change_state(MusicSelection)