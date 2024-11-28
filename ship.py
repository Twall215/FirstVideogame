import pygame
class Ship:
    #Ship of Theseus
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('spaceship.bmp')
        self.rect = self.image.get_rect()
       
        #Starts ship in the center
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Update the ships pos based on the movement flag
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)