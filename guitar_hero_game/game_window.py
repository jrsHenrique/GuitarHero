import pygame
from settings import *
from game_states import *

class GameWindow:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Guitar Hero")

    def run(self):
        state = INIT
        while state != QUIT:
            if state == INIT:
                state = main_menu(self.window) 
            if state == MUSIC:
                state = selection(self.window)
            if state[0] == 2:
                state = game(self.window)
                data = state
            if data[0] == 3:
                state = won(self.window,data)
            if data[0] == 5:
                state = lost(self.window)

        pygame.quit()