import pygame
from settings import WIDTH, HEIGHT, COLORS

class Note(pygame.sprite.Sprite):
    def __init__(self, color, position, speed_y=5):
        super().__init__()
        self.color = COLORS[color]  # Cor da nota, obtida do dicionário global COLORS
        self.image = pygame.Surface((20, 20))  # Cria uma superfície para a nota
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=position)
        self.speed_y = speed_y  # Velocidade vertical da nota

    def update(self):
        """ Move a nota para baixo com base na sua velocidade. """
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.kill()  # Remove a nota do grupo de sprites se ela sair da tela

    def draw(self, window):
        """ Desenha a nota na janela especificada. """
        window.blit(self.image, self.rect)

