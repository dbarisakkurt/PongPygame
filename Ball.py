import Constants
import pygame
import random

class Ball(pygame.sprite.Sprite):
    """Creates a Ball object"""

    def __init__(self):
        super(Ball, self).__init__()
        self.x = 300
        self.y = 300
        self.change_x = random.randrange(-20, 20)
        self.change_y = random.randrange(-20, 20)
        self.rect = pygame.Rect(self.x, self.y, 30, 100)

    def draw(self, screen):
        pygame.draw.circle(screen, Constants.BLUE, [self.x, self.y], Constants.BALL_SIZE)

    def update(self):
        self.x += self.change_x
        self.y += self.change_y
        self.rect = pygame.Rect(self.x, self.y, 30, 100)
 
        # Bounce the ball if needed
        if self.y > Constants.SCREEN_HEIGHT - Constants.BALL_SIZE or self.y < Constants.BALL_SIZE:
            self.change_y *= -1
