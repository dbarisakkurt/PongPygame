from Constants import *
import pygame

class Player(pygame.sprite.Sprite):
    """Creates a Player object"""

    def __init__(self, x, y, key1, key2, pos1, pos2):
        super(Player, self).__init__()
        self.surf = pygame.Surface((x, y))
        self.surf.fill(BLUE)
        self.rect = pygame.Rect(pos1,pos2, 30, 100)
        self.key1=key1
        self.key2=key2

    def update(self, pressed_keys):
        if pressed_keys[self.key1]:
            self.rect.move_ip(0, -20)
        if pressed_keys[self.key2]:
            self.rect.move_ip(0, 20)

        # Keep player on the screen
        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
