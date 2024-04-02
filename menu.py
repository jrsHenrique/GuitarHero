import pygame
from musics.disritmia import DisritmiaGame
from musics.internet_toxica import InternetToxicaGame
from musics.when_sun_goes_down import WhenSunGoesDownGame
from musics.wish_you_were_here import WishYouWereHereGame
from musics.stairway_to_heaven import StairwayToHeavenGame
from musics.smells_like_teen_spirit import SmellsLikeTeenSpiritGame

class StartGameEnvironment:        
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("imagens/gameback.jpeg").convert()
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.font = pygame.font.Font(None, 36)
        self.menu_options = ["Disritmia", "A internet é tóxica", "When the sun goes down", "Wish you were here", "Stairway to heaven", "Smells like teen Spirit", "Voltar"]
        self.selected_option = 0
        self.option_rects = []
        self.current_game = None

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

    def run(self):
        self.selected_option = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                    elif event.key == pygame.K_RETURN:
                        if(self.selected_option == 6):
                            return "initial_menu"
                        self.launch_selected_game()
                    elif event.key == pygame.K_ESCAPE:
                        return "initial_menu"
            self.draw_menu()
            pygame.display.flip()
            self.clock.tick(60)

    def launch_selected_game(self):
        # Launch the selected game. This is a placeholder for launching actual games.
        print(f"Launching {self.menu_options[self.selected_option]}")

class InitialMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.background_image = pygame.image.load("imagens/guitar.jpeg")
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))

    def run_game(self):
        menu_options = ["Start Game", "Instructions", "Quit"]
        selected_option = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(menu_options)
                    elif event.key == pygame.K_RETURN:
                        if selected_option == 0:
                            return "start_game"
                        elif selected_option == 1:
                            print("Showing instructions...")
                        elif selected_option == 2:
                            return "quit"
            
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background_image, (0, 0))
            for i, option in enumerate(menu_options):
                color = (255, 0, 0) if i == selected_option else (255, 255, 255)
                text = self.font.render(option, True, color)
                self.screen.blit(text, (400 - text.get_width() // 2, 200 + i * 50))
            pygame.display.flip()

def main_game_loop():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Guitar Hero")

    initial_menu = InitialMenu(screen)
    start_game_environment = StartGameEnvironment(screen)

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

if __name__ == "__main__":
    main_game_loop()
