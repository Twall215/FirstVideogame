class GameStats:
    #Track stats for Alien Invasion

    def __init__(self, ai_game):
        
        #initialize stats
        self.settings = ai_game.settings
        self.reset_stats()
        #Start Alien Invasion in an inactive state
        self.game_active = False
        
    def reset_stats(self):
        #initialize stats that can change during the game
        self.ships_left = self.settings.ship_limit

    