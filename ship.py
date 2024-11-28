import pygame
class Ship:
    #Ship of Theseus
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('spaceship.bmp')
        self.rect = self.image.get_rect()
       
        #Starts ship in the center
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)


        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Update the ships pos based on the movement flag
        #Update the ships x value, not the rect
        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x += self.settings.ship_speed
        #Update rect object from self.x
        self.rect.x - self.x
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)