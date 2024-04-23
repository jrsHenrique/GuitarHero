import pygame
from guitar_hero_game.settings import WIDTH, HEIGHT, SONG_END_TIMES
from states.game_play import GamePlay

class MusicSelection:
    def __init__(self, window, change_state):
        self.window = window
        self.change_state = change_state
        self.font = pygame.font.SysFont(None, 36)
        self.options = list(SONG_END_TIMES.keys())
        self.selected = 0

    def display(self):
        self.window.fill((0, 0, 0))
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255) if i == self.selected else (100, 100, 100))
            self.window.blit(text, (50, 30 + i * 40))
        self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.selected > 0:
                    self.selected -= 1
                elif event.key == pygame.K_DOWN and self.selected < len(self.options) - 1:
                    self.selected += 1
                elif event.key == pygame.K_RETURN:
                    self.change_state(GamePlay, self.options[self.selected])
