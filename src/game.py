import pygame
from pygame.locals import *
from song import Song
from fret import Fret
import pygbutton
import tkinter as tk
import tkinter.filedialog as tkFileDialog

class GameMain():

    done = False
    color_bg = Color('black')

    def __init__(self, chart, width=1280, height=800):
        pygame.mixer.pre_init(44100,-16,2,2048)
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.chart = chart
        self.song = Song(self.chart, self)
        self.song.load_chart()
        self.frets = pygame.sprite.Group()
        self.fret0 = Fret(540, 720, Color('green'), 0, self)
        self.fret1 = Fret(590, 720, Color('red'), 1, self)
        self.fret2 = Fret(640, 720, Color('yellow'), 2, self)
        self.fret3 = Fret(690, 720, Color('blue'), 3, self)
        self.fret4 = Fret(740, 720, Color('orange'), 4, self)
        self.frets.add(self.fret0, self.fret1, self.fret2, self.fret3, self.fret4)
        fire_image_original = pygame.image.load('../assets/images/rXjEwA.gif.png').convert_alpha()
        self.fire_image = pygame.transform.scale(fire_image_original, (120, 120))  # Redimensionar a imagem para caber no botão
        self.fire_active = False
        self.score = 0
        self.multiplier = 1
        self.partial_multiplier = 0
        self.missed_notes = 0
  
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.score_text = self.font.render('0', True, Color('white'))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.center = (940, 400)
        self.multiplier_text = self.font.render('x1', True, Color('white'))
        self.multiplier_text_rect = self.score_text.get_rect()
        self.multiplier_text_rect.center = (940, 500)
        self.partial_text = self.font.render('', True, Color('white'))
        self.partial_text_rect = self.partial_text.get_rect()
        self.partial_text_rect.center = (940, 530)
        self.song.audio_stream.play()
        self.song_over = False

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.song.update()
            for note in self.song.note_list:
                note.update()
            for fret in self.frets:
                fret.update()
            self.draw()
            self.clock.tick(60)
            print(self.clock.get_fps())
        pygame.quit()

    def draw(self):
        self.screen.fill(self.color_bg)
        if not self.song_over:
            for fret in self.frets:
                pygame.draw.circle(self.screen, Color('black'), fret.rect.center, 25)
                pygame.draw.circle(self.screen, fret.color, fret.rect.center, 25, 5)
                if fret.held_note != None:
                    pygame.draw.line(self.screen, fret.color, fret.rect.center, (fret.rect.center[0], fret.held_note.sustain_y), 3)
                if fret.pressed:
                    pygame.draw.circle(self.screen, fret.color, fret.rect.center, 15)
                if fret.fire_active and fret.fire_timer > 0:
                    fire_pos = (fret.rect.center[0] - self.fire_image.get_width() // 2, 
                                fret.rect.center[1] - self.fire_image.get_height() * 0.7)
                    self.screen.blit(self.fire_image, fire_pos)
                    fret.fire_timer -= 1
                elif fret.fire_timer <= 0:
                    fret.fire_active = False

            for note in self.song.loaded_notes:
                pygame.draw.circle(self.screen, Color(note.color), note.rect.center, 20)
                if note.sustain:
                    if not note.held:
                        pygame.draw.line(self.screen, Color(note.color), note.rect.center, (note.rect.center[0], note.sustain_y))
                if note.hopo == True:
                    pygame.draw.circle(self.screen, Color('white'), note.rect.center, 10)
            self.score_text = self.font.render('{}'.format(self.score), True, Color('white'))
            self.screen.blit(self.score_text, self.score_text_rect)
            self.multiplier_text = self.font.render('x{}'.format(self.multiplier), True, Color('white'))
            self.screen.blit(self.multiplier_text, self.multiplier_text_rect)
            if self.multiplier == 4:
                self.partial_multiplier = 8
            self.partial_text = self.font.render('I'*self.partial_multiplier, True, Color('white'))
            self.screen.blit(self.partial_text, self.partial_text_rect)
            pygame.draw.line(self.screen, Color('green'), (1015, 517), (1015, 539.5), 4)

            if self.missed_notes >= 10:
                #stop media playback
                self.song.audio_stream.stop()
                self.song_over = True

        #The end of song screen
        else:
            self.final_score_text = self.font.render('Final Score: {}'.format(self.score), True, Color('blue'))
            self.final_score_rect = self.final_score_text.get_rect()
            self.final_score_rect.center = (self.width/2, self.height/2 - 50)
            self.play_again_text = self.font.render('Press A or Green to return to menu', True, Color('green'))
            self.play_again_rect = self.play_again_text.get_rect()
            self.play_again_rect.center = (self.width/2, self.height/2)
            self.quit_text = self.font.render('Press S or Red to quit', True, Color('red'))
            self.quit_rect = self.quit_text.get_rect()
            self.quit_rect.center = (self.width/2, self.height/2 + 50)
            self.screen.blit(self.final_score_text, self.final_score_rect)
            self.screen.blit(self.play_again_text, self.play_again_rect)
            self.screen.blit(self.quit_text, self.quit_rect)
        pygame.display.flip()  # put all the work on the screen

    def handle_events(self):

        events = pygame.event.get()
        
        for event in events:

            if event.type == pygame.QUIT:
                self.done = True

            #Keyboard controls
                #Use A,S,D,F,G to press frets
                #Use Left and Right arrow keys to strum
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.song.audio_stream.stop()
                    menu = Menu()
                    menu.main_loop()
                
                elif event.key == K_a:
                    self.fret0.pressed = True
                    if self.song_over:
                        menu = Menu()
                        menu.main_loop()
                    else:
                        self.fret0.check_for_strum()
                        
                elif event.key == K_s:
                    self.fret1.pressed = True
                    if self.song_over:
                        self.done = True
                    else:
                        self.fret0.check_for_strum()
                        
                elif event.key == K_d:
                    self.fret2.pressed = True
                    self.fret0.check_for_strum()
                    
                elif event.key == K_f:
                    self.fret3.pressed = True
                    self.fret0.check_for_strum()
                    
                elif event.key == K_g:
                    self.fret4.pressed = True
                    self.fret0.check_for_strum()
                    
                # elif event.key == K_LEFT or event.key == K_RIGHT:
                #     for fret in self.frets:
                #         if fret.pressed:
                #             fret.check_for_strum()d
            elif event.type == KEYUP:
                if event.key == K_a:
                    self.fret0.pressed = False
                elif event.key == K_s:
                    self.fret1.pressed = False
                elif event.key == K_d:
                    self.fret2.pressed = False
                elif event.key == K_f:
                    self.fret3.pressed = False
                elif event.key == K_g:
                    self.fret4.pressed = False

            #Controller controls
            elif event.type == JOYBUTTONDOWN:
                if event.button == 0:
                    self.fret0.pressed = True
                    if self.song_over:
                        menu = Menu()
                        menu.main_loop()
                    else:
                        self.fret0.check_for_strum()

                elif event.button == 1:
                    self.fret1.pressed = True
                    if self.song_over:
                        self.done = True
                    else:
                        self.fret1.check_for_strum()

                elif event.button == 3:
                    self.fret2.pressed = True
                    self.fret2.check_for_strum()

                elif event.button == 2:
                    self.fret3.pressed = True
                    self.fret3.check_for_strum()
                    
            elif event.type == JOYBUTTONUP:
                if event.button == 0:
                    self.fret0.pressed = False
                elif event.button == 1:
                    self.fret1.pressed = False
                elif event.button == 3:
                    self.fret2.pressed = False
                elif event.button == 2:
                    self.fret3.pressed = False
                elif event.button == 4:
                    self.fret4.pressed = False
                    
            elif event.type == JOYHATMOTION:
                if event.value == (0, -1) or event.value == (0, 1):
                    for fret in self.frets:
                        if fret.pressed:
                            fret.check_for_strum()

