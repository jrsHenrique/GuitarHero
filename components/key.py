import pygame
from settings import COLORS, KEY_MAPPINGS

class Key:
    def __init__(self, window, color, key_code, position):
        self.window = window
        self.color = COLORS[color]  # Assume COLORS is a dict of color name to RGB values
        self.key_code = key_code  # Pygame key code for the key
        self.position = position  # (x, y) position for the key on the screen
        self.radius = 20  # Radius of the key circle
        self.is_pressed = False

    def draw(self):
        """ Draw the key on the screen. """
        if self.is_pressed:
            # Draw a filled circle if the key is pressed
            pygame.draw.circle(self.window, self.color, self.position, self.radius)
        else:
            # Draw an empty circle otherwise
            outline_color = (255, 255, 255)  # White outline
            pygame.draw.circle(self.window, outline_color, self.position, self.radius, 2)
            pygame.draw.circle(self.window, self.color, self.position, self.radius - 5)

    def update(self, events):
        """ Update the key's pressed state based on keyboard events. """
        self.is_pressed = False
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == self.key_code:
                self.is_pressed = True
            elif event.type == pygame.KEYUP and event.key == self.key_code:
                self.is_pressed = False

    def check_collision(self, note):
        """ Check if the key collides with a note. """
        # Calculate distance to note's position
        note_position = note.position  # Assuming note object has a position attribute
        dx = note_position[0] - self.position[0]
        dy = note_position[1] - self.position[1]
        distance = (dx**2 + dy**2)**0.5
        return distance <= self.radius + note.radius
