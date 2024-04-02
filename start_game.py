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
        self.option_rects = []  # Rectangles for each option

    def draw_menu(self):
        # Fill the screen with the background image
        self.screen.blit(self.background, (0, 0))

        # Render and draw the menu options
        self.option_rects = []  # Clear previous option rectangles
        for i, option in enumerate(self.menu_options):
            text = self.font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (self.screen.get_width() // 2, 200 + i * 50)  # Position the text

            # Draw option rectangle
            option_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 5, text_rect.width + 20, text_rect.height + 10)
            self.option_rects.append(option_rect)

            # Highlight selected option
            if i == self.selected_option:
                pygame.draw.rect(self.screen, (255, 0, 0), option_rect)
            
            # Draw text
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
                        print("Selected option:", self.menu_options[self.selected_option])
            self.draw_menu()
            pygame.display.flip()

            # Cap the frame rate to 60 FPS
            self.clock.tick(60)

        pygame.quit()

# Example usage
if __name__ == "__main__":
    game = StartGameEnvironment()
    game.run()
