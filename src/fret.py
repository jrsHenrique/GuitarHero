import pygame
from pygame.locals import *

class Fret(pygame.sprite.Sprite):
    def __init__(self, x, y, color, num, game):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.num = num
        self.game = game
        self.pressed = False
        self.held_note = None
        self.fire_active = False
        self.fire_timer = 0

        self.image = pygame.Surface([50, 50])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def check_for_strum(self):
        note_hit_list = pygame.sprite.spritecollide(self, self.game.song.loaded_notes, False)
        for note in note_hit_list:
            if note.rect.center[1] > 700 and note.rect.center[1] < 740 and note in self.game.song.loaded_notes:
                hit = False
                if note.chord:
                    note.dead = True
                    hit = True
                else:
                    for fret in self.game.frets:
                        if fret.pressed and fret.num > self.num:
                            break
                    else:
                        note.dead = True
                        hit = True
                
                if hit:
                    self.game.song.previous_note_hit = True
                    self.game.score += 50 * self.game.multiplier
                    self.game.partial_multiplier += 1
                    self.game.hit_notes += 1  # Increment hit notes counter
                    self.fire_active = True
                    self.fire_timer = 10
                
                if note.sustain != 0 and self.pressed:
                    note.held = True
                    self.held_note = note


    def update(self):
        note_hit_list = pygame.sprite.spritecollide(self, self.game.song.loaded_notes, False)
        for note in note_hit_list:
            if note.rect.center[1] > 700 and note.rect.center[1] < 740 and note in self.game.song.loaded_notes:
                hit = False
                if note.hopo == True and self.game.song.previous_note_hit == True and self.pressed == True:
                    if note.chord:
                        note.dead = True
                        hit = True
                    else:
                        for fret in self.game.frets:
                            if fret.pressed and fret.num > self.num:
                                break
                        else:
                            note.dead = True
                            hit = True
                
                if hit:
                    self.game.song.previous_note_hit = True
                    self.game.score += 50 * self.game.multiplier
                    self.game.partial_multiplier += 1
                    self.game.hit_notes += 1  # Increment hit notes counter
                
                if note.sustain != 0 and self.pressed:
                    note.held = True
                    self.held_note = note

        #checking for missed notes
        for note in self.game.song.loaded_notes:
        # Assume the note miss threshold is y = 760, adjust as necessary
            if note.rect.top > 760 and not note.dead and not note.held:
                note.dead = True  # Mark the note as dead to avoid multiple counts
                self.game.missed_notes += 1

        if self.held_note != None:
            self.game.score += 2 * self.game.multiplier
            if self.held_note.sustain_y  > 720:
                self.held_note = None
            if not self.pressed:
                self.held_note = None
        if self.game.partial_multiplier >= 9:
            self.game.partial_multiplier = 0
            if self.game.multiplier != 4:
                self.game.multiplier += 1
    

