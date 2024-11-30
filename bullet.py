import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #a class that manages bullets from the ship
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settimgs = ai_game.settings
        self.color = self.settings.bullet_color

        #bullet rect @ (0,0) and sets correct position
        self.rect = pygame.Rect(0,0 , self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store bullet's position as a decimal val
        self.y = float(self.rect.y)

    def update(self):
        #Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        #Update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)