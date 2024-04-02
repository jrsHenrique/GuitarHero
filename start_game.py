import pygame

class StartGameEnvironment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()  # For controlling the frame rate

        # Load the background image and scale it to match the screen dimensions
        self.background = pygame.image.load("imagens/gameback.jpeg").convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        # Set up the font
        self.font = pygame.font.Font(None, 36)

        # Set up the menu options
        self.menu_options = ["Disritmia", "A internet é tóxica", "When the sun goes down", "Wish you were here", "Stairway to heaven", "Smells like teen Spirit"]
        self.selected_option = None

    def draw_menu(self):
        # Fill the screen with the background image
        self.screen.blit(self.background, (0, 0))

        # Render and draw the menu options
        for i, option in enumerate(self.menu_options):
            text = self.font.render(option, True, (255, 255, 255))
            if i == self.selected_option:
                pygame.draw.rect(self.screen, (255, 0, 0), (self.screen.get_width() // 2 - 100, 200 + i * 50, 200, 40))
            self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, 200 + i * 50))

        # Draw the selected option

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.selected_option = self.menu_options[0]
                    elif event.key == pygame.K_2:
                        self.selected_option = self.menu_options[1]
                    elif event.key == pygame.K_3:
                        self.selected_option = self.menu_options[2]
                    elif event.key == pygame.K_4:
                        self.selected_option = self.menu_options[3]
                    elif event.key == pygame.K_5:
                        self.selected_option = self.menu_options[4]
                    elif event.key == pygame.K_6:
                        self.selected_option = self.menu_options[5]

            self.draw_menu()
            pygame.display.flip()

            # Cap the frame rate to 60 FPS
            self.clock.tick(60)

        pygame.quit()

# Example usage
if __name__ == "__main__":
    game = StartGameEnvironment()
    game.run()
