import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #Single alien fleet

    def __init__(self, ai_game):
        #initializes alien and sets up starting position
        super().__init__()
        self.screen = ai_game.screen

        #load the image and set its rect attribute
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #Starting in the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store exact horizontal position
        self.x = float(self.rect.x)