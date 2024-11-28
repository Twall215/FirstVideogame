import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    #overall class to manage game assets and behavior
    def __init__(self):
        pygame.init()
        #Initialize the game, and create game resources
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #Sets background color
        self.bg_color = (230, 230, 230)#Light grey bg 

    def _check_events(self):
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the ship to the right
                    self.ship.moving_right = True
                #Move the ship to the left
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            #Allows for movement to stop once key has been released
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
            #Updates Image on the screen and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #Make the most recently drawn screen visible
            pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
        

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
        
