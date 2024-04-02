import pygame
from start_game import StartGameEnvironment

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Guitar Hero")

# Set up the menu options
menu_options = ["Start Game", "Instructions", "Quit"]
selected_option = 0

# Set up the font
font = pygame.font.Font(None, 36)

# Load the background image
background_image = pygame.image.load("imagens/guitar.jpeg")
background_image = pygame.transform.scale(background_image, (window_width, window_height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    # Start game
                    start_game_environment = StartGameEnvironment()
                    start_game_environment.run()
                elif selected_option == 1:
                    # Show instructions
                    print("Showing instructions...")
                elif selected_option == 2:
                    # Quit game
                    running = False

    # Fill the window with a black background
    window.fill((0, 0, 0))

    # Draw the background image
    window.blit(background_image, (0, 0))

    # Draw the menu options
    for i, option in enumerate(menu_options):
        text = font.render(option, True, (255, 255, 255))
        if i == selected_option:
            pygame.draw.rect(window, (255, 0, 0), (window_width // 2 - 100, 200 + i * 50, 200, 40))
        window.blit(text, (window_width // 2 - text.get_width() // 2, 200 + i * 50))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