import pygame
import pygbutton
from pygame.locals import *

class Menu:
    done = False
    color_bg = pygame.Color('gray30')

    def __init__(self, width=800, height=600):
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.background_image = pygame.image.load("../assets/images/guitarnew.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))
        self.selected_button_index = 0

        # Definindo uma fonte personalizada para os botões
        button_font = pygame.font.Font(None, 24)

        # Ajustando as coordenadas dos botões para alinhá-los à esquerda
        button_x = 50
        button_y = 75
        button_spacing = 100
        button_width = 300


        self.slowride = pygbutton.PygButton((button_x, button_y, button_width, 50), 'Top Gun Anthem (Easy)', font=button_font)
        self.slowride.bgcolor = pygame.Color('green')

        button_y += button_spacing
        self.jukebox = pygbutton.PygButton((button_x, button_y, button_width, 50), 'Top Gun Anthem (Expert)', font=button_font)
        self.jukebox.bgcolor = pygame.Color('red')

        button_y += button_spacing
        self.topgun = pygbutton.PygButton((button_x, button_y, button_width, 50), 'Top Gun Anthem (Hard)', font=button_font)
        self.topgun.bgcolor = pygame.Color('yellow')

        button_y += button_spacing
        self.hail = pygbutton.PygButton((button_x, button_y, button_width, 50), 'Hail to the King (Expert)', font=button_font)
        self.hail.bgcolor = pygame.Color('blue')

        button_y += button_spacing
        self.choose = pygbutton.PygButton((button_x, button_y, button_width, 50), 'Choose a File...', font=button_font)
        self.choose.bgcolor = pygame.Color('orange')

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background_image, (0, 0))

        buttons = [self.slowride, self.jukebox, self.topgun, self.hail, self.choose]

        for i, button in enumerate(buttons):
            if i == self.selected_button_index:
                button.bgcolor = pygame.Color('white')
            else:
                button.bgcolor = pygame.Color('gray')

            button.draw(self.screen)

        pygame.display.flip()  # Put all the work on the screen

    def handle_events(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.done = True
                elif event.key == K_a:
                    game = GameMain('topgun(easy).chart')
                    game.main_loop()
                elif event.key == K_s:
                    game = GameMain('topgun(expert).chart')
                    game.main_loop()
                elif event.key == K_d:
                    game = GameMain('topgun.chart')
                    game.main_loop()
                elif event.key == K_f:
                    game = GameMain('hail.chart')
                    game.main_loop()
                elif event.key == K_g:
                    root = tk.Tk()
                    root.withdraw()
                    file_path = tkFileDialog.askopenfilename()
                    if file_path == '':
                        pass
                    else:
                        file_path = file_path.split('/')
                        game = GameMain(file_path[-1])
                        game.main_loop()
            elif event.type == JOYBUTTONDOWN:
                if event.button == 0:
                    game = GameMain('topgun(easy).chart')
                    game.main_loop()
                elif event.button == 1:
                    game = GameMain('topgun(expert).chart')
                    game.main_loop()
                elif event.button == 3:
                    game = GameMain('topgun.chart')
                    game.main_loop()
                elif event.button == 2:
                    game = GameMain('hail.chart')
                    game.main_loop()
                elif event.button == 4:
                    root = tk.Tk()
                    root.withdraw()
                    file_path = tkFileDialog.askopenfilename()
                    if file_path == '':
                        pass
                    else:
                        file_path = file_path.split('/')
                        game = GameMain(file_path[-1])
                        game.main_loop()

            if 'click' in self.slowride.handleEvent(event):
                game = GameMain('../assets/charts/topgun(easy).chart')
                game.main_loop()
            if 'click' in self.jukebox.handleEvent(event):
                game = GameMain('../assets/charts/topgun(expert).chart')
                game.main_loop()
            if 'click' in self.topgun.handleEvent(event):
                game = GameMain('../assets/charts/topgun.chart')
                game.main_loop()
            if 'click' in self.hail.handleEvent(event):
                game = GameMain('../assets/charts/hail.chart')
                game.main_loop()
            if 'click' in self.choose.handleEvent(event):
                root = tk.Tk()
                root.withdraw()
                file_path = tkFileDialog.askopenfilename()
                if file_path == '':
                    pass
                else:
                    file_path = file_path.split('/')
                    game = GameMain(file_path[-1])
                    game.main_loop()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    self.selected_button_index = (self.selected_button_index - 1) % 5
                elif event.key == K_DOWN:
                    self.selected_button_index = (self.selected_button_index + 1) % 5
                elif event.key == K_RETURN:
                    if self.selected_button_index == 0:
                        game = GameMain('../assets/charts/topgun(easy).chart')
                        game.main_loop()
                    elif self.selected_button_index == 1:
                        game = GameMain('../assets/charts/topgun(expert).chart')
                        game.main_loop()
                    elif self.selected_button_index == 2:
                        game = GameMain('../assets/charts/topgun.chart')
                        game.main_loop()
                    elif self.selected_button_index == 3:
                        game = GameMain('../assets/charts/hail.chart')
                        game.main_loop()
                    elif self.selected_button_index == 4:
                        root = tk.Tk()
                        root.withdraw()
                        file_path = tkFileDialog.askopenfilename()
                        if file_path == '':
                            pass
                        else:
                            file_path = file_path.split('/')
                            game = GameMain(file_path[-1])
                            game.main_loop()

menu = Menu()
menu.main_loop()
