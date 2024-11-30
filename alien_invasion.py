import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


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

        #Create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        #Fleet creation
        self._create_fleet()
        #Sets background color
        self.bg_color = (230, 230, 230)#Light grey bg 

        #Make play button
        self.play_button = Button(self, "Play")

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
         #starts a new game when the player clicks play
         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
         if button_clicked and not self.stats.game_active:
              #HIde the mouse cursor
              pygame.mouse.set_visible(False)
              #Resets stats
              self.stats.reset_stats()
              self.stats.game_active = True

              #Clear the board
              self.aliens.empty()
              self.bullets.empty()

              #Create a new fleet and center ship
              self._create_fleet()
              self.ship.center_ship()

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

            #Draw the play button if the game is inactive
            if not self.stats.game_active:
                 self.play_button.draw_button()

            pygame.display.flip()
    
    def _update_bullets(self):
            #Delete bullets that have disappeared
            for bullet in self.bullets.copy():
                 if bullet.rect.bottom <= 0:
                      self.bullets.remove(bullet)
            print(len(self.bullets))
            self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):       
            #Check for collision and deletes if True
            collisions = pygame.sprite.groupcollide(
                 self.bullets,self.aliens, True, True
            )
            if not self.aliens:
                 #Destroy existing bullets and create new fleet
                 self.bullets.empty()
                 self._create_fleet()

    #Create an alien and place in the row
    def _create_alien(self, alien_number, row_number):
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien_height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)

    def _create_fleet(self):
         #width of the row
         #Spacing between each alien is one alien width
         alien = Alien(self)
         alien_width, alien_height = alien.rect.size
         available_space_x = self.settings.screen_width - (2*alien_width)
         #Puts 9 aliens on screen
         number_aliens_x = available_space_x // (3*alien_width)
         #Height of the row
         ship_height = self.ship.rect.height
         available_space_y = (self.settings.screen_height - (10*alien_height) - ship_height) #Gives the player a fighting chance(4 rows)
         number_rows = available_space_y // (2*alien_height)

         #Create the full fleet of aliens
         for row_number in range(number_rows):
              for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)
        
    def _update_aliens(self):
        #Checks if the fleet is at an edge then updates the positions accordingly
        self._check_fleet_edges()
        self.aliens.update() 
        #Did the ship get hit?
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
              self._ship_hit()
        #Did they hit the ground?
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        #Respond if aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        #Drop the entire fleet and change the direction
        for alien in self.aliens.sprites():
              alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    #Respond to ship being hit by an alien
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            #Decrement ships_left
            self.stats.ships_left -= 1
            #Get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            #create a new fleet and recenter the ship
            self._create_fleet()
            self.ship.center_ship()
            #Pause
            sleep(0.5)
        else:
             self.stats.game_active = False
             pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
         screen_rect = self.screen.get_rect()
         for alien in self.aliens.sprites():
              if alien.rect.bottom >= screen_rect.bottom:
                   #Treat this the same as if the ship got hit
                    self._ship_hit()
                    break
              
    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
        
