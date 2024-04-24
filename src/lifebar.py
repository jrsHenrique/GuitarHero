import pygame

class Lifebar:
    def __init__(self, max_life, game):
        self.max_life = max_life
        self.current_life = max_life
        self.game = game
        self.width = 200
        self.height = 20
        self.life_rect = pygame.Rect(940, 250, self.width, self.height)  # Adjust position as needed

    def update_life(self, hit=False, miss=False):
        self.current_life = self.max_life - self.game.missed_notes 
        self.current_life = max(0, min(self.current_life, self.max_life))
        
    def draw(self):
        # Change color based on life percentage
        life_percentage = self.current_life / self.max_life
        if life_percentage > 0.7:
            color = pygame.Color('green')
        elif life_percentage > 0.3:
            color = pygame.Color('yellow')
        else:
            color = pygame.Color('red')

        # Draw the lifebar
        current_width = self.width * life_percentage
        life_bar_rect = pygame.Rect(self.life_rect.left, self.life_rect.top, current_width, self.height)
        pygame.draw.rect(self.game.screen, color, life_bar_rect)
        pygame.draw.rect(self.game.screen, pygame.Color('white'), self.life_rect, 2)  # Border for visibility