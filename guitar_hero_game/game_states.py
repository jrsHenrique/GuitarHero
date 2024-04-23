from tkinter import RIGHT
from settings import *
import pygame, sys
from abc import ABC, abstractmethod
from player import Player

class GameState:
    def __init__(self, window, state, path):
        self.window = window
        self.click = False
        self.clock = pygame.time.Clock()
        self.state = state
        self.current_state = state
        self.background = pygame.image.load(path)

    @abstractmethod
    def run(self):
        pass


class MainMenu(GameState):
    def __init__(self, window):
        super().__init__(window, INIT, 'assets/images/tela_inicial.png')

    def run(self):
        while self.current_state == self.state:
            self.clock.tick(fps)  
            self.window.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.current_state = QUIT
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            self.window.blit(self.background, (0,0))
                
            mx, my = pygame.mouse.get_pos()
            start = pygame.Rect(width/2.1,380,width/8,100)
            exit = pygame.Rect(width/1.35,380,width/8,100)
            if start.collidepoint((mx,my)):
                if self.click:
                    self._currentstate = MUSIC

            if exit.collidepoint((mx,my)):
                if self.click:
                    pygame.quit()


            self.click = False
            pygame.display.flip()
            pygame.display.update()

            return self.state
        
class Selection(GameState):
    def __init__(self, window):
        super().__init__(window, MUSIC, 'assets/images/sem_goat.png')
        self.chosen_music = ''

    def run(self):
        while self.current_state == self.state:
            self.clock.tick(fps)  
            self.window.fill((0,0,0))

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.current_state = QUIT
                    pygame.quit()
                    sys.exit()
                
                if evento.type == pygame.KEYDOWN:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button:
                    if evento.button == 1:
                        self.click = True
            self.window.blit(self.background, (0,0))

            mx, my = pygame.mouse.get_pos()
            m1 = pygame.Rect(width/12,130,width/2,50)
            m2 = pygame.Rect(width/12,200,width/2.2,50)
            m3 = pygame.Rect(width/12,290,width/1.7,50)
            m4 = pygame.Rect(width/12,350,width/1.9,50)
            m5 = pygame.Rect(width/12,420,width/1.5,50)
            m6 = pygame.Rect(width/12,505,width/4.5,50)

            if m1.collidepoint((mx,my)):
                if self.click:
                    self.chosen_music = 'assets/musicas/riptide_vance-joy.mp3'
                    state = GAME
            if m2.collidepoint((mx,my)):
                if self.click:
                    self.chosen_music = 'assets/musicas/grapejuice-harry.mp3'
                    state = GAME
            if m3.collidepoint((mx,my)):
                if self.click:
                    self.chosen_music = 'assets/musicas/jose_gonzalez-killing_for_love.mp3'
                    state = GAME
            if m4.collidepoint((mx,my)):
                if self.click:
                    self.chosen_music = 'assets/musicas/clairo_flamin-hot-cheetos.mp3'
                    state = GAME
            if m5.collidepoint((mx,my)):
                if self.click:
                    self.chosen_music = 'assets/musicas/a-drowning_how-to-destroy-angels.mp3'
                    state = GAME
            if m6.collidepoint((mx,my)):
                if self.click:
                    self.chosen_music = 'assets/musicas/eyen_plaid.mp3'
                    state = GAME

            pygame.display.flip()
            pygame.display.update()
            self.click = False
            lista_return = [self.current_state,self.chosen_music]

        return lista_return
    
class Game(GameState):
    def __init__(self, window):
        super().__init__(window, GAME, 'assets/images/sem_goat.png')
        self.Player = Player()
        self.combo = 0

    def run(self):
        
