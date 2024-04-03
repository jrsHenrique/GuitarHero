import pygame

from ..menus.initial_menu import InitialMenu
from ..menus.music_menu import MusicMenu

def main_game_loop():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Guitar Hero")

    initial_menu = InitialMenu(screen)
    start_game_environment = MusicMenu(screen)

    current_state = "initial_menu"
    running = True
    while running:
        if current_state == "initial_menu":
            next_state = initial_menu.run_game()
        elif current_state == "start_game":
            next_state = start_game_environment.run()
        
        if next_state == "quit":
            running = False
        elif next_state:
            current_state = next_state

    pygame.quit()