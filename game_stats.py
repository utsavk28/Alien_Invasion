class Gamestats() :
    def __init__(self,ai_settings):
        """Initialize Game Stats"""
        self.ai_settings = ai_settings
        self.score = 0
        self.high_score = 0
        self.level = 1
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
