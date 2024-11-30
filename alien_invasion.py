import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        #Fleet creation
        self._create_fleet()
        #Sets background color
        self.bg_color = (230, 230, 230)#Light grey bg 

    #Reads keypresses
    def _check_keydown_events(self, event):
            if event.key == pygame.K_RIGHT:
                #Move the ship to the right
                self.ship.moving_right = True
            #Move the ship to the left
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
    
    #Allows for action to stop once key has been released                
    def _check_keyup_events(self, event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
        
    def _check_events(self):
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)   

    def _fire_bullet(self):
        #Create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)        
        

    def _update_screen(self):
            #Updates Image on the screen and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #Make the most recently drawn screen visible
            for bullet in self.bullets.sprites():
                 bullet.draw_bullet()
            #puts the aliens on the screen
            self.aliens.draw(self.screen)
            pygame.display.flip()
    
    def _update_bullets(self):
            #Delete bullets that have disappeared
            for bullet in self.bullets.copy():
                 if bullet.rect.bottom <= 0:
                      self.bullets.remove(bullet)
            print(len(self.bullets))

    #Create an alien and place in the row
    def _create_alien(self, alien_number, row_number):
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien_height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)

    def _create_fleet(self):
         #Make an alien and find the number of aliens in a row
         #Spacing between each alien is one alien width
         alien = Alien(self)
         alien_width, alien_height = alien.rect.size
         available_space_x = self.settings.screen_width - (2*alien_width)
         number_aliens_x = available_space_x // (2*alien_width)
         #Height of the row
         ship_height = self.ship.rect.height
         available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
         number_rows = available_space_y // (2*alien_height)

         #Create the full fleet of aliens
         for row_number in range(number_rows):
              for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)
        
            

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
        
