import pygame
import random
from settings import WIDTH, HEIGHT, FPS, SONG_END_TIMES, COLORS, KEY_MAPPINGS
from components.note import Note
from components.key import Key
from states.end_screen import *

class GamePlay:
    def __init__(self, window, change_state, song_path):
        self.window = window
        self.change_state = change_state
        self.song_path = song_path
        self.notes = pygame.sprite.Group()
        self.keys = [Key(self.window, color, position) for color, position in KEY_MAPPINGS.items()]
        self.load_song(song_path)
        self.score = 0
        self.combo = 0
        self.missed_notes = 0
        self.start_time = pygame.time.get_ticks()

    def load_song(self, song_path):
        self.song_length = SONG_END_TIMES[song_path]
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

    def display(self):
        self.window.fill((0, 0, 0))
        current_time = (pygame.time.get_ticks() - self.start_time) / 1000
        if current_time > self.song_length:
            self.evaluate_performance()
        
        self.manage_notes()
        for note in self.notes:
            note.update()
            note.draw(self.window)
        for key in self.keys:
            key.draw()

        self.check_events()
        self.update_score()

    def manage_notes(self):
        # This should ideally be time or beat based
        if random.randint(0, 50) == 25:
            color = random.choice(list(COLORS.keys()))
            new_note = Note(color, COLORS[color], KEY_MAPPINGS[color][0], KEY_MAPPINGS[color][1])
            self.notes.add(new_note)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.change_state(None)
            elif event.type == pygame.KEYDOWN:
                for key in self.keys:
                    if event.key == key.key_code:
                        hit = False
                        for note in self.notes:
                            if key.check_collision(note):
                                self.score += 1
                                self.combo += 1
                                note.kill()
                                hit = True
                                break
                        if not hit:
                            self.combo = 0
                            self.missed_notes += 1

    def update_score(self):
        # Simple score and combo display
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        combo_text = font.render(f'Combo: {self.combo}', True, (255, 255, 0))
        self.window.blit(score_text, (10, 10))
        self.window.blit(combo_text, (10, 50))

    def evaluate_performance(self):
        if self.score / (self.score + self.missed_notes) > 0.75:
            self.change_state(WinScreen)
        else:
            self.change_state(LoseScreen)
