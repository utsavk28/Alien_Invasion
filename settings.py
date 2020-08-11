class Settings():

    def __init__(self):
        """Initialize the GAME'S SETTINGS"""
        # SCREEN Settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = 255,255,255
        self.bullet_allowed = 3

        self.speed_up_scale = 1.1
        self.score_up_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.bullet_speed_factor = 3
        # Alien Settings
        self.aliens_speed_factor = 1
        self.fleet_drop_speed = 2
        # Ship Settings
        self.ship_speed_factor = 1.5
        # Fleet direction 1 represents right and -1 represent left
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.bullet_speed_factor *= self.speed_up_scale
        self.aliens_speed_factor *= self.speed_up_scale
        self.fleet_drop_speed *= self.speed_up_scale
        self.ship_speed_factor *= self.speed_up_scale
        self.alien_points *= self.score_up_scale


