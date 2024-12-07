class Settings:
    def __init__(self):
        #Initialize the game's static Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        #Ship's Settings
        self.ship_limit = 3
        
        #Bullet Settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (230,230,230)
        self.bullets_allowed = 4

        #Alien drop Settings
        self.fleet_drop_speed = 15

        #How quickly the game speeds up
        #Change difficulty here
        self.speedup_scale = 1.1
        #How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = .5

        self.alien_points = 50
        
        #fleet_direction of 1 represents right; - 1 represents left
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        


        
        

        

        