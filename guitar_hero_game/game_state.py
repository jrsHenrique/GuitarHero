from states.init_menu import InitMenu
from states.music_selection import MusicSelection
# Import other states

class GameState:
    def __init__(self, window):
        self.window = window
        self.current_state = InitMenu(self.window, self.change_state)

    def update(self):
        self.current_state.display()

    def change_state(self, new_state_class):
        self.current_state = new_state_class(self.window, self.change_state)