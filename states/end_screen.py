import pygame
from settings import WIDTH, HEIGHT
from states.game_play import GamePlay

class EndScreen:
    def __init__(self, window, change_state, message, sub_message, color):
        self.window = window
        self.change_state = change_state
        self.font = pygame.font.SysFont('arial', 48)
        self.text = self.font.render(message, True, color)
        self.subtext = self.font.render(sub_message, True, (255, 255, 255))

    def display(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.text, (WIDTH / 2 - self.text.get_width() / 2, HEIGHT / 3))
        self.window.blit(self.subtext, (WIDTH / 2 - self.subtext.get_width() / 2, HEIGHT / 2))
        self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.restart_game()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()

    def restart_game(self):
        # This method can be overridden in subclass
        self.change_state(GamePlay)  # Assume GamePlay is correctly reinitialized

class WinScreen(EndScreen):
    def __init__(self, window, change_state):
        super().__init__(window, change_state, 
                         'Congratulations! You won!', 
                         'Press Enter to play again or ESC to exit.', 
                         (0, 255, 0))

class LoseScreen(EndScreen):
    def __init__(self, window, change_state):
        super().__init__(window, change_state, 
                         'Game Over. Try again!', 
                         'Press Enter to retry or ESC to exit.', 
                         (255, 0, 0))
