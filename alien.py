import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #Single alien fleet

    def __init__(self, ai_game):
        #initializes alien and sets up starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the image and set its rect attribute
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #Starting in the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store exact horizontal position
        self.x = float(self.rect.x)
    
    #Adding movement
    def update(self):
        #Move the alien to the right or left
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
    
    #Putting up borders for the aliens
    def check_edges(self):
        #Return True if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True