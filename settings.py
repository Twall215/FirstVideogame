class Settings:
    def __init__(self):
        #Initialize the game's Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        
        #Alien Settings
        self.alien_speed = 0.75
        self.fleet_drop_speed = 25
        #fleet_direction of 1 represents right; - 1 represents left
        self.fleet_direction = 1

        #Ship's Settings
        self.ship_speed = 1.5

        #Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230,230,230)
        self.bullets_allowed = 4