import pygame

class BaseGame:
    def __init__(self, game_title):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.game_title = game_title
    
    def draw_game(self):
        self.screen.fill((0, 0, 0))
        text = self.font.render(f"{self.game_title} Game", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
            self.draw_game()
            self.clock.tick(60)