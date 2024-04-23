import pygame
from settings import *
from game_state import GameState

class GameWindow:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.state = GameState(self.window)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            self.state.update()
            pygame.display.flip()
            clock.tick(FPS)