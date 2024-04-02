import pygame
from musics.disritmia import DisritmiaGame
from musics.internet_toxica import InternetToxicaGame
from musics.when_sun_goes_down import WhenSunGoesDownGame
from musics.wish_you_were_here import WishYouWereHereGame
from musics.stairway_to_heaven import StairwayToHeavenGame
from musics.smells_like_teen_spirit import SmellsLikeTeenSpiritGame

class StartGameEnvironment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("imagens/gameback.jpeg").convert()
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.font = pygame.font.Font(None, 36)
        self.menu_options = ["Disritmia", "A internet é tóxica", "When the sun goes down", "Wish you were here", "Stairway to heaven", "Smells like teen Spirit"]
        self.selected_option = None
        self.option_rects = []  # Rectangles for each option
        self.current_game = None  # Track the current game state

    def draw_menu(self):
        self.screen.blit(self.background, (0, 0))
        self.option_rects = []  # Clear previous option rectangles
        for i, option in enumerate(self.menu_options):
            text = self.font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, 200 + i * 50))  # Position the text
            option_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 5, text_rect.width + 20, text_rect.height + 10)
            self.option_rects.append(option_rect)
            if i == self.selected_option:
                pygame.draw.rect(self.screen, (255, 0, 0), option_rect)
            self.screen.blit(text, text_rect)

    def draw_back_button(self):
        text = self.font.render("Back", True, (255, 255, 255))
        text_rect = text.get_rect(midtop=(self.screen.get_width() // 2, 500))
        pygame.draw.rect(self.screen, (0, 255, 0), text_rect.inflate(20, 10))
        self.screen.blit(text, text_rect)

    def run(self):
        self.selected_option = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                    elif event.key == pygame.K_RETURN:
                        if self.current_game is None:
                            self.launch_selected_game()
                    elif event.key == pygame.K_BACKSPACE:
                        if self.current_game is not None:
                            self.return_to_main_menu()
            if self.current_game is None:
                self.draw_menu()
            else:
                self.current_game.run()
            self.draw_back_button()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def launch_selected_game(self):
        if self.selected_option == 0:
            self.current_game = DisritmiaGame()
        elif self.selected_option == 1:
            self.current_game = InternetToxicaGame()
        elif self.selected_option == 2:
            self.current_game = WhenSunGoesDownGame()
        elif self.selected_option == 3:
            self.current_game = WishYouWereHereGame()
        elif self.selected_option == 4:
            self.current_game = StairwayToHeavenGame()
        elif self.selected_option == 5:
            self.current_game = SmellsLikeTeenSpiritGame()

    def return_to_main_menu(self):
        self.current_game = None

# Example usage
if __name__ == "__main__":
    game = StartGameEnvironment()
    game.run()
