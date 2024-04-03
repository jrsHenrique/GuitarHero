import pygame

class InitialMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.background_image = pygame.image.load("assets/images/guitar.jpeg")
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
